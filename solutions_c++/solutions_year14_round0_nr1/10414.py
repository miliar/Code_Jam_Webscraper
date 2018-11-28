
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <bitset>
#include <complex>
#include <cmath>
#include <ctime>
#include <cassert>
#define ll long long
using namespace std;
int main()
{
//    freopen("A-small-attempt2.in","r",stdin);
//    freopen("a.out","w",stdout);
    int casen;
    int t=1;
    for(scanf("%d",&casen);casen;casen--)
    {
        int a1[5],a2[5],a[4][4];
        int row1;
        scanf("%d",&row1);
        if(row1>4||row1<=0) {printf("Case #%d: Volunteer cheated!\n",t++);continue;}
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
        {
            scanf("%d",&a[i][j]);
            if(i==row1-1) a1[j]=a[i][j];
        }
        int row2;
        scanf("%d",&row2);
        if(row2>4||row2<=0) {printf("Case #%d: Volunteer cheated!\n",t++);continue;}
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
        {
            scanf("%d",&a[i][j]);
            if(i==row2-1) a2[j]=a[i][j];
        }
//        for(int i=0;i<4;i++)
//            cout<<a1[i]<<" ";
        int flag=0;
        int answer;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            if(a1[i]==a2[j])
        {
            flag++;
            answer=a1[i];
        }
        if(flag==1) {printf("Case #%d: %d\n",t++,answer);continue;}
        else if(flag==0) printf("Case #%d: Volunteer cheated!\n",t++);
        else if(flag>1) printf("Case #%d: Bad magician!\n",t++);
    }
    return 0;
}
