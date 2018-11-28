#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <queue>
#include <list>
#include <set>
#include <stack>
#include <deque>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define INF  2147483647

const int size = 4;
int t, row, num;
map <int, int> m;

int main() {
	freopen("A-small-attempt1.txt", "r", stdin); freopen("A-small-attempt1-out.txt", "w", stdout);
	
	scanf("%d", &t);
	int tt = 0;
	while (tt++ < t) {
		m.clear();
		for(int k = 0; k < 2; ++k) {
		    scanf("%d", &row);
		    for(int i = 0; i < size; ++i) 
			    for(int j = 0; j < size; ++j) {
				    scanf("%d", &num);
				    if(i == row - 1) 
					    ++m[num];
			    }
		}

		printf("Case #%d: ", tt);
		map <int,int>::iterator it;
		for(it = m.begin(); it != m.end(); ++it)
			if(it->second > 1)
				break;
		if(it == m.end()) {
			printf("Volunteer cheated!\n");
			continue;
		}
		map <int,int>::iterator it2 = it;
		for(++it2; it2 != m.end(); ++it2)
			if(it2->second > 1)
				break;
		if(it2 == m.end())
			printf("%d\n", it->first);
		else
			printf("Bad magician!\n");
	}

	return 0;
}