#include <iostream>

using namespace std;

int checkNonzero(int arr[10]){
    for(int i=0;i<10;i++)
        if(arr[i]==0)
            return 0;
    return 1;
}

void countDigits(int arr[],unsigned long long int n){
    while(n!=0){
        arr[n%10]++;
        n=n/10;
    }
}

void answer(int index){
    int arr[10]={0};
    unsigned long long int n,test;
    cin>>n;
    test=n;
    if(n==0){
        cout<<"Case #"<<index<<": INSOMNIA"<<endl;
        return;
    }
    countDigits(arr,test);
    int k=2;
    while(!checkNonzero(arr)){
        test=n*k++;
        countDigits(arr,test);
    }
    cout<<"Case #"<<index<<": "<<test<<endl;
}

int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        answer(i);
    }
    return 0;
}
