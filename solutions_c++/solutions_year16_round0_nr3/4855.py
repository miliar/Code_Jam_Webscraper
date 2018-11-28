#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define N 123456

long long number( string str, int base)
{
    long long addpower=1,num=0;
    for( int i=str.length()-1; i>=0; i-- )
    {
        if( str[i]=='1')
            num += addpower;
        addpower *= base;
    }
    return num;
}

long long isprime( long long n)
{
    for( long long int i=2; i*i<=n; i++ )
    {
        if( n%i==0 ) {
            return i;
        }
    }
    return -1;
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for( int tt=1 ; tt<=t ; tt++ )
    {
        int n,x;
        scanf("%d %d",&n,&x);


        vector < string > arr;
        vector < long long > ans[x];
        string str="";

        for( int i=0; i<n; i++ )
            str.pb('0');

        string cur="";
        for( int i=1; i<(1<<n); i++ )
        {
            if( arr.size()==x )
                break;
            cur=str;
            for( int j=0; j<n ; j++ )
                if((i&(1<<j)))
                 cur[j]='1';

            if( cur[0]=='1' && cur[n-1]=='1' )
            {
                bool flag=true;
                vector < long long > cur_arr;

                for( int i=2; i<=10; i++ )
                {
                    long long z=isprime(number(cur,i));
                    if( z==-1 )
                        flag=false;
                    cur_arr.pb(z);
                }
                if( flag==true )
                {
                    int counter=arr.size();
                    arr.pb(cur);
                    ans[counter]=cur_arr;
                }
            }
        }
        printf("Case #%d:\n",tt);

        for( int i=0; i<x ; i++ )
        {
            cout << arr[i] <<" ";
            for( int j=0 ; j<ans[i].size(); j++ )
                printf("%d ",ans[i][j]);
            printf("\n");
        }
    }

    return 0;
}

