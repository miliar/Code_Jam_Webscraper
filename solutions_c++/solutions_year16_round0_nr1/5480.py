#include<iostream>
using namespace std;
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    long long tests,t,n,i,curr,left;
    bool used[20];
    cin>>tests;
    for(t=1;t<=tests;t++){
        cin>>n;
        if(n!=0){
            for(i=0;i<11;i++){
                used[i]=false;
            }
            curr=n;
            left=10;
            for(i=1;left!=0;i++){
                curr=i*n;
                while(curr!=0){
                    if(!used[curr%10]){
                        left--;
                        used[curr%10]=true;
                    }
                    curr/=10;
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(n==0){
            cout<<"INSOMNIA\n";
        }else{
            cout<<(i-1)*n<<"\n";
        }
    }
    return 0;
}
