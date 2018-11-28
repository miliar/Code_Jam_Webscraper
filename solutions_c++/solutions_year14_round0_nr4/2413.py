#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
int main(){
	int T;
	//freopen("InputBalance.txt","r",stdin);
	//freopen("OutBalance.txt","w",stdout);
	cin>>T;
	for(int kasus=1;kasus<=T;kasus++){
		vector<double> Naomi,Ken;
		int N,NaomiScoreDeceit=0,NaomiScoreWar=0,KenScore=0,TotalScore=0;
		cin>>N;
		for(int i=0;i<N;i++){
			double temp;
			scanf("%lf",&temp);
			Naomi.push_back(temp);}
		for(int i=0;i<N;i++){
			double temp;
			scanf("%lf",&temp);
			Ken.push_back(temp);}
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		//DECEITFUL WAR
		int NaoLowest=0;
		int NaoHighest=Naomi.size()-1;
		int KenLowest=0;
		int KenHighest=Ken.size()-1;
		while(TotalScore!=N){
			//cout<<"Naomi Highest : "<<Naomi[NaoHighest]<<" , Ken Highest : "<<Ken[KenHighest]<<endl;
			//cout<<"Naomi Lowest : "<<Naomi[NaoLowest]<<" , Ken Lowest : "<<Ken[KenLowest]<<endl;
			if (Naomi[NaoHighest] > Ken[KenHighest]){
				NaomiScoreDeceit++;
				int OldLowest=NaoLowest;
				while(Naomi[NaoLowest]<Ken[KenLowest]) NaoLowest++;
				
				KenScore+=NaoLowest-OldLowest;
				KenLowest++;
				NaoLowest++;
			}
			else{
				KenScore++;
				KenHighest--;
				NaoLowest++;
			}
			TotalScore=KenScore+NaomiScoreDeceit;
		}
		//cout<<"TotalScore : "<<TotalScore<<endl;
		//WAR
		NaoLowest=0;
		NaoHighest=Naomi.size()-1;
		KenLowest=0;
		KenHighest=Ken.size()-1;
		TotalScore=0;
		KenScore=0;
		while(TotalScore!=N){
			//cout<<"Naomi Highest : "<<Naomi[NaoHighest]<<" , Ken Highest : "<<Ken[KenHighest]<<endl;
			//cout<<"Naomi Lowest : "<<Naomi[NaoLowest]<<" , Ken Lowest : "<<Ken[KenLowest]<<endl;
			if (Naomi[NaoLowest] < Ken[KenLowest]){
				KenScore++;
				KenLowest++;
				NaoLowest++;
			}
			else{
				int OldLowest=KenLowest;
				while(OldLowest<=KenHighest){
					if (Naomi[NaoLowest]<Ken[OldLowest])
						break;
					else OldLowest++;
				}
				if (OldLowest>KenHighest)
					NaomiScoreWar+=OldLowest-KenLowest;
				else{
					NaomiScoreWar+=OldLowest-KenLowest;
					KenLowest=OldLowest+1;
					NaoLowest++;
					KenScore++;
				}
			}
			TotalScore=NaomiScoreWar+KenScore;
		}		
		printf("Case #%d: %d %d\n",kasus,NaomiScoreDeceit,NaomiScoreWar);
	}
	return 0;}