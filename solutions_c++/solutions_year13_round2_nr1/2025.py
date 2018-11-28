#include<iostream>
#define N 105

using namespace std;

long long A[N];

int main(){
    int nc;
    cin>>nc;
    for(int caso=1;caso<=nc;caso++){
        int n;
        long long a;
        cin>>a>>n;
        for(int i=0;i<n;i++)cin>>A[i];
        if(a==1LL){
            cout<<"Case #"<<caso<<": "<<n<<endl;
            continue;
        }
        sort(A,A+n);
        int resp=n;
        long long s=a;
        int cont=0;
        for(int i=0;i<n;i++){
            if(s>A[i]){
                s+=A[i];
            }
            else{
                long long k=2;
                while(true){
                    long long aux=k*s-k+1;
                    cont++;
                    //cout<<k<<" "<<cont<<" "<<aux<<" "<<s<<" "<<A[i]<<endl;
                    if(aux>A[i])break;
                    k*=2;
                }
                s=s*k-k+1+A[i];
            }
            resp=min(resp,cont+n-1-i);
        }
        cout<<"Case #"<<caso<<": "<<resp<<endl;
    }
}
