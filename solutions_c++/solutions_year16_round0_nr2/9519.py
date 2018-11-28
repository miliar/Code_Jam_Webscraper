#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

lli go(string &S, int pos){
	if(pos == 0){
		if(S[pos] == '+') return 0;
		else return 1;
	}
	if(S[pos] == '+'){
		return go(S,pos-1);
	}else{
		if(S[pos-1] == '+'){
			return go(S,pos-1) + 2LL;
		}else{
			return go(S,pos-1);
		}
	}
} 
int main(){
	int t;
	string S;
    scanf("%d",&t);
    for(int q = 0;q<t;q++){
    	cin>>S;
    	int n = S.length();
    	lli ans = go(S,n-1);
    	printf("Case #%d: %lld\n",q+1,ans);
    }   
    return 0;
}