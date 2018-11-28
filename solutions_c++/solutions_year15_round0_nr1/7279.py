#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <limits> 
#include <climits> 
#include <cassert>
using namespace std;



int main(int argc, char ** argv) {
	if (argc > 1)
	{
		FILE * file = freopen("input.txt", "r", stdin);
	}
	freopen("output.txt", "w", stdout);
	int T{ 0 };
	cin >> T;

	for (int caseNum = 1; caseNum <= T; caseNum++){
		int shynessMax{ 0 };
		cin >> shynessMax;

		string audience;
		cin.get();
		getline(cin, audience);
		int numFriends{ 0 };
		int numClamping{ 0 };

		for (int shynessLevel = 0; shynessLevel < audience.size(); shynessLevel++){
			int shynessLevelPeople = audience[shynessLevel] - '0';

			if (shynessLevel <= numClamping){
				numClamping += shynessLevelPeople;
			}
			else if(shynessLevel > numClamping){
				int numFriendsNeeded = shynessLevel - numClamping;
				numFriends += numFriendsNeeded;
				numClamping += (numFriendsNeeded + shynessLevelPeople);
			}
		}
		cout << "Case #" << caseNum << ": "  << numFriends << endl;
	}

	 


	return 0;
}
