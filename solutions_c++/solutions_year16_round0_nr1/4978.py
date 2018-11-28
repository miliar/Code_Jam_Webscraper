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
	int A[10], num;
	ll N,T,i, temp, temp2;
	cin >> T;
	for(i = 1;i<=T;++i){
		cin >> N;
		cout << "Case #" << i << ": ";
		if(N==0){
			cout << "INSOMNIA\n";
			continue;
		}
		memset(A,0,sizeof(A));
		temp2 = num = 0;
        while(num < 10){
        	temp2+=N;
        	temp = temp2;
        	while(temp!=0){
                if(A[temp%10] == 0){
                	++num;
                	A[temp%10] = 1;
                }
                temp/=10;
        	}
        }
        cout << temp2 << '\n';
	}
    return 0;
}
