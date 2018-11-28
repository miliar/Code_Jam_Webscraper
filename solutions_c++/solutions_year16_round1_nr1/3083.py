#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<deque>
#include<set>
#include<map>
#include<iterator>
#include<ctime>
#include<iterator>
#include<numeric>
#include<fstream>

#define CLOCK cerr<<"Time elapsed: "<<1.0 * clock()/CLOCKS_PER_SEC<<" s.\n";
#define length(a,type) sizeof(a)/sizeof(type);

using namespace std;

template<class T>
bool checkEquality(T a,T b){return a==b;}
template<class T>
bool checkGreater(T a,T b){return a>b;}

long long limit=9223372036854775807;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout); 
	int T;
	string w;

	scanf("%d",&T);
	for(int num=1;num<=T;++num){
		cin>>w;
			deque<char> Q;
		Q.push_front(w[0]);
		for(int i=1;i<w.size();++i){
			if(Q.front()>w[i])
			   Q.push_back(w[i]);
			else
			   Q.push_front(w[i]);
		}
		

		printf("Case #%d: ",num);
		while(!Q.empty()){
			printf("%c",Q.front());
			Q.pop_front();
		}
		printf("\n");
		
	fflush(stdout);
	}
	
			

	return 1;
}
