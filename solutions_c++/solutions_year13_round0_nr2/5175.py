#include<stdio.h>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define vvi vector<vector<int> >
#define pii pair<int,int>
#define vpii vector< vector<pair<int,int> > >
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define ABS(a) (a<0?-1*(a):a)
#define pi 2 * acos (0.0)


using namespace std;
int n,m,a[100][100],b[100][100];

bool check_row(int x,int y)
{
    for(int i=0;i<m;i++)
        if(a[x][i]>y)  return false;
    return true;
}
bool check_col(int x,int y)
{
    for(int i=0;i<n;i++)
        if(a[i][x]>y)  return false;
    return true;
}
int main()
{
    int tcase,i,j,co=1;
    //freopen("B-large.in","r",stdin);
    //freopen("out_B.txt","w",stdout);
    cin>>tcase;
    bool flag;
    while(tcase--)
    {
        cin>>n>>m;
        vector<pair<int,int> >v[110];
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                cin>>a[i][j];
                v[a[i][j]].push_back(make_pair(i,j));
            }
        }
        flag=true;
        for(i=1;i<=100;i++)
        {
            int t=v[i].size();
            if(t)
            {
                for(j=0;j<t;j++)
                {
                    int x=v[i][j].first;
                    int y=v[i][j].second;
                    if(!check_row(x,i)&&!check_col(y,i))
                    {
                        flag=false;
                        break;
                    }
                }
            }
            if(!flag)   break;
        }
        printf("Case #%d:",co++);
        if(flag)    printf(" YES\n");
        else    printf(" NO\n");
    }
    return 0;
}
