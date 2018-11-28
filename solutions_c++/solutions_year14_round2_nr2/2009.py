#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>

using namespace std;

int main(){
	int N,testCase = 1,A,B,K,count = 0;
	cin>>N;
	map<int,int> seen;
	while(testCase <= N){
		count = 0;
		seen.clear();
		scanf("%d %d %d",&A,&B,&K);
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				if((i&j) < K) {count++;}
				//cout<<i<<" "<<j<<" "<<(i&j)<<"\n";
				//cout<<(i&j)<<"\n";
			}
		}
		printf("Case #%d: %d\n",testCase,count);
		testCase++;
	}
	
}