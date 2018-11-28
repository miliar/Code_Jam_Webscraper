#include<iostream>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<vector>
#include<cstdio>

using namespace std;

vector<long long>ans;

int main(){

    freopen("gcj_round1C_prbA_input.txt","r",stdin);
    freopen("gcj_round1C_prbA_output.txt","w",stdout);

    int t,l;
    cin>>t;
    for(l=1;l<=t;l++){
        ans.clear();
        long long n,i,a[50],maxm=0,cnt=0;
        cin>>n;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        cout<<"Case #"<<l<<": ";
        while(1){
            for(i=0;i<n;i++){
                if(a[i]>maxm)maxm=a[i];
            }
            for(i=0;i<n;i++){
                if(a[i]==maxm){
                    cnt++;
                }
            }
            if(cnt%2!=0){
                for(i=0;i<n;i++){
                    if(a[i]==maxm){
                        cout<<char(i+'A')<<" ";
                        a[i]--;
                        break;
                    }
                }
            }
            cnt=0;
            for(i=0;i<n;i++){
                if(a[i]==maxm){
                    cnt++;
                    cout<<char(i+'A');
                    a[i]--;
                }
                if(cnt==2)break;
            }
            if(cnt>0)cout<<" ";
            maxm=0;cnt=0;
            for(i=0;i<n;i++){
                if(a[i]>0)cnt++;
            }
            if(cnt==0)break;
            cnt=0;
        }
        cout<<"\n";
    }
    return 0;
}
