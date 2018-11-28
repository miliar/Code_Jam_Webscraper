#include<stdio.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<set>
#include<iostream>
using namespace std;

#define S(x) scanf("%d",&x)
#define St(x) scanf("%s",x)
#define P(x) printf("%d\n",x)
#define Ps(x) printf("%s\n",x)
#define P1(x) printf("%lld\n",x)
#define Pt(x) printf("%d ",x)
#define Y printf("YES\n")
#define N printf("NO\n")
#define mod 1000000009
int abs(int x){return x<0?-x:x;}
int main()
{
    int t;
    cin>>t;
    int a=t;
    while(t--)
    {
        int i,j,k,p,count=0,d;
        cin>>k;
        int arr[4][4];
        int brr[16];
        for(i=0;i<16;i++)
            brr[i]=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>arr[i][j];
        }
        for(j=0;j<4;j++)
        {
            brr[arr[k-1][j]-1]++;
            //cout<<arr[k-1][j]<<'\n';
        }
        cin>>d;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>arr[i][j];
        }
        for(j=0;j<4;j++)
        {
           //  cout<<arr[d-1][j]<<'\n';

            if(brr[arr[d-1][j]-1]!=0)
            {
                p=arr[d-1][j];

                count++;
            }
        }
        if(count==1)
            cout<<"Case #"<<(a-t)<<": "<<p<<'\n';
            else if(count==0)
            cout<<"Case #"<<(a-t)<<": "<<"Volunteer cheated!"<<'\n';
            else if(count>1)
            cout<<"Case #"<<(a-t)<<": "<<"Bad magician!"<<'\n';

        }
        return 0;
        }

