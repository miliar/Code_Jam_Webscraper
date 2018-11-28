#include <iostream>
#include <list>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        std::string S, outS;
        cin >> S;
        std::list<char> L;
        L.push_back(S[0]);
        for(int j = 1; j < S.size(); j++) {
            if(S[j] >= L.front()) L.insert(L.begin(), S[j]);
            else L.push_back(S[j]);
        }
        std::list<char>::iterator it;
        cout << "Case #" << i+1 << ": ";
        for(it = L.begin(); it!=L.end(); it++) {
            cout << *it;
        }
        cout << endl;
    }
	// your code goes here
	return 0;
}
