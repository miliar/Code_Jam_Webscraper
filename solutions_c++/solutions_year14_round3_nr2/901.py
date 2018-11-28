//#include<conio.h>
//0000000000000000000000000000//
//%%%%   Archit Srivastava %%%//
//        NIT Durgapur        //
//0000000000000000000000000000//
#include<ctype.h>
#include<cstdio>
#include<stdio.h>
#include<utility>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<sstream>
#include<map>
#include<string>
#include<set>
#include<time.h>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define PB push_back
#define MP make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000007
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define piw(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plln(n) printf("%lld\n",n)
#define pllw(n) printf("%lld ",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define psn(s) printf("%s\n",s)
#define psw(s) printf("%s ",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")
#define mods 1000000009
//
//inline int ri()
//{
//    int n=0;char c;
//    while(1)
//    {
//        c=getchar();//_unlocked();
//        if(c=='\n'||c==' '||c==EOF)break;
//        n=(n<<3) + (n<<1) +c-48;
//    }
//    return n;
//}
/*
inline long long rll()
{
    long long n=0;
    char c;
    while(1)
    {
        c=getchar_unlocked();
        if(c=='\n'||c==' '||c==EOF)break;
        n=(n<<3) + (n<<1) + c - 48;
    }
    return n;
}
*/
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef unsigned long long LL;

#define PI (3.141592653589793)
#include<fstream>

LL gcd(LL a,LL b)
{
    if(b>a)
        return gcd(b,a);
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}


string str[100+5];
LL me=0;
int uss[30]={};

int check(string s)
{
    int i,count=1;
    char prev=s[0];

    for(i=1;i<s.length();i++)
    {
        if(s[i]==prev)
        {
            count++;
        }
        else
        {
            if(count==uss[prev-'a'])
            {
                prev=s[i];
                count=1;
            }
            else
            {
                return 0;
            }
        }
    }
    return 1;
}

int meth(int id,int curr,int n,int used[12],string s)
{
//        cout<<"curre "<<id<<" "<<curr<<" "<<n<<"\n";
    if(curr==n)
    {
//        cout<<"Here\n";
//        for(int j=0;j<=n;j++)
//        {
//            if(used[j]!=1)
//            {
//                s+=str[j];
//                if(check(s))
//                {
//                    me+=1;
//                    return 1;
//                }
//                return 0;
//            }
//        }
//        s+=str[id];

                if(check(s))
                {
//                    cout<<s<<" LOL \n";
                    me+=1;
                    return 0;
                }
                return 0;

    }
    else
    {
//        cout<<"LOOP\n";
        int tt=n;
        for(int j=0;j<=tt;j++)
        {
//            cout<<id<<" "<<j<<" "<<used[j]<<"\n";
            string ne;
            if(used[j]!=1)
            {
                used[j]=1;
                ne=s+str[j];
                id=j;
                meth(id,curr+1,n,used,ne);
                used[j]=0;
            }

        }
    }
}

int main()
{
    int t,z;
    si(t);
    z=t;
    while(t--)
    {
        me=0;
        int n;
        si(n);
        int i;
        rep(i,29)
        uss[i]=0;
        rep(i,n)
        {
            cin>>str[i];
            string temp=str[i][0];
            if(str[i].length!=1)
                temp+=str[i][str[i].length()-1];
            str[i]=temp;
            for(int j=0;j<str[i].length();j++)
            {
                uss[str[i][j]-'a']++;
            }

//            cout<<str[i];pn;
        }
        int used[12]={};
        string s="";
        rep(i,n){
            used[i]=1;
        meth(i,0,n-1,used,str[i]);
        used[i]=0;
        }

        cout<<"Case #"<<z-t<<": ";
        cout<<me;pn;
    }
}
