#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define endl "\n"
#define mp make_pair
#define pb push_back
string s;
int f(int i, int isPos){
		if(i<0) return 0;

		if(s[i]== '+' && isPos){
			return f(i-1,isPos);

		}
		else if(s[i]== '-' && !isPos){
			return f(i-1,isPos);

		}
		else return 1+f(i-1,!isPos);
	
}
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int cnt=1;
	while(T--){

		cin >> s;
		cout << "Case #" << cnt++ << ": ";
		cout << f(s.size()-1,true) << endl;
	}

	return 0;
}