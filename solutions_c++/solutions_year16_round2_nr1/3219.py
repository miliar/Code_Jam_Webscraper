#include <iostream>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <math.h>
#include <stack>
#include <queue>
#include <ctype.h>
#include <map>
#include <bitset>
#include <limits>
typedef long long ll;
#define filla(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
#define F first
#define S second
#define MOD 1000000007
using namespace std;
/*long long choose(int n,int k)
{
    if(k==0)
        return 1;
    else
    {
        long long f=1;
        if(k>n-k)
            k=n-k;
        int p=1;
        while(p<=k)
        {
            f*=n--;
            f/=p++;
        }
        return f;
    }
}
ll power(int a,int b)
{
    ll ret;
    if(b==0)
        return 1;
    if(b==1)
        return a;
    ret=power(a,b/2);
    ret=(ret*ret);
    if(b&1)
        ret=(ret*a);
    return ret;
}
bool cmp(int a,int b)
{
    return a>b;
}*/
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    string s;
    int z;
    getline(cin,s);
    for(z=1;z<=t;z++)
    {
        getline(cin,s);
        int i,p,j;
        string c;
        string k[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
        int a[10],ctr=0;
        memset(a,0,sizeof(a));
        map<char,int> m;
        for(i=0;i<s.length();i++)
        {
            m[s[i]]++;
        }
        if(m['Z']>0)
        {
            p=m['Z'];
            for(i=0;i<4;i++)
                m[k[0][i]]-=p;
            ctr+=4*p;
            a[0]+=p;
        }
        if(m['W']>0)
        {
            p=m['W'];
            for(i=0;i<k[2].length();i++)
                m[k[2][i]]-=p;
            ctr+=3*p;
            a[2]+=p;
        }
        if(m['U']>0)
        {
            p=m['U'];
            for(i=0;i<k[4].length();i++)
                m[k[4][i]]-=p;
            ctr+=4*p;
            a[4]+=p;
        }
        if(m['X']>0)
        {
            p=m['X'];
            for(i=0;i<k[6].length();i++)
                m[k[6][i]]-=p;
            ctr+=3*p;
            a[6]+=p;
        }
        if(m['G']>0)
        {
            p=m['G'];
            for(i=0;i<k[8].length();i++)
                m[k[8][i]]-=p;
            ctr+=5*p;
            a[8]+=p;
        }
        while(ctr<s.length())
        {
            if(m['O']>0)
            {
                p=m['O'];
                for(i=0;i<k[1].length();i++)
                    m[k[1][i]]-=p;
                ctr+=3*p;
                a[1]+=p;
            }
            if(m['H']>0)
            {
                p=m['H'];
                for(i=0;i<k[3].length();i++)
                    m[k[3][i]]-=p;
                ctr+=5*p;
                a[3]+=p;
            }
            if(m['F']>0)
            {
                p=m['F'];
                for(i=0;i<k[5].length();i++)
                    m[k[5][i]]-=p;
                ctr+=4*p;
                a[5]+=p;
            }
            if(m['S']>0)
            {
                p=m['S'];
                for(i=0;i<k[7].length();i++)
                    m[k[7][i]]-=p;
                ctr+=5*p;
                a[7]+=p;
            }
            if(m['N']>0)
            {
                p=m['N'];
                for(i=0;i<k[1].length();i++)
                    m[k[1][i]]-=p;
                ctr+=4*(p/2);
                a[9]+=(p/2);
            }
        }
        cout<<"Case #"<<z<<": ";
        for(i=0;i<10;i++)
        {
            for(j=0;j<a[i];j++)
            {
                cout<<i;
            }
        }
        cout<<endl;
    }
    return 0;
}