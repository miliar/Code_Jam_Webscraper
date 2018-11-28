#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi; 

typedef unsigned int uint;

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define MAX_DISTANCE (300000)

inline void printB(vvi &B, int N, int M) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < M; y++)
            cout << B[x][y];
        cout << endl;
    }
}

inline int check(vvi &B, int N, int M) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < M; y++)
            if (B[x][y] == 0)
                return 0;
    }
    
    return 1;
}

inline void fillx(vvi &V, int x, int M) {
    for (int y = 0; y < M; y++)
        V[x][y] = 1;
}

inline void filly(vvi &V, int N, int y) {
    for (int x = 0; x < N; x++)
        V[x][y] = 1;
}


int naive(vvi &B, int N, int M) {
    int x, y;
    
    vvi V(N, vi(M, 0));
    
    for (int i = 1; i <= 100; i++) {
        for (x = 0; x < N; x++) {
            
            for (y = 0; y < M; y++) {
                if (V[x][y] == 0 && B[x][y] != i)
                    break;
            }
            
            if (y == M) {
                fillx(V, x, M);
            }
        }
        
        for (y = 0; y < M; y++) {
            
            for (x = 0; x < N; x++) {
                if (V[x][y] == 0 && B[x][y] != i)
                    break;
            }
            
            if (x == N) {
                filly(V, N, y);
            }
        }
    }
    
    //printB(B, N, M);
    //printB(V, N, M);
    return check(V, N, M);
}

int main(void) {
	
	int x, y, z;
	int numCases;
	unsigned int i, j, k;
	
	scanf("%d", &numCases);
	for (int T = 1; T <= numCases; T++) {
        int N, M;
        scanf("%d%d", &N, &M);
		vvi L(N, vi(M));
        
        
        for (int x = 0; x < N; x++)
            for (int y = 0; y < M; y++)
                scanf("%d", &L[x][y]);
        
        int ck = naive(L, N, M);
        printf("Case #%d: %s\n", T, (ck ? "YES": "NO"));
	}

	return 0;
}