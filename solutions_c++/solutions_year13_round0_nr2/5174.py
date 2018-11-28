#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<list>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<iterator>
#include<algorithm>
#include<stack>
#include<queue>
using namespace std;

int n,m,a[100][100];
int search(int i,int j)
{
    int r=1,c=1;
    while(j+c<m || j-c>=0)
    {
        if(j+c<m&&a[i][j+c]>a[i][j])
                break;
        if(j-c>=0&&a[i][j-c]>a[i][j])
            break;
        c++;
    }
    if(j+c>=m && j-c<0)
        return 1;
    while(i+r<n || i-r>=0)
    {
        if(i+r<n&&a[i+r][j]>a[i][j])
            break;
        if(i-r>=0&&a[i-r][j]>a[i][j])
            break;
        r++;
    }
    if(i+r>=n && i-r<0)
        return 1;
    return 0;
}
int judge()
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(!search(i,j))
                return 0;
    return 1;
}
int main()
{
    int t,cas=1;;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        printf("Case #%d: ",cas++);
        int ans=judge();
        if(ans==0)
            printf("NO\n");
        else
            printf("YES\n");
    }
    return 0;
}
