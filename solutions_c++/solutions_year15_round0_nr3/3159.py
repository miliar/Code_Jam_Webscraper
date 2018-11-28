#include <vector>
#include <climits>
#include <stack>
#include <map>
#include <algorithm>
#include <list>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <queue>
#define ll long long
#define s1(a) scanf("%d",&a)
#define sc(a) scanf("%c",&a)
#define s1ll(a) scanf("%lld",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s2ll(a,b) scanf("%lld %lld",&a,&b)
#define s1d(a) scanf("%lf",&a)
#define s2d(a,b) scanf("%lf %lf",&a,&b)
#define p1(a) printf("%d\n",a)
#define pc(a) printf("%c\n",a)
#define p1ll(a) printf("%lld\n",a)
#define p1d(a) printf("%lf\n",a)
#define MAX 1000000
using namespace std;
int main()
{
    int t;
    s1(t);
    for(int ii=1;ii<=t;ii++)
    {
        int L,X;
        s2(L,X);
        string str;
        cin>>str;
        bool minus=false, ans=false;
        char check;
        int r,c;
        char arr[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
        bool arrmin[4][4]={{true,true,true,true},{true,false,true,false},{true,false,false,true},{true,true,false,false}};
        int f=0,ccount=0;
        check='1';
        char finstr[3];

        for(int i=1;i<=X;i++)
        {
            for(int j=0;j<L;j++)
            {
                /**
                if(f==0)
                {
                    f++;continue;
                }*/
                if(check=='1')
                    r=0;
                else if(check=='i')
                    r=1;
                else if(check=='j')
                    r=2;
                else if(check=='k')
                    r=3;

                if(str[j]=='1')
                    c=0;
                else if(str[j]=='i')
                    c=1;
                else if(str[j]=='j')
                    c=2;
                else if(str[j]=='k')
                    c=3;

                check=arr[r][c];
                if(arrmin[r][c]==false)
                    minus=(!minus);

                //cout<<check<<" "<<minus<<endl;
                if(ccount==0&&check=='i')
                {
                    ccount++;
                    finstr[0]=check;
                    /**
                    if(j+1<L)
                    {
                        check=str[j];
                        //f=0;
                    }
                    else
                    {
                        check=str[0];
                        f=0;
                    }*/
                    check='1';
                }
                else if(ccount==1&&check=='j')
                {
                    ccount++;
                    finstr[1]=check;
                    /**
                    if(j+1<L)
                    {
                        check=str[j];
                        //f=0;
                    }
                    else
                    {
                        check=str[0];
                        f=0;
                    }*/
                    check='1';
                }
                else if(ccount==2&&check=='k'&&i==X&&j==L-1)
                {
                    ccount++;
                    finstr[2]=check;
                    /**
                    if(j+1<L)
                    {
                        check=str[j];
                        //f=0;
                    }
                    else
                    {
                        check=str[0];
                        f=0;
                    }*/
                    check='1';
                }
            }
        }
        if(minus==false &&ccount==3)
            ans=true;
        if(ans==true)
            printf("Case #%d: YES\n",ii);
        else
            printf("Case #%d: NO\n",ii);
    }
}
