#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[111111];

int ab(int x){if (x<0)return -x;return x;}

int myswap(int l,int r){

    if(l>=r){
        for(int i=r;i<l;i++)
            swap(a[i],a[i+1]);
    }else{

        for(int i=r;i>l;i--)
            swap(a[i],a[i-1]);
    }

    return ab(r-l);
}

int main()
{
    //freopen("b.in","r",stdin);
    //freopen("b.out","w",stdout);
    int cas,cass=0,n;
    cin>>cas;
    while(cas--){
        cass++;
        cin>>n;
        for(int i=1;i<=n;i++)
            cin>>a[i];


        int p=1,q=n;

        int ans=0;
        while(p<=q){

            int mi=1000000006,loc=0;
            for(int i=p;i<=q;i++)
            if(a[i]<=mi)
            {
                mi=a[i];
                loc=i;
            }

            if(ab(loc-p)>=ab(loc-q)){
                ans+=myswap(q,loc);
                q--;
            }
            else{
                ans+=myswap(p,loc);
                p++;
            }


        }



        cout<<"Case #"<<cass<<": "<<ans<<endl;
    }


    return 0;
}
