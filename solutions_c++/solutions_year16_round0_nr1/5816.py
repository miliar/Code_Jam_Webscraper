#include <bits/stdc++.h>

using namespace std;
int cases = 1;
int main(void) {
    freopen("/home/vanessi/ClionProjects/HackerRankContest/Counting Sheep.in","r",stdin);
    freopen("/home/vanessi/ClionProjects/HackerRankContest/Counting Sheep.out","w",stdout);
    int t;scanf("%d",&t);
    while(t--){
        long long n,tar = 0;scanf("%lld",&n);tar = n;
        set<char> x;
        bool finish = false;
        for (int i = 0; i < 100000; ++i) {
            string xx = to_string(tar);
            for (int j = 0; j < xx.size(); ++j) {
                x.insert(xx[j]);
            }
            if(x.size()==10){
                finish = 1;
                break;
            }
            tar+=n;
        }
        if(finish)printf("Case #%d: %lld\n",cases++,tar);
        else printf("Case #%d: INSOMNIA\n",cases++);
    }
}