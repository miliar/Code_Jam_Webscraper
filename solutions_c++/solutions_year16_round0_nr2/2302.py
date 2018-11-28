#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map>
#include <set>

using namespace std;
string s;
set<string>st;
int main() {
	ios::sync_with_stdio(false);cin.tie(0);
    int cases;
    cin>>cases;
    int tc=1;
    while(cases--){
		cout<<"Case #"<<tc++<<": ";
		cin>>s;
		char last=s[0];
		int groups=1;
		for(int i=1;i<s.size();i++){
			if(last!=s[i])groups++;
			last=s[i];
		}
		if(s.back()=='+')groups--;
		cout<<groups<<"\n";
    }
 }


