#include<bits/stdc++.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) typeof(c.begin())
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define si set<int>
#define msi multiset<int>
#define sp set<pair<int,int> >
#define vp vector<pair<int,int> >
#define pb push_back
#define mp make_pair
using namespace std;
int main()
{
	int t,k,n,i,f,j;
    char string[101][102];
    char string1[102];
    int chk[101][101];
    
    freopen("input.txt","r",stdin);
        freopen("qqqq.txt","w",stdout);
    cin>>t;
    for(k=1;k<=t;++k)
    {
        f=1;
        for(i=0;i<=100;++i)
        {
 
            for(j=0;j<=100;++j)
            {
 
                chk[i][j]=0;
            }
        }
        cout<<"Case #"<<k<<": ";
        int n;
        cin>>n;
        for(i=1;i<=n;++i)
            cin>>string[i];
            
 int x;
        x=0;
        string1[x]=string[1][0];
                       chk[1][x]++;
 
        for(i=1;i<strlen(string[1]);++i)
        {
            if(string[1][i]!=string[1][i-1])
            {
                x++;
                string1[x]=string[1][i];
 
                chk[1][x]++;
            }
            else{
                chk[1][x]++;
            }
        }
        
        
        for(i=2;i<=n;++i)
        {
            x=0;
            if(string[i][0]!=string1[0])
            {
                f=0;
                break;
            }
            else{
                    chk[i][x]++;
 
            }
            for(j=1;j<strlen(string[i]);++j)
            {
                if(string[i][j]!=string[i][j-1])
                {
                    x++;
                    if(string[i][j]!=string1[x])
                    {
                        f=0;
                        break;
                    }
                    else
                    chk[i][x]++;
                }
               else{
                chk[i][x]++;
                 }
            }
            
            
            
            
        }
        
        
        
            if(f==0)
                cout<<"Fegla Won\n";
            else{
                int len=strlen(string1);
                int ans=0;
 
                int tmp;
                 for(i=0;i<len;++i)
                {
                     tmp=0;
                     for(j=1;j<=n;++j)
                    {
                       tmp=tmp+chk[j][i];
                    }
                    if(tmp%n==0)
                    {
                        tmp=tmp/n;
                        int ans1=0;
                                for(j=1;j<=n;++j)
                       {
                       ans1=ans1+abs(tmp-chk[j][i]);
                        }
                        ans=ans+ans1;
                    }
                    else{
					 	int ans1,ans2;
                    int tmp1,tmp2;
                  ans1=ans2=0;
                    tmp1=tmp/n;
                        tmp2=tmp1+1;
                        for(j=1;j<=n;++j)
                       {
                       ans1=ans1+abs(tmp1-chk[j][i]);
                        }
                        for(j=1;j<=n;++j)
                       {
                       ans2=ans2+abs(tmp2-chk[j][i]);
                        }
                        ans=ans+min(ans1,ans2);
                    }
                }
                        cout<<ans<<endl;
            }
 
 
    }
    return 0;
}
