#include<iostream>
#include<fstream>
using namespace std;

int check(bool a[],long long int n,int k){
   int r;
    while(n){
    	r=n%10;
        if(a[r]==0)
		 { k--;
	     }
        a[r]=1;
        n/=10;
    }
    return k;
}

int main(){
     
int main(){
	
    int t;
    long long int n,m;
    cin >> t;
    int k=10,i=1;
    while(t--){
        cin >> n;
        m=0;
        k=10;
        if(n==0){
                cout<<"Case #"<<i++<<": "<<"INSOMNIA"<<endl;
                continue;
        }
        bool a[10]={0};
        while(k){
                m+=n;
            k = check(a,m,k);
    } cout<<"Case #"<<i++<<": "<<m<<endl;

    }
return 0;
}
