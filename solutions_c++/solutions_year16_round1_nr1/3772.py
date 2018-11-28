//============================================================================
// Author      : Prateek Agarwal
// Institution : NITJ
//============================================================================

#include <bits/stdc++.h>

#define ll long long

#define TEST int t;scan(t);while(t--)
#define scan(n) scanf("%d",&n)
#define scanl(n) scanf("%lld",&n)
#define set(x,y) memset(x,y,sizeof(x))
#define loop(i,l,r,x) for (int i=l;i<=r;i+=x)
#define printl(n) printf("%d\n",n)
#define print(n) printf("%d ",n)
#define pb push_back

#define INF 1000000000
#define M 1000000007
#define MAX 100000000
#define LIM 10

using namespace std;

ifstream inf("test.txt");
ofstream of("out.txt");


int init(){
	int cs = 1;
	int t;
	inf>>t;
	while(t--){
		of << "Case " << "#" << cs++ << ": ";
		char s[1234];
		char x[10000];
		int st=1001,en=1001;
		inf>>s;
		int l = strlen(s);
		x[st] = s[0];
		for (int i=1;i<l;i++){
			if (s[i]>=x[st]){
				st--;
				x[st] = s[i];
			}
			else{
				en++;
				x[en] = s[i];
			}
		}
		for (int i=st;i<=en;i++) of << x[i];
		of << endl;
	}
	return 0;
}

int main(){
	//clock_t start = clock();
	init();
	//printf("%.6f\n",double(clock()-start)/CLOCKS_PER_SEC);
	return 0;
}

