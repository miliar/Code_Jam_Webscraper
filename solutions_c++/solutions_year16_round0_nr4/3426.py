#include<bits/stdc++.h>
#define endl '\n'
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ll long long
#define ld long double
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	int ncases, caseNumber = 1;
	cin >> ncases;
	while(ncases--){
		int k,c,s;
		cin >> k >> c >> s;
		
		cout << "Case #" << caseNumber << ": ";
		for(int i=1;i<=k;++i)
			cout << i << " ";
		cout << endl;
		caseNumber++;
	}
	return 0;
}