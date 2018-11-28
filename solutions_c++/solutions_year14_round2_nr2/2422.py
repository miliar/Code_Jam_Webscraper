#include<iostream>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#include<vector>
#include<cmath>
#include<cstdio>
typedef long long ll;
#define rep(i,n) for(i=0;i<n;i++)
using namespace std;



int main(){
    int i,j,t,t1,n,a,b,k;
    string str[1000];

    cin>>t;

    int ans;


    for(t1=1;t1<=t;t1++){

        cin>>a>>b>>k;
         ans = 0;

        for(i=0;i<a;i++)
            for(j=0;j<b;j++){
                if(  (j&i) < k)
                    ans++;
                  //  cout<<i<<" "<<j<<" "<<(i&j)<<" "<<k<<endl;
                    }

        cout<<"Case #"<<t1<<": "<<ans<<endl;
    }//t


    return 0;
}
