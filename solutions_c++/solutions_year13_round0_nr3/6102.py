#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    int k=1;
    while(t--){
        int A[]={1,4,9,121,484};
        int a,b;
        cin>>a>>b;
        int rp=0;
        for(int i=0; i<5; i++)
            if(A[i]>=a && A[i]<=b)
                rp++;
        cout<<"Case #"<<k<<": "<<rp<<endl;
        k++;
    }   
}
