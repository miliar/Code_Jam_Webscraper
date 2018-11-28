//author: CHC
//First Edit Time:	2014-04-13 00:46
//Last Edit Time:	2014-04-13 01:20
//Filename:1.cpp
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--){
        int a[5][5],b[5][5],ha[100]={ 0 };
        int ans1,ans2;
        int flag=0,num;
        memset(ha,0,sizeof(ha));
        scanf("%d",&ans1);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++){
            scanf("%d",&a[i][j]);
            if(i==ans1)ha[a[i][j]]=1;
        }
        scanf("%d",&ans2);
        for(int i=1;i<=4;i++){
        for(int j=1;j<=4;j++){
            scanf("%d",&b[i][j]);
            if(i==ans2){
                if(ha[b[i][j]]){
                    ++flag;
                    num=b[i][j];
                }
            }
        }
        }
        printf("Case #%d: ",++cas);
        if(flag==0)puts("Volunteer cheated!");
        else if(flag==1)printf("%d\n",num);
        else puts("Bad magician!");
    }
    return 0;
}
