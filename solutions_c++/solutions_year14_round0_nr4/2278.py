/*template by : Dewangga Winardi*/
#include <bits/stdc++.h>

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)	
#define mp make_pair
#define fi first
#define sc second
#define ll long long
#define pb push_back
#define RESET(v,a) memset(v,a,sizeof(v))	
#define pause system("pause")
#define INF 1000000000
#define INFL 1000000000LL
#define debug_time1 time_start(&asd);
#define debug_time2 print_time(asd);

using namespace std;

void time_start(clock_t *asd) {
	*asd=clock();
} 

void print_time(clock_t asd) {
	asd=clock()-asd;
	printf("waktu=%.fmilisecond\n", (float)asd/CLOCKS_PER_SEC*1000);
}

inline string GetString()
{
	char S[1000005];
	scanf("%s",S);
	string ret=S;
	return ret;
}

template<typename t>
t getnum()
{
 t res=0;
 char c;
 int sign=1;
 while(1){
	c=getchar_unlocked();
	if(c==' '||c=='\n')continue;
	else break;}
 if(c=='+'){}
 else if(c=='-')sign=-1;
 else res=c-'0';
 while(1){
	c=getchar_unlocked();
	if(c>='0'&&c<='9')res=res*10+c-'0';
	else break;}
return res*sign;
}

/*end of template*/

int main(int argc , char** argv)
{		
	clock_t asd;
	//freopen("input.txt","r",stdin);
	//freopen("d.out","w",stdout);
	int tc=getnum<int>();
	for (int t=1; t<=tc; t++) {
		int ans1=0,ans2=0;
		vector<double> nao,ken;
		double x;
		int n=getnum<int>();
		for (int i=0; i<n; i++) {
			scanf("%lf",&x);
			nao.pb(x);
		}
		for (int i=0; i<n; i++) {
			scanf("%lf",&x);
			ken.pb(x);
		}
		sort(nao.begin(),nao.end()),sort(ken.begin(),ken.end());

		int lili=0;
		for (int i=0; i<n; i++) {
			if (nao[i]<ken[lili]) lili++; else {
				while (lili<n && nao[i]>=ken[lili]) {
					lili++,ans2++;
				}
				lili++;
			}					
		}

		while (nao.size()>0) {
			int lala=nao.size()-1;
			while (nao[lala]>ken[lala]) {
				ans1++;
				nao.erase(nao.begin()+nao.size()-1);
				ken.erase(ken.begin()+ken.size()-1);	
				lala=nao.size()-1;
				if (lala==-1) break;			
			}			
			if (nao.size()==0) break;
			nao.erase(nao.begin());			
			ken.erase(ken.begin()+ken.size()-1);	
		}

		printf("Case #%d: %d %d\n",t,ans1,ans2);
	}
	return 0;
}