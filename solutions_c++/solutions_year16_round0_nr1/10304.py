#include<iostream>
using namespace std;

int main(){
int t;
cin>>t;
int s=t;
while(t--){
    int n;
    cin>>n;
    if(n==0) cout<<"Case #"<<s-t<<": "<<"INSOMNIA"<<endl;
    else if(n==1) cout<<"Case #"<<s-t<<": "<<10<<endl;
    else {
        int arr[10]={0};
        bool flag=true;
        int i=1;
        while(1){
            int fn=n*i;
        int num;
        while(fn>0){
            num=fn%10;
            arr[num]=1;
            fn=fn/10;
        }
        i++;
        for(int j=0;j<10;j++){
            if(arr[j]==0){flag=false;break;}
            if(j==9) flag=true;
        }
        if(flag==false) continue;
        else {
            cout<<"Case #"<<s-t<<": "<<n*(i-1)<<endl;
            break;
        }
    }
}
}
return 0;
}
