#include <iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
using namespace std;
const int N = 10005;
int T,n,X;
string L;
string str;
int mult[5][5]={ {0,0,0,0,0},
				 {0,1,2,3,4},
				 {0,2,-1,4,-3},
				 {0,3,-4,-1,2},
				 {0,4,3,-2,-1}};
int id(char c){
	if(c=='i')return 2;
	if(c=='j')return 3;
	if(c=='k')return 4;
}
int Multi(int x,int y){
	int ans = mult[int(abs(x))][int(abs(y))];
	if(x<0)ans*=-1;
	if(y<0)ans*=-1;
	return ans;
}
int pre[N],post[N];
void solve(){
	scanf("%d%d",&n,&X);
	cin>>L;
	str="";
	for(int i=0;i<X;i++)str+=L;
	n=n*X;

	pre[0]=id(str[0]);
	for(int i=1;i<n;i++){
		pre[i]=Multi(pre[i-1],id(str[i]));
	}
	post[n-1]=id(str[n-1]);
	for(int i=n-2;i>=0;i--){
		post[i]=Multi(id(str[i]),post[i+1]);
	}
	/*puts("bug1");
	for(int i=0;i<n;i++)printf("%d",pre[i]);cout<<endl;
	puts("bug2");
	for(int i=0;i<n;i++)printf("%d",post[i]);cout<<endl;*/
    bool ok=0;
	bool hasi=0;
	for(int i=0;i<n-1;i++){
		//cout<<'T'<<' '<<i<<' '<<pre[i]<<' '<<hasi<<' '<<post[i+1]<<endl;
		if(pre[i]==4&&hasi==1&&post[i+1]==4){
			ok=1;
			break;
		}
		if(pre[i]==2)hasi=1;
	}
	if(ok)puts("YES");
	else puts("NO");
}
int main(){
	scanf("%d",&T);
	for(int cas=0;cas<T;cas++){
		printf("Case #%d: ",cas+1);
		solve();
	}
	return 0;
}
