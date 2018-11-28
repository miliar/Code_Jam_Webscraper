#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <list>
#include <queue>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <sstream>
#include <bitset>
#include <set>



using namespace std;




int main()
{
	freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);

    int T,cased=0;
    cin>>T;
    while(T--)
    {
        long A, B, K; cin>>A>>B>>K;
        long long  cnt=0;
        for(long i=0; i<A; i++){
            for(long j=0; j<B; j++){
                long c = i&j;
                if(c<K){
                    cnt++;
                }
            }
        }
       printf("Case #%d: %lld\n",++cased,cnt);
    }
    return 0;
}





