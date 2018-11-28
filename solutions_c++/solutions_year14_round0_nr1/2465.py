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
	c=getchar();
	if(c==' '||c=='\n')continue;
	else break;}
 if(c=='+'){}
 else if(c=='-')sign=-1;
 else res=c-'0';
 while(1){
	c=getchar();
	if(c>='0'&&c<='9')res=res*10+c-'0';
	else break;}
return res*sign;
}

/*end of template*/

int main(int argc , char** argv)
{		
	clock_t asd;
	//freopen("input.txt","r",stdin);
	freopen("a.out","w",stdout);
	int cnt[100];
	int tc=getnum<int>();
	for (int testcase=1; testcase<=tc; testcase++) {
		memset(cnt,0,sizeof(cnt));
		bool bisa=false,dobel=false;
		int ans;

		int n=getnum<int>();
		n--;				
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				int x=getnum<int>();				
				if (i==n) cnt[x]++;										
			}
		}

		n=getnum<int>();
		n--;				
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				int x=getnum<int>();				
				if (i==n) {
					cnt[x]++;
					if (cnt[x]==2) {
						if (bisa) dobel=true;
						else {
							bisa=true;
							ans=x;
						}
					}
				}				
			}
		}
		cout<<"Case #"<<testcase<<": ";
		if (!bisa) cout<<"Volunteer cheated!"<<'\n';
		else if (dobel)  cout<<"Bad magician!"<<'\n';
		else cout<<ans<<'\n';
	}
	return 0;
}