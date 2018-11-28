#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int N, x;
int main(){
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%d", &N);
        vector<int>v;
        for(int i = 0; i < N; i++){
                scanf("%d", &x);
                v.push_back(x);
        }
        int id = 0;
        for(int i = 0; i < N; i++)
            if(v[i] > v[id])id = i;
        int ans = 1000000000;
        for(int mask = 0; mask < (1<<N); mask++){
            vector<int> a, b =v, c ;
            int swaps = 0;
            int x = mask | (1<<id);
            for(int i = 0; i < N; i++){
                if( (x>>i) & 1)a.push_back(v[i]);
                else c.push_back(v[i] );
            }
            sort(a.begin(), a.end() );
            sort(c.begin(), c.end() );
            reverse(c.begin(), c.end());

            for(int i = 0; i < a.size(); i++){
                int y = -1;
                for(int j = 0; j < N ; j++)
                    if(b[j] == a[i])y =j;
                while(y > i){
                    swap(b[y], b[y - 1]);
                    swaps++, y--;
                }
            }
            for(int i = 0; i < c.size(); i++){
                int y = -1;
                for(int j = 0; j < N ; j++)
                    if(b[j] == c[i])y =j;
                while(y > 0 && b[y] > b[y - 1]){
                    swap(b[y], b[y - 1]);
                    y--, swaps++;
                }
            }
            ans = min(ans, swaps);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
