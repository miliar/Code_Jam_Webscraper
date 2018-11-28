#include<cstdio>
#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
bool isPalin(long long num){
	stringstream ss;
	string sNum,sNumR;
	long long numR;
	ss<<num;
	ss>>sNum;
	sNumR=sNum;
	reverse(sNumR.begin(),sNumR.end());
	ss<<sNumR;
	ss>>numR;
	ss<<numR;
	ss>>sNumR;
	return sNum == sNumR;
}
int main(){
	vector<long long> goodNum;
	int three=3;
	for(long long i=1;i<=10000000;i++){
		if(isPalin(i) && isPalin(i*i)){
			goodNum.push_back(i*i);
		}
		if(i==three){
			i=i/3*10;
			three*=10;
		}
	}
	int C;
	scanf("%d",&C);
	for(int Case=1;Case<=C;Case++){
		long long A,B;
		int ans=0;
		cin>>A>>B;
		for(int i=0;i<goodNum.size();i++)
			if(A<=goodNum[i] && goodNum[i]<=B)
				ans++;
		printf("Case #%d: %d\n",Case,ans);
	}
	/*long long sum[55]={};
	sum[1]=3;
	for(int i=2;i<=50;i++){
		// start from 1
		sum[i]=1L<<((i-1)>>1);
		if(i&1)
			sum[i]+=i>>1;
		// start from 2
		sum[i]++;
		if(i&1)
			sum[i]++;
	}*/
	
}
