#include <bits/stdc++.h>
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
int n;
char s[MAXN],t[MAXN];
int calc(){
	for(int i=1;i<=n;i++)
		if(s[i]=='-')
			return 0;
	return 1;		
}
void rotate(int x,int y){
	for(int i=x;i<=y;i++)
		t[i]=(s[i]=='+'?'-':'+');
	for(int i=x;i<=y;i++)
		s[i]=t[y-i+1];	
}
void radius(){
	for(int i=1;i<=n;i++){
		if(s[i]=='-')
			break;
		s[i]='-';	
	}
}
int main(){
	freopen("codeJam.in", "r", stdin);
	freopen("codeJam.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%s",s+1);
		n=strlen(s+1);
		int ans=0,pnt=n;
		while(1){
			if(calc())
				break;
			while(pnt>0 and s[pnt]=='+')	
				pnt--;
			if(!pnt)
				break;
			if(s[1]=='-')
				rotate(1,pnt);
			else
				radius();		
			ans++;	
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}

