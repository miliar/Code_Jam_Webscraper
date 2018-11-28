#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cstring>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

using namespace std;


int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: ",casenr);
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double res = X/2.;
		FOR(i,1,X+5){
			double res2 = res+C/((i-1)*F+2.)-X/((i-1.)*F+2.) + X/(i*F+2.);
			if(res2<res) res=res2;
			else break;
		}
		printf("%.7lf\n",res);
	}
	return 0;
}
  

