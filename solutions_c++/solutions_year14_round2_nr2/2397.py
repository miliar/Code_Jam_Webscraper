#include<bits/stdc++.h>

using namespace std;

int main(){
        //freopen("B-small-attempt0.in","r",stdin);
        //freopen("2A.txt","w",stdout);
        int tc;
        int ct=0;
        cin>>tc;
        while(tc--){

                ct++;
                int n,a,k;
                cin>>n>>a>>k;
                long long ans=0;
                for(int i=0;i<n;++i)
                        for(int j=0;j<a;++j)
                                if((i&j)<k)
                                        ans++;
                cout<<"Case #"<<ct<<": ";
                cout<<ans<<endl;
        }
}
