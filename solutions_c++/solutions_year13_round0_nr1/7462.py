#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define eps 1e-8
#define DEBUG(a) cout<<#a" = "<<(a)<<endl;
#define DEBUGARR(a,n) for(int i=0;i<(n);i++) {cout<<#a"["<<i<<"] = "<<(a)[i]<<endl;}
#define pi acos(-1.0)
using namespace std;
int main()
{
    #ifdef StyleTang_Code
    freopen("123.in","r",stdin);
    freopen("123.out","w",stdout);
    #endif
    int t;
    string str[4];
    int i,j,k;
    cin>>t;
    for(int index=1;index<=t;index++)
    {
        for(i=0;i<4;i++)
        cin>>str[i];
        bool flag[3];
        flag[2]=flag[0]=flag[1]=false;
        bool temp;
        for(i=0;i<4;i++)
        {
            temp=true;
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='.')
                flag[2]=true;
                if(str[i][j]=='X'||str[i][j]=='T')
                continue;
                temp=false;
            }
            flag[0]=flag[0]|temp;
        }
                for(i=0;i<4;i++)
        {
            bool temp=true;
            for(j=0;j<4;j++)
            {
                if(str[j][i]=='X'||str[j][i]=='T')
                continue;
                temp=false;
            }
            flag[0]=flag[0]|temp;
        }
                for(i=0;i<4;i++)
        {
            bool temp=true;
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='O'||str[i][j]=='T')
                continue;
                temp=false;
            }
            flag[1]=flag[1]|temp;
        }
                for(i=0;i<4;i++)
        {
            bool temp=true;
            for(j=0;j<4;j++)
            {
                if(str[j][i]=='O'||str[j][i]=='T')
                continue;
                temp=false;
            }
            flag[1]=flag[1]|temp;
        }
        temp=true;
        for(i=0;i<4;i++)
        {
            if(str[i][i]=='X'||str[i][i]=='T')
            continue;
            temp=false;
        }
        flag[0]=flag[0]|temp;
        temp=true;
        for(i=0;i<4;i++)
        {
            if(str[i][i]=='O'||str[i][i]=='T')
            continue;
            temp=false;
        }
        flag[1]=flag[1]|temp;
        temp=true;
        for(i=0;i<4;i++)
        {
            if(str[i][3-i]=='X'||str[i][3-i]=='T')
            continue;
            temp=false;
        }
        flag[0]=flag[0]|temp;
        temp=true;
        for(i=0;i<4;i++)
        {
            if(str[i][3-i]=='O'||str[i][3-i]=='T')
            continue;
            temp=false;
        }
        flag[1]=flag[1]|temp;
        if(flag[0]&&flag[1])
        {
            printf("Case #%d: Draw\n",index);
            continue;
        }
        if(flag[0])
        {
            printf("Case #%d: X won\n",index);
            continue;
        }
        if(flag[1])
        {
            printf("Case #%d: O won\n",index);
            continue;
        }
        if(flag[2])
        printf("Case #%d: Game has not completed\n",index);
        else
        printf("Case #%d: Draw\n",index);
    }
	return 0;
}
