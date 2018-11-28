#include <bits/stdc++.h>
#define PB push_back
using namespace std;

int mod(int v, int n, int m){   //value, base n, mod
    long long i=1,ans=0;
    while(i<=v)i<<=1;i>>=1;
    while(i){
        ans = (ans*n)%m;
        if(v&i)ans+=1;
        i>>=1;
    }
    return ans%m;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,J,N,arr[11];
    vector<int> vec;
    vec.PB(2);
    for(int i=3;i<=3000;i++)for(int j=0;;j++){
        if(i%vec[j]==0){
            break;
        }
        if(vec[j]*vec[j]>i){
            vec.PB(i);
            break;
        }
    }
    cin>>T;
    for(int I=1;I<=T;I++){
        cout<<"Case #"<<I<<":\n";
        cin>>N>>J;
        for(int i=(1<<(N-1))+1;;i+=2){
            if(J==0)break;
            memset(arr,0,sizeof(arr));
            for(int j=2;j<=10;j++){
                for(int k=0;k<vec.size();k++){
                    if(mod(i,j,vec[k])==0){
                        arr[j]=vec[k];
                        arr[0]++;
                        break;
                    }
                }
                if(arr[j]==0)break;
            }
            if(arr[0]==9){
                J--;
                for(int j = N - 1; j >= 0; j--)
                    cout << (i & (1 << j) ? '1': '0');
                for(int j=2;j<=10;j++)cout<<" "<<arr[j];
                cout<<endl;
            }
        }
    }
}
