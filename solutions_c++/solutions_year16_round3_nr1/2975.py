#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<utility>
#include<cstring>
#include<map>
#include<time.h>

#define pb push_back
#define po pop_back
#define fs first
#define sc second
#define INF 100000L * 100000L * 100000L * 10000L

using namespace std;

int t,n,v[30],i,j,k,isum,trgt,cj;
int main(){
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);

    cin>>t;
    for(k=0;k<t;++k){
        cout<<"Case #"<<k+1<<": ";
        cin>>n;
        for(i=0;i<n;++i)
            cin>>v[i];
        for(;i<26;++i)
            v[i]=0;
        if(v[0]>v[1]){
            isum=v[1];
            trgt=0;
        }
        else{
            isum=v[0];
            trgt=1;
        }
        j=2;
        while(isum<v[trgt]){
            isum+=v[j];
            ++j;
        }
        --j;
        cj=j;
        while(isum>v[trgt]&&v[j]){
            cout<<(char)('A'+j)<<" ";
            isum--;
            v[j]--;
        }
        ++j;
        for(;j<26;++j){
            while(v[j]--)
                cout<<(char)('A'+j)<<" ";
        }
        for(j=cj;j>1;--j){
            while(v[j]--){
                cout<<(char)('A'+j)<<(char)('A'+trgt)<<" ";
                v[trgt]--;
                isum--;
            }
        }
        while(v[1]>0){
            v[1]--;
            cout<<"AB"<<" ";
        }
        cout<<endl;
    }
}
