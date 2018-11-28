#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>
//0为平手，1为X胜，2为O胜，3为未完成 
using namespace std;
char mapt[5][5];
int fun(int s1,int s2,int t)
{
    int i,j;
    //判断未完成 
    if(s1+t<4&&s2+t<4) return 3;
    //判断一行 
    for(i=0;i<4;i++)
    {
        int cnt1 = 0,cnt2 = 0;
        for(j=0;j<4;j++)
        {
            if(mapt[i][j]=='X'||mapt[i][j]=='T') cnt1++;
            if(mapt[i][j]=='O'||mapt[i][j]=='T') cnt2++;
        }    
        if(cnt1==4) return 1;
        if(cnt2==4) return 2;
    }   
    //判断一列 
    for(j=0;j<4;j++)
    {
        int cnt1 = 0,cnt2 = 0;
        for(i=0;i<4;i++)
        {
            if(mapt[i][j]=='X'||mapt[i][j]=='T') cnt1++;
            if(mapt[i][j]=='O'||mapt[i][j]=='T') cnt2++;
        }    
        if(cnt1==4) return 1;
        if(cnt2==4) return 2;
    }
    //判断反斜着 
    int cnt1 = 0,cnt2 = 0;
    for(i=0;i<4;i++)
    {
        
        j=i;
        if(mapt[i][j]=='X'||mapt[i][j]=='T') cnt1++;
        if(mapt[i][j]=='O'||mapt[i][j]=='T') cnt2++;
    }    
    if(cnt1==4) return 1;
    if(cnt2==4) return 2;
    //判断斜 
    cnt1 = 0,cnt2 = 0;
    for(i=0;i<4;i++)
    {
        j=3-i;
        if(mapt[i][j]=='X'||mapt[i][j]=='T') cnt1++;
        if(mapt[i][j]=='O'||mapt[i][j]=='T') cnt2++;
    }    
    if(cnt1==4) return 1;
    if(cnt2==4) return 2; 
    //平局draw 
    if(s1+s2+t<16) return 3;
    return 0;
}    
int main()
{
    freopen("A-large.in","r",stdin); 
    freopen("A-large.out","w",stdout);
    int n;
    int s1,s2,i,j,t,l=1;
    scanf("%d",&n);
    
    while(n--)
    {
        s1=0;s2=0;t=0;
        for(i=0;i<4;i++) 
        {
            scanf("%s",mapt[i]);    
        }
        for(i=0;i<4;i++) 
        {
            for(j=0;j<4;j++)
            {
                if(mapt[i][j]=='X') s1++;
                else if(mapt[i][j]=='O') s2++;
                else if(mapt[i][j]=='T') t++;
            }    
        }    
        //printf("%d,%d,%d\n",s1,s2,t);
        int k = fun(s1,s2,t);
        if(k==0) printf("Case #%d: Draw\n",l++);
        else if(k==1) printf("Case #%d: X won\n",l++);
        else if(k==2) printf("Case #%d: O won\n",l++);
        else if(k==3) printf("Case #%d: Game has not completed\n",l++);
    }       
    return 0;
}

