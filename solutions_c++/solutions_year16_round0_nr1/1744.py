#include <algorithm>
#include <stdio.h>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

void num_insert(set<int>& num, int N){
	int cur;
	if(N==0){
		num.insert(N);
		return;
	}
	while(N>0){
		//cout<<N<<endl;
		cur = N%10;
		num.insert(cur);
		N/=10;
	}
	return;
}

int main(){
	int T,N;
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		printf("Case #%d: ",i+1);
		scanf("%d",&N);
		set<int> num;
		num_insert(num,N);
		int cur = N*2;
		//int c = 1;
		while(cur!=N){
			//cout<<cur<<' '<<num.size()<<endl;
			num_insert(num,cur);
			if(num.size()==10) break;
			cur+=N;
			//c++;
		}

		if(num.size()==10) cout<<cur<<endl;
		else cout<<"INSOMNIA\n";
		
	}
	return 0;
}