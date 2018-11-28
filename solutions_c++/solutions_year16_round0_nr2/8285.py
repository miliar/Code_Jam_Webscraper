#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <cstdlib>
using namespace std;

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

bool allHappy(string pancake) {
    int len = pancake.length();
    bool happy = true;
    for (int i=0; i<len && happy; i++) {
        if (pancake[i]!='+') {
            happy = false;
        }
    }
    return happy;
}

string flip(string pancake, int n) {
    string result = pancake;
    for (int i=0; i<=n; i++) {
        if (result[i]=='-') {
            result[i]='+';
        }
        else result[i]='-';
    }
    return result;
}

int pancakeFlipping(vector<int> vis, string pancake, int len, int flipped) {
    int min = 1000000;
    if (allHappy(pancake)) {
        return flipped;
    }
    else if (flipped<len) {
        for (int i=0; i<len; i++) {
            if (vis[i]==0) {
                vis[i] = 1;
                string next = flip(pancake, i);
                int retVal = pancakeFlipping(vis, next, len, flipped+1);
                //cout << i << " " << flipped << " " << retVal << endl;

                if (retVal<min) min=retVal;
            }
        }
        return min;
    }
    else return min;
}

int main() {
	int T;
	scanf("%d",&T);
	getchar();
	for (int i=0; i<T; i++) {
		string pancake;
        getline(cin, pancake);
        int len = pancake.length();
        vector<int> vis;
        for (int j=0; j<len; j++) {
            vis.push_back(0);
        }

        printf("Case #%d: %d\n",i+1, pancakeFlipping(vis, pancake, len, 0));

	}
	return 0;
}