#include <iostream>
#include<stdio.h>
#include<string.h>
#include<bitset>
#include<vector>
# define ll long long int
using namespace std;

ll power(ll x, ll y)
{
    ll temp;
    if( y == 0)
       return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
    {
        if(y > 0)
            return x*temp*temp;
        else
            return (temp*temp)/x;
    }
}
char s[2005];
int visit[2005];
vector<int>pos;
int search(char a[12],char b[12],int n)
{
    int i,j,z=strlen(a);
    for( i=0;i<z;i++)
    {
        for( j=0;j<n;j++)
        {
            if(s[j]==a[i] && !visit[j])
            {
                pos.push_back(j);
                 break;
            }
        }
        if(j==n)
            {
                pos.clear();
                return 0;
            }
    }
    if(i==z)
    {
        for(int h=0;h<pos.size();h++)
            visit[pos[h]]=1;
        pos.clear();
        return 1;
    }
}
char f[12][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char x[12][10]={"Z","W","U","X","G","O","T","F","S","N"};
char y[10]={0,2,4,6,8,1,3,5,7,9};
int cnt[10];
int a[100];
int main()
{
   // freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
    freopen("outputtbcc.txt","w",stdout);
    int test;
    int n,ans,first,second,pos1,pos2,temp,c,k,start,end;
    cin>>test;
    int sum;
    for(int t=0;t<test;t++)
    {
        cin>>n;
        printf("Case #%d: ",t+1);
        sum=0;
        for(int i=0;i<n;i++)
        {
           cin>>a[i];
           sum+=a[i];
        }
        while(sum>0)
        {
        first=-1,second=pos1=pos2=-1;
        for(int i=0;i<n;i++)
        {
            if(a[i]>first && a[i]>second)
                second=first,pos2=pos1,first=a[i],pos1=i;
            else if(a[i]>second)
                second=a[i],pos2=i;
        }
        if(sum==3 && first==1 && second==1)
          {
             cout<<char(pos1+65)<<" ";
             sum-=1;
             a[pos1]--;
             continue;
          }
        sum-=2;
         if(sum!=-1)
        {
            cout<<char(pos1+65)<<char(pos2+65)<<" ";
            a[pos1]--;a[pos2]--;
        }
        else
            cout<<char(pos1+65)<<" ";
        }
        cout<<endl;
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
