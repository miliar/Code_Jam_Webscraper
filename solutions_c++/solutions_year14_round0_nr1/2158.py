#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>


using namespace std;

set<int> possibilities;
vector<int> answers;

void solve() {
    
    possibilities.clear();
    answers.clear();
    
	int k;
	scanf("%d", &k);
	for (int i=1; i<=4; i++) {
	    int a[4];
	    scanf("%d %d %d %d\n", a, a+1, a+2, a+3);
	    if (k==i) {
	        // Chosen row
	        for (int j=0; j<4; ++j) {
	            possibilities.insert(a[j]);
	        }
	    }
	}
	
	scanf("%d", &k);
	for (int i=1; i<=4; i++) {
	    int a[4];
	    scanf("%d %d %d %d\n", a, a+1, a+2, a+3);
	    if (k==i) {
	        // Chosen row
	        for (int j=0; j<4; ++j) {
	            if ( possibilities.count(a[j]) == 1 ) {
	                answers.push_back(a[j]);
	            }
	        }
	    }
	}
	
	if ( answers.size() == 0 ) printf("Volunteer cheated!\n");
	else if ( answers.size() == 1 ) printf("%d\n", answers[0]);
	else printf("Bad magician!\n");
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
