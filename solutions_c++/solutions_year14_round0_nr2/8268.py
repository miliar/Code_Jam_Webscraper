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
#pragma comment(linker,"/STACK:116777216")
#define MAXN 100100

using namespace std;

int t;

int used;

double c,f,x,ans,z,ans1,w;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>t;

    for(int o=1;o<=t;o++)
    {



        cin>>c>>f>>x;

        z=2.0;

        ans=x/z;

        ans1=0;

        while(ans1<ans)
            {
                w=c/z;
                z=z+f;
                ans1+=w;

                if(ans>ans1+x/z)
                    ans=ans1+x/z;
            }

        printf("Case #%d: ",o);
        //cout<<ans<<endl;
        printf("%.7lf\n",ans);
    }



    return 0;
}
