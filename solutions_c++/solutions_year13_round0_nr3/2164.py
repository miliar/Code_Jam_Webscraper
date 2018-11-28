#include "stdio.h"
#include "string.h"
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int a,b;
bool IsP(int n){
	int cnt=0;
	char str[15];
	while(n){
		str[cnt]=n%10;
		cnt++;
		n/=10;
	}
	for(int i=0;2*i<cnt;i++){
		if(str[i]!=str[cnt-i-1])
			return false;
	}
	return true;
}
int Check(int n){
	int cnt=0;
	for(int i=1;i*i<=n;i++){
		if(IsP(i)==false) continue;
		if(IsP(i*i)) cnt++;
	}
	return cnt;
}
void Solve(){
	printf("%d\n",Check(b)-Check(a-1));
}
int main(){
	freopen("D:\\Test\\in.txt","r",stdin);
	freopen("D:\\Test\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d %d",&a,&b);	
		printf("Case #%d: ",t);
		Solve();
	}
    return 0;
}