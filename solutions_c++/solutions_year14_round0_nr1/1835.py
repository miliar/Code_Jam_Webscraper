/*@author: c0d3_k1ra
 *
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>
#include <map>
#include <string>
#include <climits>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <ctime>
using namespace std;
typedef long int int64;
typedef long long int int64l;
typedef unsigned long long uint64l;
typedef unsigned long uint64;
inline void scanint(int *a)
{
    char c = 0;int sign=1;
    while(c<33)
       // c = fgetc_unlocked(stdin);
    c = getc(stdin);

    *a = 0;
    while(c>33)
    {
        if(c=='-'){ sign=-1;
        c = getc(stdin);
        //c = fgetc_unlocked(stdin);
        continue;}
        *a = *a*10 + c - '0';
       // c = fgetc_unlocked(stdin);
    c = getc(stdin);
    }
    *a=*a * sign;
    //printf("%d\n",*a);
}
char outputbuf[20];

inline void putint(int n)
{
	outputbuf[19]='\n';
    bool flag=false;int i=18,r;
    if(n<0){ flag=true; n*=-1;}
    while(n!=0)
    {
        r=n%10;
        outputbuf[i--]=r+'0';
        n/=10;
    }
    if(flag) outputbuf[i--]='-';
    i++;
    while(i<20)
    {
        //putchar_unlocked(outputbuf[i++]);
        putc(outputbuf[i++],stdout);
    }
}
int main()
{
    int t,i,j,ans1,ans2,cnt,val,k;
    scanint(&t);
    for(k=1;k<=t;++k)
    {
        int arr1[4][4],arr2[4][4];
        scanint(&ans1);
        ans1--;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
                scanint(&arr1[i][j]);
        scanint(&ans2);
        ans2--;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
                scanint(&arr2[i][j]);
        cnt=0;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            {
                if(arr1[ans1][i]==arr2[ans2][j])
                {
                    cnt++;
                    val=arr1[ans1][i];
                }
            }
        }
        printf("Case #%d: ",k);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if(cnt>1) printf("Bad magician!\n");
        else if(cnt==1) printf("%d\n",val);
    }
    return 0;
}
