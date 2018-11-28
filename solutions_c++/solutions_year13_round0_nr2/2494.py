#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>
using namespace std;
int main()
{
ifstream cin ("B-large.in");
ofstream cout ("progout2.out");
int n,m,t,i,j,counter=0;
cin>>t;
while(t--)
{
    counter++;
    cin>>n>>m;
    int arr[n][m],small[n];
    for(i=0;i<n;i++)
    {
        small[i]=101;
        for(j=0;j<m;j++)
        {
            cin>>arr[i][j];
            small[i]=min(arr[i][j],small[i]);

        }
    }
    int p1,p2;
    bool check3=0;
    for(i=0;i<n;i++)
    {
        bool check1=0,check2=0;
        for(j=0;j<m;j++)
        {
            check1=0;check2=0;
                for(p1=0;p1<m;p1++)
                {
                    if(arr[i][p1]>arr[i][j]){check1=1;break;}

                }
                for(p2=0;p2<n;p2++)
                {
                    if(arr[p2][j]>arr[i][j]){check2=1;break;}
                }
            if(check1&&check2){check3=1;break;}
        }
        if(check1&&check2)break;
    }
    if(check3)
    {
        cout<<"Case #"<<counter<<": NO\n";
    }
    else
    {
        cout<<"Case #"<<counter<<": YES\n";
    }
}
return 0;
}
