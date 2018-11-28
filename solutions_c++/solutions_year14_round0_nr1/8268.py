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

int t,n,m,v[17],a[5][5],ans;

int used;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>t;

    for(int o=1;o<=t;o++){
        ans=0;
        used=0;
        cin>>n;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            cin>>a[i][j];

        for(int i=1;i<=4;i++)
            v[a[n][i]]++;

        cin>>n;

        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            cin>>a[i][j];

        for(int i=1;i<=4;i++)
            v[a[n][i]]++;

        for(int i=1;i<=16;i++){
            if(v[i]==2 && used==1)
            {
                used=2;
                //cout<<i<<" ma"<<endl;
                break;
            }
            if(v[i]==2 && used==0){
                used=1,ans=i;
            //cout<<i<<" xa"<<endl;
            }

        }

        printf("Case #%d: ",o);

        if(used==0)
            printf("Volunteer cheated!\n");
        if(used==2)
            printf("Bad magician!\n");
        if(used==1)
            printf("%d\n",ans);

        memset(v,0,sizeof(v));
    }

    return 0;
}
