#include <bits/stdc++.h>
/*#include <boost/multiprecision/cpp_int.hpp> */
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define gc getchar_unlocked
#define pp pair<int,int>
#define bigint boost::multiprecision::cpp_int
#define bsize 600
using namespace std;
ll t,l,x;

bool stat[4][9],stat2[4][9];

int mul(int a,int b)
{
    if(a==1 && b==1)return 1;
    if(a==b)return 5;
    int mul=0;
    if(a>4 && b<=4)mul=4;
    if(a<=4 && b>4)mul=4;
    if(a>4)a-=4;
    if(b>4)b-=4;

    if(a==1)return mul+b;
    if(b==1)return mul+a;
    if(a==b && mul==0)return 5;
    if(a==b && mul==4)return 1;

    if(a==2 && b==3)return mul+4;
    if(a==3 && b==4)return mul+2;

    if(a==4 && b==2)return mul+3;

    if(mul==0)mul=4;
    else mul=0;

    if(a==3 && b==2)return mul+4;
    if(a==4 && b==3)return mul+2;

    if(a==2 && b==4)return mul+3;
}

int main()
{
    cin>>t;

    for(int y=1;y<=t;y++)
    {
        memset(stat,false,sizeof(stat));
        stat[1][1]=true;
        cin>>l>>x;
        string s,ss;
        cin>>ss;

        for(int i=1;i<=x;i++)s.append(ss);
       //cout<<ss<<endl;
        for(int i=1;i<=s.size();i++)
        {
            char letter= s[i-1];
            int curr;
            if(letter=='i')curr=2;
            else if(letter=='j')curr=3;
            else curr=4;

            memset(stat2,false,sizeof(stat2));

           if(stat[1][2])stat2[2][curr]=true;

           if(stat[2][3])stat2[3][curr]=true;

           for(int z=1;z<=8;z++)
           {
               for(int zz=1;zz<=3;zz++)
               {
                   if(stat[zz][z])
                   {
                       int res=mul(z,curr);
                     //  cout<<z<<" "<<curr<<" "<<res<<endl;
                       stat2[zz][res]=true;
                   }
               }
           }

           for(int z=1;z<=3;z++)
           {
               for(int zz=1;zz<=8;zz++)
               {
                   stat[z][zz]=stat2[z][zz];
               }
           }

        }
        cout<<"Case #"<<y<<": ";
        if(stat[3][4])cout<<"YES\n";
        else cout<<"NO\n";
    }
    /*
    cout<<endl;

    for(int i=1;i<=8;i++)
    {
        for(int j=1;j<=8;j++)cout<<i<<" "<<j<<" "<<mul(i,j)<<endl;
    }
    */
return 0;
}
