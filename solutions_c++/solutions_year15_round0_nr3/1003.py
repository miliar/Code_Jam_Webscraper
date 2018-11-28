/**
country:China
Author:JiaYang Lee
Language:c++
Date:2015-04-12
School:SCAU
*/
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 10500;
const int inf = 1e9+7;
const int mod = 1e9+7;
typedef long long ll;

/**
index:
0   1   2   3   4   5   6   7
-1  1   i   -i  j  -j   k   -k
*/

int cas=1;
int len;
ll k;
char ch[N],str[N*16];
const int matrix[8][8]={{1,0,3,2,5,4,7,6},
                        {0,1,2,3,4,5,6,7},
                        {3,2,0,1,6,7,5,4},
                        {2,3,1,0,7,6,4,5},
                        {5,4,7,6,0,1,2,3},
                        {4,5,6,7,1,0,3,2},
                        {7,6,4,5,3,2,0,1},
                        {6,7,5,4,2,3,1,0},
                        };

int Encode(char c)
{
    if(c=='1')return 1;
    if(c=='i')return 2;
    if(c=='j')return 4;
    return 6;
}

void repeat(char *ch,char *str,int times)
{
    for(int i=0;i<len*times;i++)
        str[i]=ch[i%len];
    str[len*times]=0;
}

int find_i(char *str)
{
    int cur=1;
    for(int i=0;str[i];i++)
    {
        cur=matrix[cur][Encode(str[i])];
        if(cur==Encode('i'))return i;
    }
    return -1;
}

int find_k(char *str)
{
    int cur=1,len=strlen(str);
    for(int i=len-1,j=0;i>=0;i--,j++)
    {
        cur=matrix[Encode(str[i])][cur];
        if(cur==Encode('k'))return j;
    }
    return -1;
}

bool is_ijk(char *str,ll times)
{
    int cur=1;
    for(int i=0;str[i];i++)
        cur=matrix[cur][Encode(str[i])];
    if(cur==0)return times&1ll;
    if(cur==1)return false;
    if(times&1ll)return false;
    times>>=1;
    return times&1ll;
}

void solve()
{

    scanf("%d%I64d%s",&len,&k,ch);
    printf("Case #%d: ",cas++);
    if(!is_ijk(ch,k))
    {
        puts("NO");
        return;
    }
    if(k>=16)
        repeat(ch,str,16);
    else
        repeat(ch,str,k);
    ll index_i,index_k;
    index_i=find_i(str);
    if(index_i==-1)
    {
        puts("NO");
        return;
    }
    index_k=find_k(str);
    if(index_k==-1)
    {
        puts("NO");
        return;
    }
    ll id=len*k-index_k-1;
    if(index_i>=id)
    {
        puts("NO");
        return;
    }
//    printf("i=%I64d,k=%I64d\n",index_i,id);
    puts("YES");
}

int main()
{
#ifdef LOCAL
    freopen("in","r",stdin);
    freopen("out","w",stdout);
#endif // LOCAL
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
    return 0;
}
