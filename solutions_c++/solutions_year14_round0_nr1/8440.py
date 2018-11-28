#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) cout << #x " is " << x << endl

using namespace std;

int main(){
    int cases;cin >> cases;
    for(int i=1; i<=cases; i++){
        int ansUser1; cin >> ansUser1; ansUser1--;
        int grid[4][4];
        set <int> auxGrid;
        for(int j=0; j<4; j++){
            for(int x=0; x<4; x++){
                int card; cin >> card;
                //D(card);
                if(ansUser1 == j) auxGrid.insert(card);
            }   
        }
        int ansUser2; cin >> ansUser2; ansUser2--;
        int posibleAns = 0;
        int ans = 0;
        int grid2[4][4];
        for(int j=0; j<4; j++){
            for(int x=0; x<4; x++){
                int card; cin >> card;
                if(ansUser2 == j) {
                    int posible = auxGrid.size();
                    auxGrid.insert(card);
                    if(posible == auxGrid.size()){
                        posibleAns++;   
                        ans = card;
                    }
                }
            }   
        }
        if(posibleAns == 0) printf("Case #%d: Volunteer cheated!\n",i);
        if(posibleAns == 1) printf("Case #%d: %d\n", i, ans);
        if(posibleAns > 1) printf("Case #%d: Bad magician!\n",i);
    }
	return 0;
}
