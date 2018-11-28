#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
int a,b,C,caso;

bool isPal(int n){
	string s="";
	while(n>0){
		int d=n%10;
		n/=10;
		s=char(d+'0')+s;
		}
	string t=s;
	reverse(t.begin(),t.end());
	return t==s;
	}
int f(int n){
	if(n*n<a)return false;
	if(!isPal(n))return false;
	if(!isPal(n*n))return false;
	return true;
	}
void doit(){
	scanf("%d%d",&a,&b);
	int ans=0;
	for(int i=1;i<=b/i;++i)if(f(i))++ans;
	printf("Case #%d: %d\n",++caso,ans);
	}
int main(){
	scanf("%d",&C);
	caso=0;
	for(int i=0;i<C;++i)doit();
	}
