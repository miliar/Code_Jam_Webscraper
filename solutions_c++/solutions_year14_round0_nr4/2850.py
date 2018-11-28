#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	ifstream in_f;
	in_f.open("D-large.in");
	ofstream out_f;
	out_f.open("D-large.out",ios::out);
	long long T,N;
	vector<long double> Naomi,Ken,Ken2,Naomi2;
	vector<long long> index_Kenmin;
	vector<long long> index_Kenmax;
	in_f>>T;
	for(long long CC=1;CC<=T;CC++)
	{
		index_Kenmin.clear();
		index_Kenmax.clear();
		Naomi.clear();
		Ken.clear();
		Ken2.clear();
		Naomi2.clear();
		long double max_Naomi=0,min_Naomi=100,min_Ken=100;
		long long y=0,z=0;	//y is the number of points Naomi will score if she plays Deceitful War optimally,
						//and z is the number of points Naomi will score if she plays War optimally.
		in_f>>N;
		for(long long i=0;i<N;i++)
		{
			long double temp;
			in_f>>temp;
			Naomi.push_back(temp);
			if(Naomi[i]>max_Naomi)
				max_Naomi=Naomi[i];
			if(Naomi[i]<min_Naomi)
				min_Naomi=Naomi[i];
			Naomi2.push_back(temp);
		}
		for(long long i=0;i<N;i++)
		{
			long double temp;
			in_f>>temp;
			Ken.push_back(temp);
			if(Ken[i]>max_Naomi)
				index_Kenmax.push_back(i);
			else if(Ken[i]<min_Naomi)
				index_Kenmin.push_back(i);
			if(Ken[i]<min_Ken)
				min_Ken=Ken[i];
			Ken2.push_back(temp);
		}
		if(index_Kenmax.size()==N)
			out_f<<"Case #"<<CC<<": 0 0"<<endl;
		else if(index_Kenmin.size()==N)
		{
			out_f<<"Case #"<<CC<<": "<<N<<" "<<N<<endl;
		}
		else
		{
			sort(Naomi.begin(),Naomi.end());
			sort(Ken.begin(),Ken.end());
			sort(Ken2.begin(),Ken2.end());
			sort(Naomi2.begin(),Naomi2.end());
			vector<long double>::iterator it1;
			vector<long double>::iterator it2;

			/*for(it1=Naomi.begin();it1!=Naomi.end();it1++)
			{
				if((*it1)<min_Ken)
					y++;
				else
					break;
			}*/
			it1=Naomi2.begin(),it2=Ken2.begin();
			while((it1!=Naomi2.end()&&it2!=Ken2.end()))
			{
				if(*it2>*it1)
				{
					Naomi2.erase(Naomi2.begin());
					Ken2.erase(Ken2.end()-1);
					it1=Naomi2.begin(),it2=Ken2.begin();
				}
				else
				{
					it1++;
					it2++;
				}
			}

			for(it1=Naomi.begin();it1!=Naomi.end();it1++)
			{
				long long temp_z=z;
				
				for(it2=Ken.begin();it2!=Ken.end();)
				{
					if((*it2)>(*it1))
					{
						Ken.erase(it2);
						z++;
						break;
					}
					else 
						it2++;
				}
				if(temp_z==z)
					Ken.erase(Ken.begin());

			}
			z=N-z;
			/*if(y>=index_Kenmax.size())
				y=N-y;
			else
				y=N-index_Kenmax.size();
			*/
			y=Ken2.size();
			out_f<<"Case #"<<CC<<": "<<y<<" "<<z<<endl;

		}

	}

	return 0;
}