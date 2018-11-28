#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define SZ(a) (int)a.size()
#define dd double

int grid[17][17];
int rec(int r,int c,int n)
{
    int ret = -1;
    for(int i = 0 ; i<1<<(r*c) ; i++)
    {
        if(__builtin_popcount(i)==n)
        {
            int cnt = 0;
            for(int j = 0; j<r ; j++)
            {
                for(int k = 0 ; k<c ; k++)
                {
                    if(i&(1<<(j*c + k)))
                    {
                        int l = 0 , m = -1;
                        if(j+l>=0 && j+l<r && k+m>=0 && k+m<c)
                        {
                            if(i&(1<<((j+l)*c + k+m))) cnt++;
                        }

                        l = -1 , m = 0;
                        if(j+l>=0 && j+l<r && k+m>=0 && k+m<c)
                        {
                            if(i&(1<<((j+l)*c + k+m))) cnt++;
                        }
                    }
                }
            }

            if(ret==-1 || ret>cnt) ret = cnt;
        }
    }
    return ret;
}


ll test(int r,int c,int n)
{
     ll tot = ((r+1)/2LL)*( (c+1)/2LL);
    tot += ((r)/2LL)*( (c)/2LL);

    ll sol = 0;

    if(tot>=n)
        sol = 0;
    else
    {
        ll rem = n-tot;
        int con = 0;
        if( !(r&1) || !(c&1)) con = 2;


        if(con>=rem)
        {
            sol = rem*2;
        }
        else
        {
            rem = rem-con;
            sol += con*2;

            ll val3 = ((r+1)/2LL) + ( (c+1)/2LL) - con;

            if(rem<= val3)
                sol += rem*3;
            else
            {
                sol += val3*3;
                rem = rem-val3;
                sol += rem*4;
            }
        }
    }
}
int main()
{
    freopen("B-small-attempt0.in" , "r" , stdin);
    freopen("B-small-attempt0.out" , "w+" , stdout);

    int tcase,cas=1;

    cin>>tcase;

    while(tcase--)
    {
        int r,c;
        int n;
        cin>>r>>c>>n;



        cout<<"Case #"<<cas++<<": "<<rec(r,c,n)<<endl;
    }
    return 0;
}

