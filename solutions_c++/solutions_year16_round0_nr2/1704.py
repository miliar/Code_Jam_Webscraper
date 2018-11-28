#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	string s;
	for(int i=0;i<T;i++){
		cin >> s;
		s+="+";
		int ans=unique(s.begin(),s.end())-s.begin()-1;
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}