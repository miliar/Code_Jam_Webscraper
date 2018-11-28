#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int n,nr,np,ns;
string r[13],p[13],s[13];

bool cal(string &ans){
	int le = ans.length();
	int rr=0,pp=0,ss=0;
	for(int i=0;i<le;i++){
		if(ans[i] == 'R')rr++;
		else if(ans[i]=='P')pp++;
		else ss++;
	}
	if(nr== rr && np==pp && ns==ss)return true;
	return false;
}


int main()
{
	r[0]="R";p[0]="P";s[0]="S";
	for(int i=1;i<=12;i++){
			p[i] = r[i-1]>p[i-1]?(p[i-1]+r[i-1]):(r[i-1]+p[i-1]);
			s[i] = p[i-1]>s[i-1]?(s[i-1]+p[i-1]):(p[i-1]+s[i-1]);
			r[i] = r[i-1]>s[i-1]?(s[i-1]+r[i-1]):(r[i-1]+s[i-1]);
	}
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		string ans ;
		scanf("%d%d%d%d",&n,&nr,&np,&ns);
		if(cal(r[n]))ans = r[n];
		else ans ="ZZ";
		if(cal(p[n]))ans = min(ans,p[n]);
		if(cal(s[n]))ans = min(ans,s[n]);

		printf("Case #%d: ",cs);
		if(ans[0]!='Z'){
			printf("%s\n",ans.c_str());
		}
		else {
			printf("IMPOSSIBLE\n");
		}

	}


	return 0;
}
