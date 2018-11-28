#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll T, num,i,j;
	cin >> T;
	for(i = 1;i<=T;++i){
        string S;
        cin >> S;
        cout << "Case #" << i << ": ";
        num = 1;
        for(j = 1;j<S.size();++j){
           if(S[j] != S[j-1]) ++num;
        }
        if(S[S.size()-1] == '+') --num;
        cout << num << '\n';
	}
    return 0;
}
