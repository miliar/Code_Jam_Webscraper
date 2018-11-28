#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <hash_map>
#include <sstream>
#include <time.h>
#include <cmath>
#include <iomanip>

using namespace std;

const int FeaNum = 93; //95+1-3(thet0)
const int Each_TimeStemp_FeaNum = 19;
const int Time_fea1 = 7; //featureµÄÊ±¼ä¶Î»®·Ö
const int Time_fea2 = 15;
const int Time_fea3 = 31;
const int Time_fea4 = 60;
const int Time_fea5 = 93;

char* LogFile = "LOG.txt";
char* LogFile_IIDindex = "LOG_IID.txt";

int Plus_example = 0;

class Type_Days{
public:
	int type;
	int days;
};

class Item_Pop_global{
public:
	vector<double> time1; //×î½üµÄÒ»¶ÎÊ±¼ä
	vector<double> time2;
	vector<double> time3;
	vector<double> time4;
	vector<double> time5;
	vector<int> user_num1;
	vector<int> user_num2;
	vector<int> user_num3;
	vector<int> user_num4;
	vector<int> user_num5;
};

class feature_space{
public:
	double feature[FeaNum];
	double GroundTruth;
};

class feature_timestemp_asist{
public:
	vector<double> type_count;
	int IID_Num;
	feature_timestemp_asist(): IID_Num(0){}
};

int Init_FeaSpa(feature_space& f)
{
	f.feature[0] = 1;
	for (int i=1; i!=FeaNum; i++)
	{
		f.feature[i] = 0;
	}
	f.GroundTruth = 0;
	return 0;
}

int InitItem_Pop(Item_Pop_global& amount)
{
	for (int i=0; i!=4; i++)
	{
		amount.time1.push_back(0);
		amount.time2.push_back(0);
		amount.time3.push_back(0);
		amount.time4.push_back(0);
		amount.time5.push_back(0);
		amount.user_num1.push_back(0);
		amount.user_num2.push_back(0);
		amount.user_num3.push_back(0);
		amount.user_num4.push_back(0);
		amount.user_num5.push_back(0);
	}
	return 0;
}

bool compareSTB(int x, int y)
{
	return x < y;
}

typedef map<int, vector<Type_Days> > log_type;
typedef pair<int,int> UID_IID_Pair;

int ReadLog_UIDindex(char* filename, map<int, log_type>& RawLog)
{
	FILE *fp = freopen(filename,"r",stdin);
	if(fp)
		printf("Open LogFile successfully!\n");
	else
	{
		printf("Open LogFile error!\n");
		exit(-1);
	}

	int uid = 0, iid = 0, type, days;
	int uid_old = 0, iid_old = 0;
	log_type log_each_brand;
	int line = 0;
	while(~scanf("%d,%d,%d,%d",&uid,&iid,&type,&days))
	{
		line++;
		if(line % 10000 == 0)
			cout<<line<<endl;

		Type_Days TDas;
		TDas.type = type;
		TDas.days = days - 14;

		if(line == 1)
		{
			log_each_brand[iid].push_back(TDas);

			iid_old = iid;
			uid_old = uid;
			continue;
		}

		if(uid != uid_old)
		{
			RawLog[uid_old] = log_each_brand;

			log_each_brand.clear();
			log_each_brand[iid].push_back(TDas);
			uid_old = uid;
			iid_old = iid;
			continue;
		}

		log_each_brand[iid].push_back(TDas);

		if(line == 182879)
		{
			RawLog[uid_old] = log_each_brand;
		}
	}
	fclose(fp);

	return 0;
}

int ConstructSets(map<int, log_type>& RawLog, map<int, log_type>& RawLog_123, map<int, log_type>& RawLog_4, map<int, log_type>& RawLog_234)
{
	for (map<int, log_type>::iterator it = RawLog.begin();it!=RawLog.end(); it++)
	{
		int uid = it->first;
		log_type Ulog = it->second;
		log_type log_each_brand_123, log_each_brand_4, log_each_brand_234;

		for (log_type::iterator it2 = Ulog.begin(); it2!=Ulog.end(); it2++)
		{
			int iid = it2->first;
			vector<Type_Days> TdaysVec = it2->second;

			for (int i=0; i!=TdaysVec.size(); i++)
			{
				int days = TdaysVec[i].days;
				if(days <= 93)
					log_each_brand_123[iid].push_back(TdaysVec[i]);
				else
					log_each_brand_4[iid].push_back(TdaysVec[i]);
				if(days > 31)
					log_each_brand_234[iid].push_back(TdaysVec[i]);
			}
		}

		//if(log_each_brand_123.size()!=0)
			RawLog_123[uid] = log_each_brand_123;
		//if(log_each_brand_4.size()!=0)
			RawLog_4[uid] = log_each_brand_4;
		//if(log_each_brand_234.size()!=0)
			RawLog_234[uid] = log_each_brand_234;
	}

	return 0;
}

int GetItemPopGlobal_GroundTruth(map<int, log_type>& RawLog_iid, map<int, Item_Pop_global>& Item_Pop, map<UID_IID_Pair, int>& GroundTruth )
{
	Item_Pop_global amount;
	InitItem_Pop(amount);

	int line = 0;
	for (map<int, log_type>::iterator it = RawLog_iid.begin(); it!=RawLog_iid.end(); it++)
	{
		line++;
		if(line % 1000 == 0)
			cout<<line<<endl;

		int iid = it->first;
		log_type log = (it->second);

		Item_Pop_global count_temp;

		InitItem_Pop(count_temp);

		for (log_type::iterator it2=log.begin();it2!=log.end(); it2++)
		{
			int UID = it2->first;
			vector <Type_Days> Tdays = it2->second;

			int a[5] = {0,0,0,0,0};

			for (int i=0; i!=Tdays.size(); i++)
			{
				int type = Tdays[i].type;
				int days = Tdays[i].days;

				if(days >93 && type == 1)
				{
					//if (UID == 1086750)
					//{
					//	cout<<iid<<endl;
					//}
					GroundTruth[make_pair(UID,iid)]++;
				}

				if(days <= 93)
				{
					if (abs(94-days) <= Time_fea1)
					{
						count_temp.time1[type]++;
						amount.time1[type]++;
						if(a[0] == 0)
						{
							count_temp.user_num1[type]++;
							a[0] = 1;
						}
					}
					if (abs(94-days)>Time_fea1 && abs(94-days)<=Time_fea2)
					{
						count_temp.time2[type]++;
						amount.time2[type]++;
						if(a[1] == 0)
						{
							count_temp.user_num2[type]++;
							a[1] = 1;
						}
					}
					if (abs(94-days)>Time_fea2 && abs(94-days)<=Time_fea3)
					{
						count_temp.time3[type]++;
						amount.time3[type]++;
						if(a[2] == 0)
						{
							count_temp.user_num3[type]++;
							a[2] = 1;
						}
					}
					if (abs(94-days)>Time_fea3 && abs(94-days)<=Time_fea4)
					{
						count_temp.time4[type]++;
						amount.time4[type]++;
						if(a[3] == 0)
						{
							count_temp.user_num4[type]++;
							a[3] = 1;
						}
					}
					if (abs(94-days)>Time_fea4 && abs(94-days)<=Time_fea5)
					{
						count_temp.time5[type]++;
						amount.time5[type]++;
						if(a[4] == 0)
						{
							count_temp.user_num5[type]++;
							a[4] = 1;
						}
					}
				}
			}
		}

		Item_Pop[iid] = count_temp;
	}

	for (map<int, Item_Pop_global>::iterator it=Item_Pop.begin(); it != Item_Pop.end(); it++)
	{
		for (int i=0; i!=4; i++)
		{
			if(amount.time1[i] !=0 )
				it->second.time1[i] = it->second.time1[i] * it->second.user_num1[i] / amount.time1[i];
			if(amount.time2[i] !=0 )
				it->second.time2[i] = it->second.time2[i] * it->second.user_num2[i] / amount.time2[i];
			if(amount.time3[i] !=0 )
				it->second.time3[i] = it->second.time3[i] * it->second.user_num3[i] / amount.time3[i];
			if(amount.time4[i] !=0 )
				it->second.time4[i] = it->second.time4[i] * it->second.user_num4[i] / amount.time4[i];
			if(amount.time5[i] !=0 )
				it->second.time5[i] = it->second.time5[i] * it->second.user_num5[i] / amount.time5[i];
		}
	}
	return 0;
}

int GetItemPopGlobal_GroundTruth_final234(map<int, log_type>& RawLog_iid, map<int, Item_Pop_global>& Item_Pop, map<UID_IID_Pair, int>& GroundTruth )
{
	Item_Pop_global amount;
	InitItem_Pop(amount);

	int line = 0;
	for (map<int, log_type>::iterator it = RawLog_iid.begin(); it!=RawLog_iid.end(); it++)
	{
		line++;
		if(line % 1000 == 0)
			cout<<line<<endl;

		int iid = it->first;
		log_type log = (it->second);

		Item_Pop_global count_temp;

		InitItem_Pop(count_temp);

		for (log_type::iterator it2=log.begin();it2!=log.end(); it2++)
		{
			int UID = it2->first;
			vector <Type_Days> Tdays = it2->second;

			int a[5] = {0,0,0,0,0};

			for (int i=0; i!=Tdays.size(); i++)
			{
				int type = Tdays[i].type;
				int days = Tdays[i].days;

				if(days >93 && type == 1)
				{
					//if (UID == 1086750)
					//{
					//	cout<<iid<<endl;
					//}
					GroundTruth[make_pair(UID,iid)]++;
				}

				if(days > 31)
				{
					if (abs(126-days) <= Time_fea1)
					{
						count_temp.time1[type]++;
						amount.time1[type]++;
						if(a[0] == 0)
						{
							count_temp.user_num1[type]++;
							a[0] = 1;
						}
					}
					if (abs(126-days)>Time_fea1 && abs(126-days)<=Time_fea2)
					{
						count_temp.time2[type]++;
						amount.time2[type]++;
						if(a[1] == 0)
						{
							count_temp.user_num2[type]++;
							a[1] = 1;
						}
					}
					if (abs(126-days)>Time_fea2 && abs(126-days)<=Time_fea3)
					{
						count_temp.time3[type]++;
						amount.time3[type]++;
						if(a[2] == 0)
						{
							count_temp.user_num3[type]++;
							a[2] = 1;
						}
					}
					if (abs(126-days)>Time_fea3 && abs(126-days)<=Time_fea4)
					{
						count_temp.time4[type]++;
						amount.time4[type]++;
						if(a[3] == 0)
						{
							count_temp.user_num4[type]++;
							a[3] = 1;
						}
					}
					if (abs(126-days)>Time_fea4 && abs(126-days)<=Time_fea5)
					{
						count_temp.time5[type]++;
						amount.time5[type]++;
						if(a[4] == 0)
						{
							count_temp.user_num5[type]++;
							a[4] = 1;
						}
					}
				}
			}
		}

		Item_Pop[iid] = count_temp;
	}

	for (map<int, Item_Pop_global>::iterator it=Item_Pop.begin(); it != Item_Pop.end(); it++)
	{
		for (int i=0; i!=4; i++)
		{
			if(amount.time1[i] !=0 )
				it->second.time1[i] = it->second.time1[i] * it->second.user_num1[i] / amount.time1[i];
			if(amount.time2[i] !=0 )
				it->second.time2[i] = it->second.time2[i] * it->second.user_num2[i] / amount.time2[i];
			if(amount.time3[i] !=0 )
				it->second.time3[i] = it->second.time3[i] * it->second.user_num3[i] / amount.time3[i];
			if(amount.time4[i] !=0 )
				it->second.time4[i] = it->second.time4[i] * it->second.user_num4[i] / amount.time4[i];
			if(amount.time5[i] !=0 )
				it->second.time5[i] = it->second.time5[i] * it->second.user_num5[i] / amount.time5[i];
		}
	}
	return 0;
}

int Fea_Time_Area(int time)
{
	if(time <= Time_fea1)
		return 0;
	if(time > Time_fea1 && time <= Time_fea2)
		return 1;
	if (time > Time_fea2 && time <= Time_fea3)
		return 2;
	if(time > Time_fea3 && time <= Time_fea4)
		return 3;
	if(time > Time_fea4)
		return 4;
}

int Count_ItmeNum_EachTime(vector<feature_timestemp_asist>& FeaAsist)
{
	for (int i=0; i!=FeaAsist.size(); i++)
	{
		int temp = 0;
		for (int j=0;j!=4;j++)
			temp += FeaAsist[i].type_count[j];
		if(temp!=0)
			FeaAsist[i].type_count[4] = 1;
	}
	return 0;
}

int Enrich_features(int iid, feature_space& features, map<int, Item_Pop_global>& Item_Pop)
{
	for (int i=0; i!=5 ; i++)
	{
		if ( features.feature[i*Each_TimeStemp_FeaNum + 1]!=0 )
			features.feature[i*Each_TimeStemp_FeaNum + 5] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[i*Each_TimeStemp_FeaNum + 1];
		if(features.feature[i*Each_TimeStemp_FeaNum + 3]!=0)
		    features.feature[i*Each_TimeStemp_FeaNum + 6] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[i*Each_TimeStemp_FeaNum + 3];
		if(features.feature[i*Each_TimeStemp_FeaNum + 4]!=0)
		    features.feature[i*Each_TimeStemp_FeaNum + 7] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[i*Each_TimeStemp_FeaNum + 4];
	}
	for (int i=0; i!=4; i++)
	{
		if (features.feature[(i+1)*Each_TimeStemp_FeaNum + 1]!=0)
			features.feature[i*Each_TimeStemp_FeaNum + 17] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[(i+1)*Each_TimeStemp_FeaNum + 1];
		if(features.feature[(i+1)*Each_TimeStemp_FeaNum + 3]!=0)
			features.feature[i*Each_TimeStemp_FeaNum + 18] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[(i+1)*Each_TimeStemp_FeaNum + 3];
		if(features.feature[(i+1)*Each_TimeStemp_FeaNum + 4]!=0)
			features.feature[i*Each_TimeStemp_FeaNum + 19] = features.feature[i*Each_TimeStemp_FeaNum + 2] / features.feature[(i+1)*Each_TimeStemp_FeaNum + 4];
	}

	map<int, Item_Pop_global>::iterator it = Item_Pop.find(iid);
	if(it==Item_Pop.end())
	{
		cout<<"error"<<endl;
		system("pause");
	}

	for (int i=0;i!=4;i++)
	{
		features.feature[0*Each_TimeStemp_FeaNum + 13 + i] = it->second.time1[i];
		features.feature[1*Each_TimeStemp_FeaNum + 13 + i] = it->second.time2[i];
		features.feature[2*Each_TimeStemp_FeaNum + 13 + i] = it->second.time3[i];
		features.feature[3*Each_TimeStemp_FeaNum + 13 + i] = it->second.time4[i];
		features.feature[4*Each_TimeStemp_FeaNum + 13 + i] = it->second.time5[i];
	}
	return 0;
}

int Generate_Feature(map<int, log_type>& RawLog_train, map<UID_IID_Pair, int>& GroundTruth, map<int, Item_Pop_global>& Item_Pop, map<UID_IID_Pair, feature_space>& features)
{
	for (map<int, log_type>::iterator it = RawLog_train.begin(); it!=RawLog_train.end(); it++) // ±éÀúËùÓÐÓÃ»§
	{
		int uid = it->first;
		log_type logs = it->second;

		vector<feature_timestemp_asist> Fea_count; /// ¼ÇÂ¼¸ÃÓÃ»§ËùÓÐÊ±¼ä¶Î½×¶Î¶ÔÓ¦µÄ²Ù×÷×ÜÊý
		for (int i=0; i!=5; i++)
		{
			feature_timestemp_asist Ftemp;
			for (int j=0;j!=5;j++) //×îºóÒ»¸öÎ¬¶ÈÊÇÍ³¼Æ¸Ã½×¶ÎÊÇ·ñÓÐitem
				Ftemp.type_count.push_back(0);
			Fea_count.push_back(Ftemp);
		}

		map<int,vector<feature_timestemp_asist> > IID_Count;//¼ÇÂ¼¸ÃÓÃ»§µÄÒ»¸öÆ·ÅÆµÄ²Ù×÷ÐÐÎª¼ÇÂ¼£¬·Ö¸÷½×¶Î

		map<int, feature_space> FeatureStore;// ´æ´¢Ã¿¸öiidµÄÌØÕ÷£¬µ«ÊÇÈ±ÉÙself pop;

		for (log_type::iterator it2 = logs.begin();it2!=logs.end();it2++) //±éÀú¸ÃÓÃ»§¶ÔÓ¦µÄËùÓÐÆ·ÅÆ¼ÇÂ¼
		{
			int iid = it2->first;
			int truth = 0;
			vector<Type_Days> Tdays = it2->second;

			feature_space feature_temp; //Îª¸Ã×épair¶¨ÒåÒ»¸öÌØÕ÷¿Õ¼ä
			Init_FeaSpa(feature_temp);

			vector<feature_timestemp_asist> FeaAsist; //¼ÇÂ¼¸ÃÆ·ÅÆÔÚ¸ÃÓÃ»§µÄ5¸öÊ±¼ä¶ÎµÄÐÐÎª
			for (int i=0; i!=5; i++)
			{
				feature_timestemp_asist Ftemp;
				for (int j=0;j!=5;j++) //×îºóÒ»¸öÎ¬¶ÈÊÇÍ³¼Æ¸Ã½×¶ÎÊÇ·ñÓÐitem
					Ftemp.type_count.push_back(0);
				FeaAsist.push_back(Ftemp);
			}
			int flag = 0; //ÓÃÓÚÍ³¼Æ¸ÃÆ·ÅÆÊÇ·ñ¼ÇÂ¼¹ýÁË¡£¼´¼ÆËãµÚ12ÎªÌØÕ÷µÄÊ±ºòÓÃµÄ¡£

			///
			UID_IID_Pair Pari_Candidate = make_pair(uid,iid); //ÕÒµ½¸Ã×épairµÄground truth
			map<UID_IID_Pair, int>::iterator it_truth = GroundTruth.find(Pari_Candidate);
			if(it_truth != GroundTruth.end() && it_truth->first.second == iid)
			{
				truth = it_truth->second;
				Plus_example++;
			}
			feature_temp.GroundTruth = truth;
			///

			for (int i=0; i!=Tdays.size(); i++) // ±éÀú¸ÃÆ·ÅÆµÄËùÓÐLog
			{
				int type = Tdays[i].type;
				int days = Tdays[i].days;

				int TimeFactor = Fea_Time_Area(94-days);//Çø·ÖÊ±¼ä¶Î
				int TimeStemp = TimeFactor * Each_TimeStemp_FeaNum;

				feature_temp.feature[1 + TimeStemp + type]++; //ÏàÓ¦Ê±¼ä¶ÎµÄÏàÓ¦²Ù×÷ÀàÐÍ+1£»

				((FeaAsist[TimeFactor]).type_count)[type]++; //Í³¼Æ³ö¸ÃÓÃ»§¶Ô¸ÃÆ·ÅÆµÄ¸÷¸ö²Ù×÷µÄÊýÁ¿£¬·Ö½×¶ÎµÄ¡£
				((Fea_count[TimeFactor]).type_count)[type]++; //Í³¼Æ³ö¸ÃÓÃ»§¶Ô¶àÓÐÆ·ÅÆµÄ¸÷¸ö²Ù×÷µÄÊýÁ¿£¬·Ö½×¶ÎµÄ¡£
				if(flag == 0)
				{
					((Fea_count[TimeFactor]).type_count)[4]++;
					flag = 1;
				}
			}

			Enrich_features(iid, feature_temp, Item_Pop);
			FeatureStore[iid] = feature_temp;
			//features[make_pair(uid,iid)] = feature_temp;

			//Count_ItmeNum_EachTime(FeaAsist);
			IID_Count[iid] = FeaAsist;
		}

		for (map<int,vector<feature_timestemp_asist> >::iterator it_fea = IID_Count.begin();it_fea!=IID_Count.end();it_fea++)
		{
			int iid_index = it_fea->first;
			//vector<feature_timestemp_asist> count_data = it_fea->second;
			for (int ii=0; ii!=5; ii++)
			{
				for (int jj=0;jj!=4;jj++)
				{
					if(Fea_count[ii].type_count[jj]!=0)
						it_fea->second[ii].type_count[jj] = it_fea->second[ii].type_count[jj] / Fea_count[ii].type_count[jj];
				}
				it_fea->second[ii].type_count[4] = Fea_count[ii].type_count[4];
			}
		}
		for (map<int, feature_space>::iterator it_fea = FeatureStore.begin();it_fea!=FeatureStore.end();it_fea++)
		{
			int iid_index = it_fea->first;
			map<int,vector<feature_timestemp_asist> >::iterator it_temp = IID_Count.find(iid_index);
			vector<feature_timestemp_asist> count_data = it_temp->second;
			for (int ii=0;ii!=5;ii++)
			{
				it_fea->second.feature[ii*Each_TimeStemp_FeaNum + 8] = count_data[ii].type_count[0];
				it_fea->second.feature[ii*Each_TimeStemp_FeaNum + 9] = count_data[ii].type_count[1];
				it_fea->second.feature[ii*Each_TimeStemp_FeaNum + 10] = count_data[ii].type_count[2];
				it_fea->second.feature[ii*Each_TimeStemp_FeaNum + 11] = count_data[ii].type_count[3];
				it_fea->second.feature[ii*Each_TimeStemp_FeaNum + 12] = count_data[ii].type_count[4];
			}
			features[make_pair(uid,iid_index)] = it_fea->second;
		}
	}
	return 0;
}

int Generate_Random(vector<int>& a, int start, int end, int num)
{
	for (int i=0; i!=num; i++)
	{
		a.push_back( (rand() % (end-start+1))+start + rand() % 23 + rand() % 121);
	}
	int chong = 0;
	do
	{
		chong = 0;
		sort(a.begin(),a.end(),compareSTB);
		for (int i =1; i!=a.size(); i++)
		{
			if(a[i] == a[i-1])
			{
				chong++;
				a[i] += rand() % 31;
			}
		}
	} while (chong != 0);

	cout<<chong<<endl;
	return 0;
}

void solve()
{
	map<int, log_type> RawLog;
	ReadLog_UIDindex(LogFile,RawLog);
	map<int, log_type> RawLog_123, RawLog_4,  RawLog_234;
	ConstructSets(RawLog,RawLog_123, RawLog_4, RawLog_234);

	map<int, log_type> RawLog_iid;
	ReadLog_UIDindex(LogFile_IIDindex,RawLog_iid);
	map<int, log_type> RawLog_123_iid, RawLog_4_iid,  RawLog_234_iid;
	ConstructSets(RawLog,RawLog_123_iid, RawLog_4_iid, RawLog_234_iid);

	map<int, Item_Pop_global> Item_Pop;
	map<UID_IID_Pair, int> GroundTruth;
	GetItemPopGlobal_GroundTruth(RawLog_iid, Item_Pop, GroundTruth);

	//ofstream outtest("GroundTruth.txt");
	//for (map<UID_IID_Pair, int>::iterator it=GroundTruth.begin();it!=GroundTruth.end();it++)
	//{
	//	outtest<<it->first.first<<","<<it->first.second<<'\t'<<it->second<<endl;
	//}
	//outtest.close();

	//map<UID_IID_Pair, feature_space> features;
	//Generate_Feature(RawLog_123, GroundTruth, Item_Pop, features);

	//ofstream out_fea("features_vaculization.txt");
	//int line = 0;
	//map<UID_IID_Pair, feature_space> feature_plus;
	//map<UID_IID_Pair, feature_space> feature_minus;
	//map<UID_IID_Pair, feature_space> features_final_train;
	//for (map<UID_IID_Pair, feature_space>::iterator it = features.begin();it!=features.end();it++)
	//{
	//	line++;
	//	if(line % 10000 == 0)
	//		cout<<line<<"out of"<<features.size()<<endl;

	//	if (it->second.GroundTruth > 0)
	//	{
	//		feature_plus[it->first] = it->second;
	//		features_final_train[it->first] = it->second;
	//	}

	//	if (it->second.GroundTruth < 0.00000001)
	//		feature_minus[it->first] = it->second;

	//	out_fea<<setprecision(6)<< setiosflags(ios::fixed | ios::showpoint)<<it->second.GroundTruth<<'\t'<<it->first.first<<","<<it->first.second<<'\t';
	//	for (int i=0; i!=FeaNum; i++)
	//	{
	//		out_fea<<i<<": "<<it->second.feature[i]<<"\t";
	//	}
	//	out_fea<<endl;
	//}
	//out_fea.close();

	////ofstream out_fea_plus("features_plus_use.txt");
	////line = 0;
	////for (map<UID_IID_Pair, feature_space>::iterator it = feature_plus.begin();it!=feature_plus.end();it++)
	////{
	////	line++;
	////	if(line % 10000 == 0)
	////		cout<<line<<"out of"<<feature_plus.size()<<endl;

	////	out_fea_plus<<setprecision(6)<< setiosflags(ios::fixed | ios::showpoint)
	////		<<it->second.GroundTruth<<'\t';
	////	for (int i=0; i!=FeaNum; i++)
	////	{
	////		out_fea_plus<<it->second.feature[i]<<"\t";
	////	}
	////	out_fea_plus<<endl;
	////}
	////out_fea_plus.close();

	////ofstream out_fea_minus("features_minus_use.txt");
	////line = 0;
	////for (map<UID_IID_Pair, feature_space>::iterator it = feature_minus.begin();it!=feature_minus.end();it++)
	////{
	////	line++;
	////	if(line % 10000 == 0)
	////		cout<<line<<"out of"<<feature_minus.size()<<endl;

	////	out_fea_minus<<setprecision(6)<< setiosflags(ios::fixed | ios::showpoint)
	////		<<it->second.GroundTruth<<'\t';
	////	for (int i=0; i!=FeaNum; i++)
	////	{
	////		out_fea_minus<<it->second.feature[i]<<"\t";
	////	}
	////	out_fea_minus<<endl;
	////}
	////out_fea_minus.close();

	//vector<int> random_num;
	//Generate_Random(random_num,0,feature_minus.size(),Plus_example);

	//int line_minus = 0, flag_random = 0;
	//cout<<features_final_train.size()<<endl;
	//for (map<UID_IID_Pair, feature_space>::iterator it = feature_minus.begin(); it != feature_minus.end() && flag_random!=Plus_example ;it++)
	//{
	//	line_minus++;
	//	if(line_minus == random_num[flag_random])
	//	{
	//		//cout<<flag_random<<endl;
	//		flag_random++;
	//		features_final_train[it->first] = it->second;
	//	}
	//}
	//cout<<"minus example num"<<features_final_train.size()<<endl;

	//ofstream out_fea_final("features_final_train.txt");
	//line = 0;
	//for (map<UID_IID_Pair, feature_space>::iterator it = features_final_train.begin();it!=features_final_train.end();it++)
	//{
	//	line++;
	//	if(line % 10000 == 0)
	//		cout<<line<<"out of"<<features_final_train.size()<<endl;

	//	out_fea_final<<setprecision(6)<< setiosflags(ios::fixed | ios::showpoint)
	//		<<it->second.GroundTruth<<" ";
	//	for (int i=0; i!=FeaNum; i++)
	//	{
	//		out_fea_final<<it->second.feature[i]<<" ";
	//	}
	//	out_fea_final<<endl;
	//}
	//out_fea_final.close();

	map<int, Item_Pop_global> Item_Pop234;
	map<UID_IID_Pair, int> GroundTruth_temp;
	GetItemPopGlobal_GroundTruth_final234(RawLog_iid, Item_Pop234, GroundTruth_temp);

	map<UID_IID_Pair, feature_space> features234;
	Generate_Feature(RawLog_234, GroundTruth_temp, Item_Pop234, features234);

	ofstream out_fea_final("features_final_use.txt");
	ofstream out_fea_final_index("features_final_use_index.txt");
	int line = 0;
	for (map<UID_IID_Pair, feature_space>::iterator it = features234.begin();it!=features234.end();it++)
	{
		line++;
		if(line % 10000 == 0)
			cout<<line<<"out of"<<features234.size()<<endl;

		out_fea_final<<setprecision(6)<< setiosflags(ios::fixed | ios::showpoint)
			<<it->second.GroundTruth<<'\t';
		out_fea_final_index<<it->first.first<<'\t'<<it->first.second<<endl;
		for (int i=0; i!=FeaNum; i++)
		{
			out_fea_final<<it->second.feature[i]<<"\t";
		}
		out_fea_final<<endl;
	}
	out_fea_final.close();
}

int main()
{
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int ln_t;
    scanf("%d", &ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        printf("Case #%d:\n", ln_cas);
        solve();
    }
    return 0;
}

