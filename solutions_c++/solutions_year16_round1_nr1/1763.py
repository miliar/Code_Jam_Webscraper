#include <iostream>
#include <vector>
#include <utility>
#include <deque>
#include <cstring>

typedef unsigned long int uli;
typedef long int li;
using namespace std;

string compute_res(string& inp) {
	deque<char> mydeque;
	mydeque.push_back(inp[0]);
	for(int i=1; i<inp.size(); i++) {
		if(inp[i]<mydeque.front()) {
			mydeque.push_back(inp[i]);
		} else {
			mydeque.push_front(inp[i]);
		}
	}
	string res = "";
	for(int i=0; i<inp.size(); i++) {
		res += mydeque.front();
		mydeque.pop_front();
	}
	return res;
}

int main(int argc, char *argv[])
{
	int T;
	string inp, res;
	cin >> T;
	for(int i=1; i<=T; i++) {
		cin >> inp;
		res = compute_res(inp);
		cout << "Case #" << i << ": " << res << endl;
	}
    return 0;
}
