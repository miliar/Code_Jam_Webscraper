#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back

using namespace std;

using ll = long long;

int read(){
	int i;
	scanf("%d",&i);
	return i;
}

char str[20001];
int n;

void Input(){
	scanf("%s",str);
	n=strlen(str);
}

typedef pair<int,char> pic;

void Solve(){
	set<pic> s;
	REP(i,n)
		s.insert(MP(i,str[i]));
	auto itr=s.begin();
	int ans=0;
	while(1){
		if(itr==s.end())
			break;
		char a=itr->second;
		if(++itr==s.end())
			break;
		char b=itr->second;
		if(a==b){
			ans+=10;
			n-=2;
			itr=s.erase(--itr);
			itr=s.erase(itr);
			if(itr!=s.begin())
				itr--;
		}
	}
	ans+=n/2*5;
	printf("%d\n",ans);
}

int main(){
	int t=read();
	REP(caseNumber,t){
		Input();
		printf("Case #%d: ",caseNumber+1);
		Solve();
	}
}