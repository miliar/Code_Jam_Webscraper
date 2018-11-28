#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

#include <math.h>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

int main(int argc, char** argv) {

	LL T;cin>>T;

	for(LL t=1; t<=T; t++)
	{
        LL K,C,S;
		cin>>K>>C>>S;
        
        cout << "Case #" << t << ": ";
        for(LL i=0; i<K; i++)
            cout << i+1 << " ";

        cout << endl;
	}

	return 0;
}

