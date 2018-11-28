#include <iostream>
#include <algorithm>
#include <cstdio>


using namespace std;


int main(){
	
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int i,x,j,stand,res;
	string S;
	for(i=1;i<=T;i++)
	{
		cin >> x >> S;
		stand = 0; res = 0;
		for(j = 0; j<S.size();j++){
			if( S[j] >= '0' && j > stand) { res += j - stand; stand += j - stand; }
			stand += S[j] - '0';
		}
		
		cout << "Case #" << i << ": " << res << endl; 
	}

}
