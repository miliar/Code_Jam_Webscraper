#include<iostream>
using namespace std;
int a_case(){
    unsigned long long a,b,c;
    bool numbers[10]={};
    cin>>a;
    if(a==0)    return -1;
    for(unsigned long long i=1;;i++){
        b=a*i;
        c=b;
        while(c!=0){
            numbers[c%10]=true;
            c/=10;
        }
        bool end=true;
        for(int j=0;j<10;j++)   end=end && numbers[j];
        if(end){
            return b;
        }
    }
}
int main(){
    int a;
    cin>>a;
    for(int i=0;i<a;i++){
        int k=a_case();
        if(k==-1)
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else    cout<<"Case #"<<i+1<<": "<<k<<endl;
    }
}
