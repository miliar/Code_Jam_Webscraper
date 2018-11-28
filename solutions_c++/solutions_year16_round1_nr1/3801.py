#include<iostream>
#include<cstring>
#include<stdio.h>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>
#include<algorithm>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n;
    cin>>n;
    for(int t=1 ; t<=n ; t++){
        cout<<"Case #"<<t<<": ";
        char c[1005],res1[1005],res2[1005];
        cin>>c;
     //  cout<<c<<endl;
        int cnt1=0,cnt2=0;
        res1[0]=c[0];
        res2[0]=c[0];
        //cout<<res1[0]<<" "<<res2[0]<<endl;
        for(int i=1 ; i<strlen(c) ; i++){
            if(c[i]>=res1[cnt1]){
                    cnt1++;
                res1[cnt1] = c[i];
              //  cout<<"cnt1="<<cnt1-1<<" "<<c[i]<<endl;
            }else{
                cnt2++;
                res2[cnt2] = c[i];
               // cout<<"cnt2="<<cnt2-1<<" "<<c[i]<<endl;
            }
        }
        for(int i=cnt1 ; i>=0 ; i--){
            cout<<res1[i];
        }
        for(int i=1 ; i<=cnt2 ; i++){
            cout<<res2[i];
        }
        cout<<endl;
       // cout<<"cnt1 = "<<cnt1<<" ; cnt2 = "<<cnt2<<endl;
    }
    return 0;
}
