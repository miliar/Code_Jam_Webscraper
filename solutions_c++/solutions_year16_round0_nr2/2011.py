//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

string aa;
long long ar[100009];
vector<long long>vec;

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,cas,test,flag,temp,now,ans=0;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>aa;
        //cout<<aa<<endl;
        n=aa.size();

        for(i=0;i<n;i++)
        {
            if(aa[i]=='+') ar[i]=1;
            else ar[i]=0;
        }

        vec.clear();

        for(i=0;i<n;i++)
        {
            if(i==0) vec.push_back(ar[i]);
            else if(ar[i]!=ar[i-1]) vec.push_back(ar[i]);
        }

        ans=vec.size();
        if(vec[ans-1]==1) ans--;

        printf("Case #%lld: %lld\n",cas,ans);

    }



}
