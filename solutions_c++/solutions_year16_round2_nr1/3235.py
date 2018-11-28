#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
using namespace std;



int main()
{
    ll t,T,n,m,i,j,ans,a,A[3000];
    string s,s1;
    vector< ll> v;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%lld",&T);
    for(t=1; t<=T; t++)
    {
        cin>>s;

        n=s.size();
        v.clear();
        memset(A,0,sizeof A);
        for(i=0; i<n; i++)
        {
            a=s[i]-'A';
            A[a]++;
        }

        s1="";

        if(A[ 'Z'-'A' ]>=1 )
        {
            a=A['Z'-'A'];

            for(i=1; i<=a; i++)
            {
                s1+='0';
                v.push_back(0);
                A['Z'-'A']--;
                A['R'-'A']--;
                A['E'-'A']--;
                A['O'-'A']--;
            }
        }

        if(A['U'-'A']>=1 )
        {
            a=A['U'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='4';
                v.push_back(4);
                A['O'-'A']--;
                A['F'-'A']--;
                A['U'-'A']--;
                A['R'-'A']--;
            }
        }

        if(A['W'-'A']>=1)
        {
            a=A['W'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='2';
                v.push_back(2);
                A['O'-'A']--;
                A['T'-'A']--;
                A['W'-'A']--;
            }
        }

        if(A['X'-'A']>=1)
        {
            a=A['X'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='6';
                v.push_back(6);
                A['S'-'A']--;
                A['I'-'A']--;
                A['X'-'A']--;
            }
        }

        if(A['G'-'A']>=1)
        {
            a=A['G'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='8';
                v.push_back(8);
                A['I'-'A']--;
                A['G'-'A']--;
                A['E'-'A']--;
                A['T'-'A']--;
                A['H'-'A']--;
            }
        }

        if(A['H'-'A']>=1)
        {
            a=A['H'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='3';
                v.push_back(3);
                A['T'-'A']--;
                A['H'-'A']--;
                A['E'-'A']--;
                A['E'-'A']--;
                A['R'-'A']--;
            }
        }

        if(A['F'-'A']>=1)
        {
            a=A[ 'F'-'A' ];
            for(i=1; i<=a; i++)
            {
                s1+='5';
                v.push_back(5);
                A['F'-'A']--;
                A['I'-'A']--;
                A['E'-'A']--;
                A['V'-'A']--;
            }
        }

        if(A['V'-'A']>=1)
        {
            a=A['V'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='7';
                v.push_back(7);
                A['S'-'A']--;
                A['V'-'A']--;
                A['E'-'A']--;
                A['E'-'A']--;
                A['N'-'A']--;
            }
        }

        if(A['O'-'A']>=1)
        {
            a=A[ 'O'-'A' ];
            for(i=1; i<=a; i++)
            {
                s1+='1';
                v.push_back(1);
                A['O'-'A']--;
                A['N'-'A']--;
                A['E'-'A']--;
            }
        }

        if(A['I'-'A']>=1)
        {
            a=A['I'-'A'];
            for(i=1; i<=a; i++)
            {
                s1+='9';
                v.push_back(9);
                A[ 'N'-'A' ]--;
                A[ 'N'-'A' ]--;
                A['I'-'A']--;
                A['E'-'A']--;
            }
        }
        sort(v.begin(),v.end());


        printf("Case #%lld: ",t);
        for(i=0;i<v.size();i++)
        cout<<v[i];
        cout<<endl;
    }
    return 0;
}

