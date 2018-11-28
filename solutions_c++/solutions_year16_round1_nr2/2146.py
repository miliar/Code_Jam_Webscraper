
#include<stdio.h>
#include<string>
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#define B int testb;scanf("%d", &testb);int t = testb;while(t--)
using namespace std;
int main(){
	int i,a,N,input;
	map<int,int> H;
	vector<int> ans;
	B{
		printf("Case #%d: ", testb-t);
		scanf("%d",&N);
		H.clear();
		ans.clear();
		input = 2 * N * N - N;
		for(i = 0;i < input; i++){
			scanf("%d",&a);
			H[a]++;
		}
		for(map<int,int>::iterator iter = H.begin(); iter != H.end(); ++iter){
			if(iter->second % 2 != 0)
			ans.push_back(iter->first);
		}
		sort(ans.begin(),ans.end());
		
		for(vector<int>::iterator iter = ans.begin(); iter != ans.end(); ++iter){
		
			cout<<*iter<<" ";
		}
		printf("\n");
	}
}
