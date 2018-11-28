#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <utility>
#include <map>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
#define REP(i,a,b) for(int (i)=(a);(i)<(b);++(i));

//global vars
int N,X;
vi S;

int main(){
	int TC;cin>>TC;
	for(int T=1;T<=TC;++T){
		printf("Case #%d:",T);
		S.clear();
		cin>>N>>X;
		for(int i=0;i<N;++i){
			int I;cin>>I;S.push_back(I);
		}
		sort(S.begin(),S.end());
		int C=0;
		//for(int i=0;i<S.size();++i){printf("%d ",S[i]);}
		while(!S.empty()){
			//int idx=-1;
			int LB=X-S[S.size()-1];S.erase(S.end()-1);
			if(S.size()==0){++C;break;}
			vi::iterator it=lower_bound(S.begin(),S.end(),LB);
			if(it==S.end()){S.erase(S.end()-1);++C;continue;}
			if(*it==LB){S.erase(it);++C;continue;}
			if(it==S.begin()){++C;continue;}
			S.erase(it-1);++C;
		}
		printf(" %d\n",C);
	}
	return 0;
}