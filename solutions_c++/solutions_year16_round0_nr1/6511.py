#include<bits/stdc++.h>

using namespace std;
#define END 100

int main() {
	ifstream in("A-large.in");
    int t,n;
    in >> t;
    for(int i = 0; i < t; i++) {
        in >> n;
        set<int> s;
        int mem;
        for(int j = 1; j <= END; j++) {
            int cur = n * j;
            mem = cur;
            while(cur > 0) {
                int digit = cur % 10;
                cur /= 10;
                if(s.find(digit) == s.end()) {
                    s.insert(digit);
                }
                if(s.size() == 10){
                    break;
                }
            }
            if(s.size() == 10){
                break;
            }
        }
        cout << "Case #" << (i+1) << ": ";
        if(s.size() == 10) {
            cout << mem << endl;
        }
        else {
            cout << "INSOMNIA" << endl;
        }

    }

	return 0;
}
