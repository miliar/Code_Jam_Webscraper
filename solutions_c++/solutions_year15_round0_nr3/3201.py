//
//  main.cpp
//  brute Dijk
//
//  Created by Dhruv Mullick on 11/04/15.
//  Copyright (c) 2015 Dhruv Mullick. All rights reserved.
//

#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define f first
#define s second
typedef pair<int,int> ii;
typedef pair<int,pair<int,int> > iii;

char dp[10001][10001];
int sgn[10001][10001];

void mult(char &c, char a, int &cs, int as)
{
    if(c=='1'&&a=='1')
    {
        cs=cs*as;
    }
    else if(c=='1'&& a=='i')
    {
        c=a;
        cs=cs*as;
    }
    else if(c=='1'&& a=='j')
    {
        c=a;
        cs=cs*as;

    }
    else if(c=='1'&& a=='k')
    {
        c=a;
        cs=cs*as;

    }
    else if(c=='i'&& a=='1')
    {
        cs=cs*as;
        
    }
    else if(c=='i'&& a=='i')
    {
        c='1';
        cs=cs*as*-1;
    }
    else if(c=='i'&& a=='j')
    {
        c='k';
        cs=cs*as;

    }
    else if(c=='i'&& a=='k')
    {
        c='j';
        cs=cs*as*-1;

    }
    else if(c=='j'&& a=='1')
    {
        cs=cs*as;

    }
    else if(c=='j'&& a=='i')
    {
        c='k';
        cs=cs*as*-1;

    }
    else if(c=='j'&& a=='j')
    {
        c='1';
        cs=cs*as*-1;
        
    }
    else if(c=='j'&& a=='k')
    {
        c='i';
        cs=cs*as;

    }
    else if(c=='k'&& a=='1')
    {
        cs=cs*as;

    }
    else if(c=='k'&& a=='i')
    {
        c='j';
        cs=cs*as;

    }
    else if(c=='k'&& a=='j')
    {
        c='i';
        cs=cs*as*-1;

    }
    else if(c=='k'&& a=='k')
    {
        c='1';
        cs=cs*as*-1;
    }

}
int main(int argc, const char * argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t,l,x,i,j,cs,as;
    char c,x1,y1;
    string S1,S;
    
    freopen("in.txt","r",stdin);
    
    cin>>t;
    for(int m=1;m<=t;m++)
    {
        cin>>l>>x;
        cin>>S1;
        
        S="";
        for(i=1;i<=x;i++)
            S=S+S1;
        
        l = l*x;
        
        
        for(i=0;i<l;i++)
        {
            c='1';
            cs=1;
            for(j=i;j<l;j++)
            {
                mult(c,S[j],cs,1);
                dp[i][j]=c;
                sgn[i][j]=cs;
            }
        }
        
        bool flag=0;
        
        for(i=0;i<=l-3 && flag==0;i++)
        {
            for(j=i+1;j<=l-2;j++)
            {
                if(dp[0][i]=='i' && sgn[0][i]==1 && dp[i+1][j]=='j' && sgn[i+1][j]==1 && dp[j+1][l-1]=='k' && sgn[j+1][l-1]==1)
                {
                    flag=1;
                    break;
                }
            }
        }
        
        cout<<"Case #"<<m<<": ";
        if(flag==1)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
    
    return 0;
}
