//Author : Jatin Goyal
//codecracker4

#include<bits/stdc++.h>
using namespace std;
#define MOD 1e18  //NA
#define N 11111
#define ll long long int
#define dt ll
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)
#define tr(container, it) for(vector<dt> ::iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> >::iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)
#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;
#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second
ll t,n,no,a[N],mid,l,r,ans,finale,dans,cur,dcur;
int main()
{
	freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
	cin>>t;
	rep(tes,1,t)
	{
	    finale=0;
	    cin>>n>>no;
	    rep(i,0,n-1) cin>>a[i];
	    if(no<=n) {cout<<"Case #"<<tes<<": "<<no<<endl; continue;}
	    //no=no-n;
	    l=0;
	    r=MOD;
	    while(l<r)
        {
            ans=0;
            mid=(l+r)/2ll;
            rep(i,0,n-1) ans+=mid/a[i]+(bool)(mid%a[i]);

            if(ans>=no) r=mid;
            else l=mid+1;
        }
        //cout<<mid<<endl;
        rep(ct,mid-2000,mid+2000)
        {
            ans=0;
            if(ct<0) continue;
            rep(i,0,n-1) ans+=ct/a[i]+(bool)(ct%a[i]);
            if(ans>=no)
            {
            //    cout<<ct<<endl;
                dans=0;
                rep(i,0,n-1) dans+=(ct-1)/a[i]+(bool)((ct-1)%a[i]);

                cur=no-dans;
                dcur=0;
                rep(i,0,n-1)
                {
                    if((ct-1)%a[i]==0)
                    {
                        dcur++;
                        if(dcur==cur) {finale=i; break;}
                    }
                }
                break;
            }
        }
	    cout<<"Case #"<<tes<<": "<<finale+1<<endl;
	}
}
