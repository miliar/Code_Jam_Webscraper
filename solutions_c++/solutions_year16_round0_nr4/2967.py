#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	int t, k, c, s;
    fstream f1;
    f1.open("Txt.txt",ios::out);
	cin >> t;
	for(int ind=1 ; ind<=t ; ind++){
		cin >> k >> c >> s;
	    f1 << "Case #" << ind << ": ";
	    for (int i=1 ; i<=s ; i++)
	    	f1 << i << ' ';
	    f1 << '\n';
	}
    f1.close();
	return 0;
}
