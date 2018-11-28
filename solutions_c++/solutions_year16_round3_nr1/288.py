#include<bits/stdc++.h>
using namespace std;
int p[27],n;
bool ok(){
    for(int i=0;i<n;i++){
        if(p[i]>0)return 0;
    }
    return 1;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>p[i];
        }
        cout<<"Case #"<<z<<":";
        while(!ok()){
            int ii=-1,jj=-1;
            int sum=0,mx=0,mxii;
            for(int i=0;i<n;i++){
                if(p[i]==0)continue;
                for(int j=i;j<n;j++){
                    if(p[j]==0)continue;
                    mx=0;
                    sum=0;
                    for(int k=0;k<n;k++){
                        if(p[k]==0)continue;
                        if(i==j && i==k){
                            if(p[k]>1){
                                sum+=p[k]-2;
                                mx=max(mx,p[k]-2);
                            }
                            else {
                                sum+=p[k]-1;
                                mx=max(mx,p[k]-1);
                            }
                        }
                        else if(i==k){
                            sum+=p[k]-1;
                            mx=max(mx,p[k]-1);
                        }
                        else if(j==k){
                            sum+=p[k]-1;
                            mx=max(mx,p[k]-1);
                        }
                        else {
                            sum+=p[k];
                            mx=max(mx,p[k]);
                        }
                    }
                    if(mx*2<=sum){
                        ii=i;
                        jj=j;
                        break;
                    }
                }
                if(ii!=-1)break;
            }
            if(ii==-1){
                mxii=-1,mx=0;
                for(int i=0;i<n;i++){
                    if(mx<p[i]){
                        mx=p[i];
                        mxii=i;
                    }
                }
                p[mxii]--;
                cout<<" "<<char('A'+mxii);
            }else{
                if(ii==jj){
                    if(p[ii]>1){
                        cout<<" "<<char('A'+ii)<<char('A'+ii);
                        p[ii]-=2;
                    }
                    else {
                        p[ii]--;
                        cout<<" "<<char('A'+ii);
                    }
                }else{
                    cout<<" "<<char('A'+ii)<<char('A'+jj);
                    p[ii]--;
                    p[jj]--;
                }
            }
//            for(int i=0;i<n;i++)cout<<p[i]<<" ";cout<<endl;
        }
        cout<<"\n";
    }
    return 0;
}
