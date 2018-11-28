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
int main()
{
   // freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
    freopen("outputtbcc.txt","w",stdout);
    int test;
    int n,ans,temp,c,k,start,end;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        cin>>s;
        printf("Case #%d: ",t+1);
        int n=strlen(s);
        for(int i=0;i<=9;i++)
            cnt[i]=0;
        for(int i=0;i<n;i++)
            visit[i]=0;
        for(int i=0;i<=9;i++)
        {
            if(search(f[y[i]],x[i],n))
            {
                cnt[y[i]]++;
                i--;
            }
        }
        for(int i=0;i<=9;i++)
        {
            for(int j=0;j<cnt[i];j++)
                cout<<i;
        }
        cout<<endl;
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
