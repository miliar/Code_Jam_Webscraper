#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int t=0;t++<T;){
        int p;
        scanf("%d",&p);
        vector<int> pancakes;
        int output = 1000;
        for(int i = 0; i < p; ++i){
            int tmp;
            scanf("%d", &tmp);
            pancakes.push_back(tmp);
        }
        sort(pancakes.begin(),pancakes.end());
        output = pancakes.back();
        for(int i = 1; i < 1001; ++i){
            int specials = 0;
            for(int j = 0; j < pancakes.size(); j++){
                specials += (pancakes[j]-1) / i;
            }
            output = min(output,specials + i);
        }
        printf("Case #%d: %d\n", t, output);
    }
    return 0;
}
