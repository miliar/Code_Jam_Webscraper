#include<iostream>
#include<algorithm>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <vector>
#include<queue>
#include<bitset>
#define ll long long
typedef pair<int, int > pii;
#define pb push_back
#define mk make_pair
#define rep(p,q,r) for(int p=q;p<r;p++)
vector<int> v[100010];

int vis[100002]={0};

int main()
{
    int t,n,p,ind,r,l,ans,cas=1;
    string s,ss;
    cin>>t;
    while(t--)
    {
        ans=0;
        cin>>s;
        n=s.length();
        while(1){
        r=n-1;
        while(r>=0&&s[r]=='+')
        r--;
        if(r==-1)
        break;
        l=0;
        while(l<n&&s[l]=='+')
        l++;

        if(l>0)
        {
            ss=s.substr(0,l);
            for(int k=0,m=l-1;k<l;k++,m--)
                {
                    if(ss[m]=='-')
                        ss[m]='+';
                        else ss[m]='-';
                    s[k]=ss[m];
                }
                ans++;
        }
         r=n-1;
        while(r>=0&&s[r]=='+')
        r--;
        if(r==-1)
            break;
        ss=s.substr(0,r+1);
         for(int k=0,m=r;k<=r;k++,m--){
            if(ss[m]=='-')
                ss[m]='+';
            else ss[m]='-';
                s[k]=ss[m];
         }

         //cout<<l<<" "<<r<<"\n";
                ans++;

        }
        printf("Case #%d: %d\n",cas,ans);
        cas++;
    }

}
