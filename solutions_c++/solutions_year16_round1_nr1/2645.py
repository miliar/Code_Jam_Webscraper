#include <iostream>
#include <string>
#include <list>

using namespace std;

list<char> generateBest(string S)
{
    list<char> vec;
    size_t len = S.length();
    for(int i = 0; i < len; i++)
        if(S[i] < vec.front())
            vec.push_back(S[i]);
        else
            vec.push_front(S[i]);
    return vec;
}

int main()
{
    int T, len;
    string S;
    list<char> Y;
	cin >> T;
	for(int i = 1; i <= T; i++) {
        cin >> S;
	    cout << "Case #" << i << ": ";
	    len = S.length();
        Y = generateBest(S);
	    for(list<char>::iterator it = Y.begin(); it != Y.end(); it++) cout << *it;
	    cout << endl;
	}
}
