#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

typedef long long ll;

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int t=0;t++<T;){
        int N, X;
        scanf("%d%d", &N, &X);
        vector<int> F;
        for(int i=0; i<N;i++){
            int tmp;
            scanf("%d",&tmp);
            F.push_back(tmp);
        }
        sort(F.begin(),F.end());
        int ret = 0;
        while(F.size() != 0){
            if((F.front() + F.back()) <= X)
                F.erase(F.begin());
            if(F.size() != 0)
                F.pop_back();
            ret++;
        }
        printf("Case #%d: %d\n", t, ret);

    }
    return 0;
}
