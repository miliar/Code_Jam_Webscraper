#include <bits/stdc++.h>

using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	long long T,N,n,arr[11];
	while(cin>>T)for(int I=1;I<=T;I++){
        memset(arr,0,sizeof(arr));
        cin>>N;
        if(N == 0)
                cout<<"Case #"<<I<<": "<<"INSOMNIA"<<endl;
        else{
            arr[10]=10;
            for(int i=1;i<10000000;i++){
                n = N*i;
                while(n){
                    if(arr[n%10] == 0){
                        arr[n%10]=1;
                        arr[10]--;
                    }
                    n/=10;
                }
                if(arr[10]==0){
                    arr[10]=N*i;
                    break;
                }
            }
            if(arr[10]>=10)
                cout<<"Case #"<<I<<": "<<arr[10]<<endl;
            else
                cout<<"Case #"<<I<<": "<<"INSOMNIA"<<endl;
        }
	}
}
