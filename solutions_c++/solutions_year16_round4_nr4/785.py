//
//
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<vector>
#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int n;
string a[5];
vector<int>loc;
string c[5];
bool flag,tag;
int ra[5],cnt[5],b[5];
void win(int t)
{
    if(!tag)
        return;
    if(t==n)
        return;
    bool nex=false;
    for(int i=0;i<n;i++)
        if(c[ra[t]][i]=='1'&&cnt[i])
        {
            nex=true;
            cnt[i]=0;
            win(t+1);
            cnt[i]=1;
        }
    if(!nex)
    {
        tag=false;
        return;
    }
}
void choose(int p,int q,int r)
{
    if(flag)return;
    if(q==r)
    {
        for(int i=0;i<n;i++)
            c[i]=a[i];
        for(int i=0;i<p;i++)
            if(b[i])
                c[loc[i]/n][loc[i]%n]='1';
        for(int i=0;i<n;i++)
            ra[i]=i;
        bool check=true;
        do
        {
            for(int i=0;i<n;i++)
                cnt[i]=1;
            tag=true;
            win(0);
            if(!tag)
            {
                check=false;
                break;
            }
        }while(next_permutation(ra,ra+n));
        if(check)
            flag=true;
        return;
    }
    if(p==loc.size())
        return;
    b[p]=1;
    choose(p+1,q+1,r);
    b[p]=0;
    choose(p+1,q,r);
}
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>a[i];
        loc.clear();
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(a[i][j]=='0')
                    loc.push_back(i*n+j);
        flag=false;
        for(int p=0;p<=loc.size();p++)
        {
            memset(b,0,sizeof(b));
            choose(0,0,p);
            if(flag)
            {
                cout<<p<<endl;
                break;
            }
        }
    }
}