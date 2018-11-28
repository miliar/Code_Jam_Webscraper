#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t, cnt;
    string s;
    char x;
    fstream f1;
    f1.open("Txt.txt",ios::out);
    cin >> t;
    for(int j=1 ; j<=t ; j++){
    	x='+';
    	cnt=0;
    	cin >> s;
    	for(int i=s.size()-1 ; i>=0 ; i--)
    		if(s[i]!=x){
    			cnt++;
    			x= x=='+' ? '-' : '+';
    		}
    	f1 << "Case #" << j << ": " << cnt << '\n';
    }
    f1.close();
    return 0;
}
