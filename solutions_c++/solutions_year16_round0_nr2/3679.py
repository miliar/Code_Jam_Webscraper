#include <bits/stdc++.h>
#define FOR(i,a) for(i = 0; i < a; i++)
#define FR(i,a,b) for(i = a; i < b; i++) 
#define F first
#define S second
typedef long long ll;
using namespace std;
int main(){
	long long i,j,steps,T,test;
	string s;
	char ch;
	// freopen("a.in","r",stdin);
	// freopen("a.out","w",stdout);
	cin >> T;
	FR(test,1,T+1){
		cin >> s;
		steps = 0;
		FOR(i,s.length()){
			while(s[i]==s[i+1]){
				i++;
			}
			steps++;
		}
		if(s[s.length()-1]=='-')
			cout << "Case #" << test << ": " << steps << endl;
		else{
			cout << "Case #" << test << ": " << steps-1 << endl;
		}
	}
	return 0;
}