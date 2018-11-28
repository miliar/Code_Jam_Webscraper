#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int N = 210;
const int M = 1000000;
const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;

typedef long long ll;

int flag[20];
int row;

int main(){
    int _, cases = 1;
    for(cin >> _; _--; ){
        printf("Case #%d: ", cases++);
        memset(flag, 0, sizeof(flag));
        scanf("%d", &row);
        for(int i = 0; i < 4; ++i)
            for(int j = 0, x; j < 4; ++j){
                scanf("%d", &x);
                if(row - 1 == i) flag[x]++;
            }
        scanf("%d", &row);
        for(int i = 0; i < 4; ++i)
            for(int j = 0, x; j < 4; ++j){
                scanf("%d", &x);
                if(row - 1 == i) flag[x]++;
            }
        vector<int> vec;
        for(int i = 1; i <= 16; ++i) if(flag[i] == 2) vec.push_back(i);
        if(vec.size() == 0) puts("Volunteer cheated!");
        else if(vec.size() > 1) puts("Bad magician!");
        else printf("%d\n", vec[0]);
    }
}