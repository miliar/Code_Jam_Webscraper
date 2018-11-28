#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <utility>
#include <stdio.h>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <assert.h>


using namespace std;
int currCase = 0;

/*
 * Global variables that are needed should be declared here
 */

int s[1001];
/**********************************************************/


void runTestCase(){
	printf("Case #%d: ", ++currCase);
	int Smax;

	assert(scanf("%d", &Smax) == 1);


	for(int i = 0; i <= Smax; ++i){
		assert(scanf("%1d", &s[i]) == 1);
	}

	int i = 0;

	int standing = 0;
	int friends = 0;
	while(i < Smax + 1){
		if(standing >= i){
			standing += s[i];
		}else{
			friends = friends + (i - standing);
			standing = standing + s[i] + (i - standing);
		}
		++i;
	}

	printf("%d\n", friends);

	return;
}

void setUp(){

	return;
}

int main(){
	setUp();

	int t;


	assert(scanf("%d", &t) == 1);

	while(t > 0){

		runTestCase();
		t--;
	}

	return 0;
}
