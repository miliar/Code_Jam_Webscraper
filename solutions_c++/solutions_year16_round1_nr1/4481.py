#include<cstdio>
#include<string>
#include<cstring>
using namespace std;

const int maxn=1010;
char s[maxn];
string A;
int n;
void solve(){
	scanf("%s",s);n=strlen(s);
	A="";
	for(int i=0;i<n;++i)A=max(s[i]+A,A+s[i]);
	printf("%s\n",A.c_str());
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int kase,i=0;scanf("%d",&kase);
	for(int i=1;i<=kase;++i){
		printf("Case #%d: ",i);
		solve();
	}
//	for(;;);
	return 0;
}
