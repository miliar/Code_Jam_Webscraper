#include<bits/stdc++.h>
#define MAXN 100009
#define INF 1000000007
#define imx 2147483647
#define LLINF 1000000000000000007
#define mp(x,y) make_pair(x,y)
#define wr cout<<"Continue Debugging!!!"<<endl;
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
#define ppb() pop_back()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
typedef pair<int,int>PII;
template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
deque<char>d,f,nw,dd,ff;
char s[MAXN];
int cmp(){
	dd=d,ff=f;
	string zz,xx;
	while(!d.empty()){
		zz+=d.front();
		d.pop_front();
	}
	while(!f.empty()){
		xx+=f.front();
		f.pop_front();
	}
	d=dd;f=ff;
	if(zz<=xx)
		return 2;
	return 1;	
}
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		d=nw;f=nw;
		scanf("%s",s);
		int n=strlen(s);
		for(int i=0;i<n;i++){
			d.push_front(s[i]);
			f.push_back(s[i]);
			if(cmp()==1){
				f.pop_back();
				f.push_front(s[i]);
			}
			else{
				d.pop_front();
				d.push_back(s[i]);
			}
		}
		printf("Case #%d: ",test);
		while(!d.empty()){
			printf("%c",d.front());
			d.pop_front();
		}
		printf("\n");
	}
	return 0;
}
/*
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
*/
