#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int x,q,w,e,r,q1,answer,status,dummy;
int counter = 0;
int printStatus[101];
int answerStatus[101];

void make() {
	status = 0;
	q1 = 0;
	q = w = e = r = 0;
    ++counter;
    //printf("Case #%d: ", counter);
    scanf("%d", &x);
    for(int i = 1; i <= 4; i++ ) {
    	if( i == x ) {
    		scanf("%d %d %d %d", &q, &w, &e, &r);
    	}
    	else {
    		scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
    	}
	}
    scanf("%d", &x);    
    for(int j = 1; j <= 4; j++ ) {
    	if( j == x ) {
    		for( int z = 1; z <= 4; z++ ) {
    			scanf("%d", &q1);
    			if( q1 == q ) {
    				status++;
    				answer = q;
    			}
    			if( q1 == w ) {
    				status++;
    				answer = w;
    			}
    			if( q1 == e ) {
    				status++;
    				answer = e;
    			}
    			if( q1 == r ) {
    				status++;
    				answer = r;
    			}
    		}
    	}
    	else {
    		scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
    	}
	}/*
	if( status == 0 ) {
		printf("Volunteer cheated!\n");
	}
	else if ( status == 1) {
		printf("%d\n",answer);
	}
	else {
		printf("Bad magician!\n");
	}*/
	printStatus[counter] = status;
	answerStatus[counter] = answer;
}
void printResult(int t3) {
	printf("Case #%d: ", t3);
	if( printStatus[t3] == 0 ) {
		printf("Volunteer cheated!\n");
	}
	else if ( printStatus[t3] == 1) {
		printf("%d\n",answerStatus[t3]);
	}
	else {
		printf("Bad magician!\n");
	}
}
int main() {
    int t,t2; scanf("%d", &t);
    t2 = 0;
    while(t2 < t) {
        make();
        t2++;
    }
    t2 = 1;
    while(t2 <= t) {
        printResult(t2);
        t2++;
    }
    return 0;
}
