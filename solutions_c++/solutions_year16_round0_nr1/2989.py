#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define ll long long int
#define ss(n) scanf("%lld", &n)
#define ssf(n) scanf("%lf", &n)
#define gc getchar
#define pb push_back
using namespace std;
int main()
{
    ll t, n, k, j=1, cnt, num, i;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    bool sleep, flag[10];
    in>>t;
    while(j<=t)
    {
        in>>n;
        for(i=0;i<10;i++)
            flag[i]=false;
        out<<"Case #"<<j<<": ";
        if(n==0)
        {
            out<<"INSOMNIA\n";
            j++;
            continue;
        }
        sleep=false;
        i=1;
        cnt=0;
        while(!sleep)
        {
            num=n*i;
            while(num)
            {
                if(!flag[num%10])
                {
                    cnt++;
                    flag[num%10]=true;
                }
                num/=10;
            }
            i++;
            if(cnt==10)
                sleep=true;
        }
        num=n*(i-1);
        out<<num<<endl;
        j++;
    }
}
