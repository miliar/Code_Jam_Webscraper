#include <iostream>
using namespace std;

int ar[]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int size=10;

void digits(long long n){
    while(n){
        long long temp=n%10;
        if(!ar[temp]){
            size--;
        }
        ar[temp]++;
        n/=10;
    }
}

int main(){
    int T;      cin>>T;
    for(int i=1; i<=T; ++i){
        size=10;
        for(int j=0; j<10; ++j)
            ar[j]=0;
        
        long long n;  cin>>n;
        int temp=n;
        if(!temp){
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        while(size>0){
            //cout<<temp<<endl;
            digits(temp);
            temp+=n;
        }
        
        cout<<"Case #"<<i<<": "<<temp-n<<endl;
        
        //for(int j=0; j<10; ++j){
        //    cout<<ar[j]<<" ";
        //}
        //cout<<endl;
    }
    
    
    return 0;
}
