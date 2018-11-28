#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
using namespace std;
int T;
bool testp(int x){
	int i,j;
	vector<int>v;
	while(x!=0){
		v.push_back(x%10);x/=10;
	}
	for(i=0;i<(int)v.size()/2;i++){
		if(v[i]!=v[v.size()-1-i])return false;
	}
	return true;
}
int main(){
	int i,j,k;
	int t;
	int A,B;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&A,&B);
		int cnt=0;
		int x=(int)sqrt((double)(A-1))+1;
		for(;x*x<=B;x++){
			if(testp(x)&&testp(x*x)){
				cnt++;
				//printf(">%d %d\n",x,x*x);
			}
		}
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
	
