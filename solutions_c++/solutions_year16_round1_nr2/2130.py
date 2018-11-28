//The Last Word
#include<stdio.h>
#include<string>
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#define T int test;scanf("%d", &test);int t = test;while(t--)
using namespace std;
int main(){
	int i,a,N,input;
	map<int,int> H;
	vector<int> ans;
	T{
		printf("Case #%d: ", test-t);
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
			//printf("%d ",citer);
			cout<<*iter<<" ";
		}
		printf("\n");
	}
}
