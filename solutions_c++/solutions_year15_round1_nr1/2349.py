#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1large.txt","w",stdout);
    int t,z=1,i,n,ans1,ans2;
    int a[1006];
    scanf("%d",&t);
   while(t--){

        cin>>n;

        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        int aa=0,bb=0,maxi=0;
        for(int i=1;i<n;i++){
            if(a[i]-a[i-1]<0){
                aa+=(a[i-1]-a[i]);
            }
            maxi=max(maxi,a[i-1]-a[i]);
        }
        for(int i=0;i<n-1;i++){
            if(a[i]>=maxi)bb+=maxi;
            else bb+=a[i];
        }
        cout<<"Case #"<<z<<": "<<aa<<" "<<bb<<"\n";
        z++;
    }
    return 0;
}
