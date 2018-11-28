#include<iostream>
#include<iomanip>
#include<sstream>
#include<vector>
#include<map>

using namespace std;

void output(map<char, int>* record){
	int max=0;
	vector <int> max_pos;
	int valid_num;

	for (map<char, int>::iterator it=(*record).begin(); it!=(*record).end(); ++it){
		if(it->second>0){
			++valid_num;

			if(it->second > max){
				max=it->second;
			}
		}
	}

	for (map<char, int>::iterator it=(*record).begin(); it!=(*record).end(); ++it){
		if(it->second==max){
			max_pos.push_back(it->first-'A');
		}
	}

	if(max==0){
		cout<<endl;
		return;
	}if(max==1){
		//cout<<"valid num:"<<valid_num<<endl;
		while(valid_num>2){
			for (map<char, int>::iterator it=(*record).begin(); it!=(*record).end(); ++it){
				if(it->second > 0){
					cout<<it->first<<" ";
					--(*record)[it->first];
					break;
				}
			}
			--valid_num;
		}

		//cout<<"valid num:"<<valid_num<<endl;
		for (map<char, int>::iterator it=(*record).begin(); it!=(*record).end(); ++it){
						if(it->second > 0){
							cout<<it->first;
						}
		}

		cout<<endl;
		return;
	}

	//else max>=2
	if(max_pos.size()>1){
		char c1='A'+max_pos[0];
		char c2='A'+max_pos[1];
		cout<<c1<<c2<<" ";
		--(*record)['A'+max_pos[0]];
		--(*record)['A'+max_pos[1]];
		output(record);
	}else{//max_pos.size==1
		char c='A'+max_pos[0];
		cout<<c<<c<<" ";
		--(*record)['A'+max_pos[0]];
		--(*record)['A'+max_pos[0]];
		output(record);
	}


}


int main(){
	int total;
	cin>>total;

	map <char, int> record;

	record['A']=0;
	record['B']=0;
	record['C']=0;
	record['D']=0;
	record['E']=0;
	record['F']=0;
	record['G']=0;
	record['H']=0;
	record['I']=0;
	record['J']=0;
	record['K']=0;
	record['L']=0;
	record['M']=0;
	record['N']=0;
	record['O']=0;
	record['P']=0;
	record['Q']=0;
	record['R']=0;
	record['S']=0;
	record['T']=0;
	record['U']=0;
	record['V']=0;
	record['W']=0;
	record['X']=0;
	record['Y']=0;
	record['Z']=0;

	int case_num=1;
	int total_party;
	int reg;

	for(int j=0; j<total; ++j){
		cin>>total_party;

		for(int i=0; i<total_party; ++i){
			cin>>reg;
			record['A'+i]=reg;
		}

		cout<<"Case #"<<case_num<<": ";
		output(&record);
		++case_num;

		for (map<char, int>::iterator it=record.begin(); it!=record.end(); ++it){
			record[it->first]=0;
		}
	}


}
