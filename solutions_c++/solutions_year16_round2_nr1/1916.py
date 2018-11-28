#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#define LEN 'Z'-'A'+1

using namespace std;

int main(){
	long long T,t;
	string str;
	long count[LEN];
	string vals[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	cin >> T;
	for(t=1;t<=T;++t){
		for(int i=0;i<LEN;++i)
			count[i]=0;
		cin >> str;
		for(size_t i=0;i<str.size();++i)
			count[str[i]-'A']+=1;
		cout << "Case #"<<t<<": ";
		vector<int> resp;
		int nums[10]={0,2,4,6,8,1,3,5,7,9};
		for(int k=0;k<10;++k){
			int i = nums[k];
			bool has;
			do{
				has=true;
				for(size_t j=0;j<vals[i].size();++j){
					has = has && count[vals[i][j]-'A']>0;
				}
				if(has){
//					cout<<i;
					resp.push_back(i);
					for(size_t j=0;j<vals[i].size();++j)count[vals[i][j]-'A']-=1;
				}
			}while(has);
		}
		sort(resp.begin(),resp.end());
		for(size_t i=0;i<resp.size();++i)
			cout << resp[i];
		cout <<endl;
	}
	return 0;
}
