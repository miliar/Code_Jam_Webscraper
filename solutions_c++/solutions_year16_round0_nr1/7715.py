#include<iostream>
using namespace std;

int main(){
    int t,n;
    int ans;
    int temp;
    bool num[10];
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        if(n==0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        int j=1;
        for(int k=0;k<=9;k++){
            num[k]=false;
        }
        while(true){
            temp=j*n;
            ans=temp;
            while(temp!=0){
                num[temp%10]=true;
                temp=temp/10;
            }
            if(num[0]&&num[1]&&num[2]&&num[3]&&num[4]&&num[5]&&num[6]&&num[7]&&num[8]&&num[9]){
                break;
            }
            j++;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
}
