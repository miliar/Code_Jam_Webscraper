#include <stdio.h>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int maxd,cnt;
int n,m;
string s[10];
int a[10];

void input()
{
	scanf("%d %d",&m,&n);
	for(int i=1; i<=m; i++) cin>>s[i];
}

int get_cnt()
{
	map<string,bool> mp[5];
	int tmp=0;
	for(int i=1; i<=m; i++) {
		for(int j=0; j<s[i].size(); j++) {
			tmp+=!(mp[a[i]][s[i].substr(0,j+1)]);
			mp[a[i]][s[i].substr(0,j+1)]=true;
		}
	}
	return tmp+n;
}

void process(int x)
{
	if(x>m) {
		int tmp=0;
		for(int i=1; i<=m; i++) tmp|=(1<<(a[i]-1));
		if(tmp!=(1<<n)-1) return;
		tmp=get_cnt();
		if(tmp>maxd) {
			maxd=tmp;
			cnt=1;
		}
		else if(tmp==maxd) cnt++;
		return;
	}

	for(int i=1; i<=n; i++) {
		a[x]=i;
		process(x+1);
	}
}

int main()
{
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("D-small-attempt0.out","wt",stdout);
	int t,i;
	scanf("%d",&t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d: ",i); 
		maxd=cnt=0;
		input();
		process(1);
		printf("%d %d\n",maxd,cnt);
	}
	return 0;
}