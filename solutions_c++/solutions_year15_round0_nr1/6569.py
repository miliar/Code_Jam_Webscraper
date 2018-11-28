#include <bits/stdc++.h>
using namespace std;

void run() {
    int max_shy;
    cin>>max_shy;
    string str;
    cin>>str;
    
    int current = str[0] - '0';
    int invites = 0;
    for (int i = 1; i <= max_shy; ++i) {
        if (i > current) {
            invites += i - current;
            current = i;
        }
        current += str[i] - '0';
    }
    cout<<invites;
}

int main() {
	int tests;
	cin>>tests;
	for (int test = 1; test <= tests; ++test) {
	    cout<<"Case #"<<test<<": ";
	    run();
	    cout<<"\n";
	}
}