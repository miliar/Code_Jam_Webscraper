#include <bits/stdc++.h>
using namespace std;

int t,n;
char last;
string s;
int moves;

int main(){
    cin >> t;
    for(int ii=1;ii<=t;ii++){
        cin >> s;
	moves = 0;
	last = s[0];
	n = s.length();

	for(int i=1;i<n;i++){
	    if(s[i] == last) continue;
	    last = s[i];
	    moves ++;
	}
	if(last == '-') moves++;
        
	printf("Case #%d: %d\n",ii,moves);
    }
    return 0;
}
