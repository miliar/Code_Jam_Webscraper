#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <fstream>
#include <set>
#include <map>
#include <cmath>
#pragma comment(linker,"/STACK:16777216")

using namespace std;

bool a[10000];

int t,x,b,say;

int main()
{
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    a[1]=1;
    a[4]=1;
    a[9]=1;
    a[121]=1;
    a[484]=1;
    
    scanf("%d",&t);
    
    for(int o=1;o<=t;o++)
        {
            say=0;
            scanf("%d%d",&x,&b);
            for(int i=x;i<=b;i++)
                if(a[i]==1)
                    say++;
            printf("Case #%d: %d\n",o,say);
            
        }
    
    
    return 0;
}
