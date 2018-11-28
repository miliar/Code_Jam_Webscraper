#include <iostream>
#include <string>

using namespace std;

int main() {
	int N;
    cin >> N;
    for (int iter=1; iter<=N; iter++){
    	string s;
    	cin >> s;
    	int flips=0;
    	if(*(s.begin()) == '-')
    		flips=1;
    	for (string::iterator it = s.begin()+1; it != s.end(); ++it)
    	{
    		// cout << *(it-1) << endl;
    		if (*(it-1) == '+')
    			if (*(it) == '-')
    				flips += 2;

    		// if (*(it-1) == '-')
    		// 	if (*(it) == '+')
    		// 		flips += 1;
    	}
    	cout << "Case #" << iter << ": " << flips << endl;
    }
    return 0;
}