#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <stack>
#include <math.h>
#include <stdlib.h>
#include <queue>
#include <string>
#include <algorithm>
#include <stack>
#include <list>
using std::priority_queue;
using std::cin;
using std::cout;
using std::map;
using std::endl;
using std::vector;
using std::string;
using std::stack;
using std::list;

int shyCount[1100];
int standCount[1100];
int audienceSize;
int traverse(){
	int totalStanding = 0;
	int friends = 0;
	int k = 0;
	int shyLevel = 0;
	bool up = false;
	while (shyCount[k] != -1){
		if (shyLevel <= totalStanding){
			totalStanding += shyCount[k];
		}
		else if (shyCount[k] != 0){
			friends += shyLevel - totalStanding;
			totalStanding += friends;
			up = true;
		}
		if (!up){
			++k;
			++shyLevel;
		}
		else {
			up = false;
		}
		
	}
	return friends;
}

int main(){
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; ++i){
		int maxShyness;
		cin >> maxShyness;
		string people;
		cin >> people; 
		for (int j = 0; j < people.size(); ++j){
			shyCount[j] = people[j] - '0';
			audienceSize += shyCount[j];
		}
		shyCount[people.size()] = -1;
		cout << "Case #" << i + 1 << ":" << " " << traverse() << endl;
	}
}