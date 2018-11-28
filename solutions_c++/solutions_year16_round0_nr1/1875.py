#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int T; scanf("%d", &T);
    for(int ti=1;ti<=T;ti++){
        printf("Case #%d: ", ti);
        int n; scanf("%d", &n);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }
        int s = 0;
        vector<bool> has_seen(10, false);
        while(!all_of(has_seen.begin(), has_seen.end(), [](bool x){return x;})){
            s += n;
            int t = s;
            while(t > 0){
                has_seen[t%10] = true;
                t /= 10;
            }
        }
        printf("%d\n", s);
    }
    return 0;
}
