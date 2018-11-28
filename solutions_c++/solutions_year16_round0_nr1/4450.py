#include<iostream>
#include<fstream>
using namespace std;

int give(bool a[],long long int n,int k){
    while(n){
        if(a[n%10]==0)k--;
        a[n%10]=1;
        n/=10;
    }
    return k;
}

int main(){
    // ifstream infile;
   //infile.open("A-small-attempt0.in");


    int t;
    long long int n,m;
    cin>>t;
    int k=10,i=1;
    while(t--){
        cin>>n;
        m=0;
        k=10;
        if(n==0){
                cout<<"Case #"<<i++<<": "<<"INSOMNIA"<<endl;
                continue;
        }
        bool a[10]={0};
        while(k){
                m+=n;
            k = give(a,m,k);
            //cout<<k<<" "<<n<<endl;
        }
    cout<<"Case #"<<i++<<": "<<m<<endl;


    }
return 0;
}
