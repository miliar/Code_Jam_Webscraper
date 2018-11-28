#include<iostream>
#include<cstdio>
#include<cmath>

int A[1001];
using namespace std;

int main(){
	char w;
	char s[1001];
	long long int stand =0;
	long long int req =0;
	int t,max;
	scanf("%d",&t);
	for (int i=1;i<=t;i++){
		stand = 0;
		req =0;
		scanf("%d",&max);
		cin>>s;
		for(int j=0;j<=max;j++){
			A[j]=(int) (s[j]-'0');
			if(stand<j){
				req+=j-stand;
				stand+=A[j]+j-stand;
			}
			else stand+=A[j];
		}
		printf("Case #%d: %llu\n",i,req);
	}
return 0;
}
