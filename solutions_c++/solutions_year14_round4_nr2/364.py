#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;

#define inf  1000000000

int a[1024];
int b[1024];
int c[1024];
map<int,int> id;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int casT, cas=0;
    cin>>casT;
    while (T--)
    {
        cas++;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&a[i]);
            b[i]=a[i];
        }
        sort(b,b+N);
        id.clear();
        for(int i=0;i<N;i++)
        {
            id.insert(pair<int,int>(b[i],i));
        }
        for(int i=0;i<N;i++) c[i]=id[a[i]];
	int ans = 0;
	for(int x = 0 ; x<=N;x++) {
            auto id = find(v2.begin(), v2.end(), x);
	int b = v2.end()-id-1;
            int a = id-v2.begin();
            
            ans+= min(a,b);
            v2.erase(it);
        }
        printf("Case #%d: %d\n",cas,ans);


    }
	return 0;
}