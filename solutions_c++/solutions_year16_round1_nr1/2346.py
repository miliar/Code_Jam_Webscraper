#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define frd(i,a,b) for(int i = a; i > b; i--)
#define fred(i,a,b) for(int i = a; i >= b; i--)
#define pb push_back
#define SET(a,v) memset(a,v,sizeof a)

#define INF 1e8
#define N 1010

typedef long long ll;
typedef pair<int,int> ii;

char word[N];
int t,len;
vector<char> ans;
char first,last;

void solve(){
		ans.clear();
		ans.pb(word[0]);
		first = last = word[0];
		fr(i,1,len){ 
			if (word[i] >= first){
				ans.insert(ans.begin(),word[i]);
				first = word[i];
			}
			else ans.pb(word[i]);
		}
		fr(i,0,len)	printf("%c",ans[i]);
		puts("");
}

int main(){
	scanf("%d",&t);
	fr(t2,0,t){
		printf("Case #%d: ",t2+1);
		scanf("%s",word);
		len = strlen(word);

		
		solve();		
	}

	return 0;
}