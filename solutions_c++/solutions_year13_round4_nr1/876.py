#include<cstdio>
#include<vector>
#include<cstring>

using namespace std;
#define MX 1001001
#define MOD 1000002013

int N,M;
vector<pair<int,int> > S;
int P[MX];

long long price(int zac,int kon,int poc){
	long long vys=kon-zac;
	if (vys){
		vys=(vys*N - vys*(vys-1)/2) % MOD;
	}
	return vys*poc % MOD;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: ",t);
		memset(P,0,sizeof P);
		S.clear();
		S.push_back(make_pair(0,0));
		scanf("%d%d",&N,&M);
		long long cena=0,cena2=0;
		for(int i=0;i<M;++i){
			int x,y,p;
			scanf("%d%d%d",&x,&y,&p);
			P[x]+=p;
			P[y]-=p;
			cena=(cena+price(x,y,p))%MOD;
		}
		for(int i=1;i<=N;++i){
			if (P[i]>0){
				S.push_back(make_pair(i,P[i]));
			}
			else if (P[i]<0){
				int zac=S.back().first;
				int p=S.back().second;
				while(P[i]<0&&p<=-P[i]){
					S.pop_back();
					cena2=(cena2+price(zac,i,p))%MOD;
					P[i]+=p;
					zac=S.back().first;
					p=S.back().second;
				}
				if (P[i]<0){
					cena2=(cena2+price(zac,i,-P[i]))%MOD;
					p+=P[i];
					P[i]=0;
					S.pop_back();
					S.push_back(make_pair(zac,p));
				}
			}
		}
		int vys=(cena+MOD-cena2)%MOD;
		printf("%d\n",vys);
	}
	return 0;
}
