#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;
int k, t, ans1 =0, ans2 =0, w;
double na[1010];
double ke[1010],u[1010];
void solve(){
    int i, j, n, l;
    cin>>n;
    for(i=0;i<n;i++){
        cin>>na[i];
    }
    for(i=0;i<n;i++){
        cin>>ke[i];
    }
    sort(na,na+n);
    sort(ke,ke+n);
    for(w=0;w<n;w++){
        l=0;
        for(j=0;j<n-w;j++){
            if(na[w+j]<ke[j]){
                l=1;
                break;
            }
        }
        if(l==0){
            ans2=n-w;
            break;
        }
    }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(na[i]<ke[j]&&u[j]==0){
            u[j]=1;
///            cout<< na[i]<<' '<< ke[j]<<endl;
            break;
            }
        }
    }
    for(i=0;i<n;i++)
        if(u[i]==0) ans1 ++;
    memset(u,0,sizeof(u));
}
int main()
{
    cin>>k;
    for(t=0;t<k;t++){
        solve();
        cout<<"Case #"<<t+1<<": "<<ans2<<' '<<ans1<<endl;
        ans1=0;ans2=0;
    }
    return 0;
}