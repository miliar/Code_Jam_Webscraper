#include <bits/stdc++.h>

using namespace std;
typedef  long long ll;

#define X first
#define Y second

int solve(int R,int C,int W){
	if(R>1)return solve(1,C,W)+(R-1)*(C/W);
	//else
	if(2*W<C)return solve(1,C-W,W)+1;
	//else
	assert(C>=W);
	if(W==C)return C;
	return W+1;
}
int main(){
	int T;cin >>T;
	for(int tt=0;tt<T;tt++){
	int R,C,W;
	cin >>R>>C>>W;
	cout << "Case #"<<tt+1<<": "<<solve(R,C,W)<<endl;
	}
}
