#include<cstdio>
#include<cstring>
#include<vector>
#include<deque>
#include<algorithm>
#define CL(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(e);i++)
#define x first
#define y second
#define MAX 1005
#define INF 1<<29

using namespace std;

int T,TC,N;
char s[MAX];
deque<char> v;

int main(){
	scanf("%d",&T);
	while (T--){
		v.clear();
		scanf("%s",s);
		v.pb(s[0]);
		for (int i=1,len=strlen(s);i<len;i++){
			if (s[i]>=v[0]) v.push_front(s[i]);
			else v.pb(s[i]);
		}
		printf("Case #%d: ",++TC);
		for (int i=0,len=v.size();i<len;i++){
			printf("%c",v[i]);
		}
		
		puts("");
	}
}
