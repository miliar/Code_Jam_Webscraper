#include <cstring>
#include <iostream>
#include <cstdio>
using namespace std;
int n,r,p,s;
string yu[3][13];
string ans;
bool ok(string str){
	int nr=0,np=0,ns=0;
	int l=str.length();
	for (int i=0;i<l;i++){
		if(str[i]=='R') nr++;
		if(str[i]=='P') np++;
		if(str[i]=='S') ns++;
	}
	if(nr==r&&np==p&&ns==s) return true;
	return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
	yu[0][0]="R";
	yu[1][0]="P";
	yu[2][0]="S";
	for (int i=1;i<=12;i++){
		for (int j=0;j<3;j++){
			int k=(j+2)%3;
			if(yu[j][i-1]<yu[k][i-1]){
				yu[j][i]=yu[j][i-1]+yu[k][i-1];
			}
			else {
				yu[j][i]=yu[k][i-1]+yu[j][i-1];
			}
		}
	}
	int T,ca=1;
	scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",ca++);
		scanf("%d%d%d%d",&n,&r,&p,&s);
		ans="Z";
		for (int i=0;i<3;i++){
			if(ok(yu[i][n])){
				if (ans>yu[i][n]){
					ans=yu[i][n];
				}
			}
		}
		if(ans[0]=='Z') printf("IMPOSSIBLE\n");
		else printf("%s\n",ans.c_str());
	}
	return 0;
}
