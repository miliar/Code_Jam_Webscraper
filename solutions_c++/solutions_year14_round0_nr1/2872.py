#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int data[4][4];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--)
    {
        bool ifv[17];
        memset(ifv,false,sizeof ifv);
        int k;
        cin>>k;
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
            cin>>data[i][j];
        for (int i=0;i<4;++i) ifv[data[k-1][i]]=true;
         cin>>k;
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
            cin>>data[i][j];
        int cnt=0,ans;
        for (int i=0;i<4;++i)
            if (ifv[data[k-1][i]]) {++cnt;ans=data[k-1][i];}
        printf("Case #%d: ",++cas);
        if (cnt==1) printf("%d\n",ans);
        if (cnt>1) printf("Bad magician!\n");
        if (cnt==0) printf("Volunteer cheated!\n");
    }
}
