#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str)
{
    int ans;
    stringstream s;
    s<<str;
    s>>ans;
    return ans;
}
string intToStr(int n)
{
    string str;
    stringstream s;
    s<<n;
    s>>str;
    return str;
}
int MAX(int a,int b)
{
    if(a >b) return a;
    return b;
}
int MIN(int a,int b)
{
    if(a <b) return a;
    return b;
}
int ABS(int a,int b)
{
    if(a >0) return a;
    return -a;
}

int arr[105][105], lawn[105][105];
int row[105], col[105];

void print(int n,int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            printf("%d",arr[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    freopen("BlargeInput.txt","r",stdin);
    freopen("BlargeOutput.txt","w",stdout);
    int test;
    scanf("%d",&test);
    int n,m;

    for(int k=1; k<=test; k++)
    {
        scanf("%d %d",&n,&m);
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                scanf("%d",&arr[i][j]);

            }
        }
//    if(k!=7) continue;
//    if(k==7)
//    {
//        print(n,m);
//    }
    bool flag = true;
    for(int i=0;i<n;i++)
    {   row[i]=-1;
        for(int j=0;j<m;j++)
        {
            row[i] = MAX(row[i],arr[i][j]);
        }
    }

    for(int j=0;j<m;j++)
    {
        col[j]=-1;
        for(int i=0;i<n;i++)
        {
            col[j] = MAX(col[j], arr[i][j]);
        }
    }
//    printf("\n\n");
//    for(int i=0;i<n;i++)
//    {
//        printf("%d",row[i]);
//    }
//    printf("\n");
//    for(int j=0;j<m;j++)
//    {
//        printf("%d",col[j]);
//    }
//    printf("\n");
//    printf("\n");
    flag = true;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if((arr[i][j]>=row[i]) || (arr[i][j]>=col[j]))
                ;
            else
            {
                flag = false;
                break;
            }
        }
    }
        if(flag)
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);

    }


    return 0;
}



