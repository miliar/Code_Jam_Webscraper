#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define toDigit(c) (c-'0')

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int numOfCase; // read number of test case
  scanf("%d", &numOfCase);

  // looping for case
	for (int caseNo = 1; caseNo <= numOfCase; caseNo++) 
 	{
    	printf("Case #%d: ", caseNo);

		int maxS;
		string shyListString;
		cin >> maxS >> shyListString;

		int extra = 0;
		int standupCount = 0;

		for (int i = 0; i < shyListString.length(); i++)
		{
			int shyLevel = toDigit(shyListString[i]);
			if(standupCount>=i){
				standupCount += shyLevel;

			}else{
				int additional = (i-standupCount);

				if(additional + standupCount >= maxS){
					additional = maxS - standupCount;
				}else{
					standupCount = standupCount + additional + shyLevel;
				}

				extra += additional;
			}
		

			if(standupCount >= maxS){
				break;
			}

		}
		cout << extra << endl;

	}

  return 0;
}
