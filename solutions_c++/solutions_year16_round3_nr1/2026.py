#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <set>
#include <vector>

using namespace std;
typedef long long ll;

#define MAX_N (30)

int A[MAX_N];
int N;

int count_sum() {
    int ret = 0;
    for ( int i = 0; i < N; i++ ) {
	ret += A[i];
    }
    return ret;
}

int majority_index() {
    int majority = 0;
    int index = -1;

    for ( int i = 0; i < N; i++ ) {
	if ( majority < A[i] ) {
	    majority = A[i];
	    index = i;
	}
    }
    return index;
}

int count_party() {
    int ret = 0;
    for ( int i = 0; i < N; i++ ) {
	if ( A[i] > 0 ) ret++;
    }
    return ret;
}

vector<int> find_two() {
    vector<int> ret;
    for ( int i = 0; i < N; i++ ) {
	if ( A[i] > 0 ) {
	    ret.push_back( i );
	}
    }

    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for ( int t = 0; t < T; t++ ) {
	scanf("%d", &N);
	for ( int i = 0; i < N; i++ ) {
	    scanf("%d", &A[i]);
	}

	printf("Case #%d:", t+1);
	while ( true ) {
	    int num_party = count_party();
	    if ( num_party == 0 ) break;
	    printf(" ");

	    if ( num_party >= 3 ) {
		int mi = majority_index();
		printf("%c", 'A' + mi);
		A[mi]--;
	    }
	    else {		// count_party <= 2
		vector<int> tp = find_two();
		printf("%c%c", 'A' + tp[0], 'A' + tp[1]);
		A[tp[0]]--;
		A[tp[1]]--;
	    }
	}

	printf("\n");
    }

    return 0;
}
