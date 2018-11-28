#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <queue>
#include <map>
using namespace std;
int n,t,a,b,result,skill,pom,team_size;
bool con;
int tab[26];
bool use[26],use_teams[26];
int teams_size[26];
int skill_size[26];
string temp;
vector<pair<int,int>> teams;
int number_teams;
int compute(int emp,int poz,int cos){
	int best_res=100000;
	if(emp>=number_teams)
		return 0;
	if(use_teams[poz]==true){
		if(poz==emp){
			return compute(emp+1,poz+1,cos);
		}else
			return compute(emp,poz+1,cos);
		//cout<<"wrong"<<endl;
	}
		
	if(emp==poz){
		use_teams[emp]=true;
		skill_size[emp]=teams[emp].first;
		teams_size[emp]=teams[emp].second;
	}
	if(skill_size[emp]==teams_size[emp]){
		int res=compute(emp+1,emp+1,cos)+teams_size[emp]*teams_size[emp];
		if(res<best_res)
			best_res=res;
	}else{
		if((skill_size[emp]<teams_size[emp]) && skill_size[emp]+cos>=teams_size[emp]){
			int res=compute(emp+1,emp+1,cos-teams_size[emp]+skill_size[emp])+teams_size[emp]*teams_size[emp];
			if(res<best_res)
				best_res=res;
		}
		for(int i=poz;i<number_teams;i++){
			if(!use_teams[i]){
				skill_size[emp]+=teams[i].first;
				teams_size[emp]+=teams[i].second;
				use_teams[i]=true;
				int res=compute(emp,i+1,cos);
				use_teams[i]=false;
				if(res<best_res)
					best_res=res;
				skill_size[emp]-=teams[i].first;
				teams_size[emp]-=teams[i].second;
				compute(emp,i+1,cos);
				if(res<best_res)
					best_res=res;
			}
		}
	}
		
	if(emp==poz)
		use_teams[emp]=false;
	return best_res;
}

int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin>>t;
	for(int test_nr=1;test_nr<=t;test_nr++){
		std::cin>>n;
		teams.clear();
		number_teams=0;
		result=0;
		int ncos=0;
		for(int i=0;i<n;i++){
			cin>>temp;
			pom=0;
			for(int j=0;j<n;j++){
				use[j]=false;
				pom*=2;
				result-=(temp[j]=='1');
				pom+=(temp[j]=='1');
			}
			ncos|=pom;
			tab[i]=pom;
		}
		for(int i=0;i<n;i++){
			if(use[i])
				continue;
			skill=tab[i];
			team_size=1;
			use[i]=true;
			do{
				//cout<<"x"<<endl;
				con=false;
				for(int j=0;j<n;j++){
					if(skill & tab[j]){
						if(!use[j]){
							con=true;
							skill|=tab[j];
							use[j]=true;
							team_size++;
						}
					}
				}
			}while (con);
			//teams[number_teams][0]=team_size;
			//teams[number_teams][1]=__builtin_popcount(skill);
			number_teams++;
			//cout<<team_size<<" "<<__builtin_popcount(skill)<<endl;
			teams.push_back(make_pair(__builtin_popcount(skill),team_size));
		}
		sort(teams.begin(),teams.end(),std::greater<pair<int,int>>());
		//cout<<teams[0].first<<" "<<teams[0].second<<endl;
		int res2=compute(0,0,n-__builtin_popcount(ncos));
		cout<<"Case #"<<test_nr<<": "<<res2+result<<endl;
		//cout<<i;
		
		
	}
}
