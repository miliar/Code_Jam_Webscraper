#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define pb push_back
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 1000
using namespace std;

int T, first, second, n, cards[16], num_cards_matched, card_num;

int main()
{
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
    	REP(i, 0, 15) cards[i] = 0;
    	num_cards_matched = 0;
    	card_num = -1;
    	scanf("%d", &first);
    	REP(i, 1, 4) {
    		REP(j, 1, 4) {
    			scanf("%d", &n);
    			if(i == first) {
    				cards[n-1] = 1;
    			}
    		}
    	}

    	scanf("%d", &second);
    	REP(i, 1, 4) {
    		REP(j, 1, 4) {
    			scanf("%d", &n);
    			if(i == second) {
    				if(cards[n-1]) {
    					num_cards_matched++;
    					card_num = n;
    				}
    			}
    		}
    	}

    	printf("Case #%d: ", t);

    	if(!num_cards_matched) {
    		printf("Volunteer cheated!\n");
    	} else if(num_cards_matched == 1) {
    		printf("%d\n", card_num);
    	} else {
    		printf("Bad magician!\n");
    	}
    }
    return 0;
}
