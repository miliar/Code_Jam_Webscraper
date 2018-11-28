#include<iostream>
#include<string>
using namespace std;

int main(){
    string a;
    int i,j,k,t,len,counter;
    cin>>t;
    for(i=1;i<=t;i++){
        counter=0;
        cin>>a;
        len = a.size();
        for(j=0;j<len-1;j++)
            if(a[j]!=a[j+1]) counter++;
        if(a[0]=='+') cout<<"Case #"<<i<<" "<<2*counter<<endl;
        else cout<<"Case #"<<i<<" "<<2*counter-1<<endl;
    }
}
