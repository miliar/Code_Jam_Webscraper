#include<bits/stdc++.h>
using namespace std;

#define in(Kavya) scanf("%lld",&Kavya);

typedef long long int ll;

ll TC,T,i,j,N,R,P,S;

int main() {
	in(TC);
	for(T=1;T<=TC;++T) {
		in(N); in(R); in(P); in(S);
		string MainR="R",MainP="P",MainS="S",tmp="";
		for(i=0;i<N;++i) {
			tmp="";
			for(j=0;j<MainR.length();++j) {
				if(MainR[j]=='R') tmp+="SR";
				else if(MainR[j]=='P') tmp+="RP";
				else if(MainR[j]=='S') tmp+="SP";
			}
			MainR="";
			MainR+=tmp;
			tmp="";
			for(j=0;j<MainP.length();++j) {
				if(MainP[j]=='R') tmp+="SR";
				else if(MainP[j]=='P') tmp+="RP";
				else if(MainP[j]=='S') tmp+="SP";
			}
			MainP="";
			MainP+=tmp;
			tmp="";
			for(j=0;j<MainS.length();++j) {
				if(MainS[j]=='R') tmp+="SR";
				else if(MainS[j]=='P') tmp+="RP";
				else if(MainS[j]=='S') tmp+="SP";
			}
			MainS="";
			MainS+=tmp;
		}
		printf("Case #%lld: ",T);
		ll RCount=0,PCount=0,SCount=0;
		for(j=0;j<MainS.length();++j) {
			if(MainS[j]=='R') ++RCount;
			else if(MainS[j]=='P') ++PCount;
			else if(MainS[j]=='S') ++SCount;
		}
		if(R==RCount && P==PCount && S==SCount) {
			for(i=0;i<MainS.length();i+=2) {
				if(MainS[i]=='S' && MainS[i+1]=='R') swap(MainS[i],MainS[i+1]);
				else if(MainS[i]=='R' && MainS[i+1]=='P') swap(MainS[i],MainS[i+1]);
				else if(MainS[i]=='S' && MainS[i+1]=='P') swap(MainS[i],MainS[i+1]);
			}
			cout << MainS << endl;
			continue;
		}
		RCount=0; PCount=0; SCount=0;
		for(j=0;j<MainP.length();++j) {
			if(MainP[j]=='R') ++RCount;
			else if(MainP[j]=='P') ++PCount;
			else if(MainP[j]=='S') ++SCount;
		}
		if(R==RCount && P==PCount && S==SCount) {
			for(i=0;i<MainP.length();i+=2) {
				if(MainP[i]=='S' && MainP[i+1]=='R') swap(MainP[i],MainP[i+1]);
				else if(MainP[i]=='R' && MainP[i+1]=='P') swap(MainP[i],MainP[i+1]);
				else if(MainP[i]=='S' && MainP[i+1]=='P') swap(MainR[i],MainR[i+1]);
			}
			cout << MainP << endl;
			continue;
		}
		RCount=0; PCount=0; SCount=0;
		for(j=0;j<MainR.length();++j) {
			if(MainR[j]=='R') ++RCount;
			else if(MainR[j]=='P') ++PCount;
			else if(MainR[j]=='S') ++SCount;
		}
		if(R==RCount && P==PCount && S==SCount) {
			for(i=0;i<MainR.length();i+=2) {
				if(MainR[i]=='S' && MainR[i+1]=='R') swap(MainR[i],MainR[i+1]);
				else if(MainR[i]=='R' && MainR[i+1]=='P') swap(MainR[i],MainR[i+1]);
				else if(MainR[i]=='S' && MainR[i+1]=='P') swap(MainR[i],MainR[i+1]);
			}
			cout << MainR << endl;
			continue;
		}
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
