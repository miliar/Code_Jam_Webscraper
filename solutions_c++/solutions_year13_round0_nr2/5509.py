#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<iostream>
#include<deque>

#define inf 1000000000

using namespace std;

int main()
{
int t, n, m, tab[100][100], done[100][100], poss, temp;
scanf("%d", &t);
for(int i=1; i<=t; i++)
{
    scanf("%d%d", &n, &m);
    for(int j=0; j<n; j++)
        for(int k=0; k<m; k++)
            scanf("%d", &tab[j][k]);
    for(int j=0; j<n; j++)
        for(int k=0; k<m; k++)
            done[j][k]=false;
    for(int j=0; j<n; j++)
    {
        poss=true;
        temp=0;
        for(int k=0; k<m; k++)
            temp=max(temp,tab[j][k]);
        for(int k=0; k<m; k++)
            if(temp==tab[j][k])
                done[j][k]=true;
    }
    for(int k=0; k<m; k++)
    {
        poss=true;
        temp=0;
        for(int j=0; j<n; j++)
            temp=max(temp,tab[j][k]);
        for(int j=0; j<n; j++)
            if(temp==tab[j][k])
                done[j][k]=true;
    }
    /*for(int j=0; j<n; j++|printf("\n"))
        for(int k=0; k<m; k++)
            printf("%d ", done[j][k]);
            */
    poss=true;
    for(int j=0; j<n; j++)
        for(int k=0; k<m; k++)
            if(!done[j][k])
                poss=false;
    if(poss)
        printf("Case #%d: YES\n", i);
    else
        printf("Case #%d: NO\n", i);

}
return 0;
}
