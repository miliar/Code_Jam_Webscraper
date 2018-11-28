#include<iostream>
#include<cmath>
#include<vector>
#include<iomanip>
#include<stdio.h>
#include<algorithm>
using namespace std;
typedef long long int lint;
#define loop(x,a,b) for(int x = a; x < b; x++)
int main()
{
	//your code here
	freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
	lint t,ct=0,pr=0,f=0,n,n2;
	cin>>t;
	while(ct<t)
    {
        int  ans[10]={0};
        cin>>n;
        if(n==0)
            cout<<"Case #"<<ct+1<<": "<<"INSOMNIA"<<endl;
        else{
        n2=n;
        while(n2>0)
        {
            ans[n2%10]=1;
            n2=n2/10;
        }
        int mu=1;
        while(1)
        {
            //cout<<"in";
            f=1;

            pr=n*mu;
            int pr2=pr;
            mu++;
            while(pr>0)
            {
                ans[pr%10]=1;
                pr=pr/10;
            }
            for(int i=0;i<=10;i++)
            {
                if(ans[i]==0)
                   {
                       f=0; break;
                    }
            }
            if(f)
            {
                     cout<<"Case #"<<ct+1<<": "<<pr2<<endl;
                    break;
            }
        }
        }
        ct++;
    }
	return(0);
}
