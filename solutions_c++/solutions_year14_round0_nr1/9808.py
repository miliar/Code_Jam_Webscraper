#include<iostream>
using namespace std;
void fn(int n)
{
    int a;
    cin>>a;
    int ans[4];
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            int t;
            cin>>t;
            if(i==a-1){
                ans[j] = t;
            }
        }
    }
    int b;
    cin>>b;
    int ans2[4];
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            int t;
            cin>>t;
            if(i==b-1){
                ans2[j] = t;
            }
        }
    }
    int cnt = 0 ;
    int anw ;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(ans[i]==ans2[j]){
                cnt +=1;
                anw = ans[i];
            }
        }
    }
    cout<<"Case #"<<n<<": ";
    if(!cnt){
            cout<<"Volunteer cheated!";
    }
    else if(cnt>1){
            cout<<"Bad magician!";
    }
    else{
        cout<<anw;
    }
    cout<<endl;

}
main(){
    int tc;
    cin>>tc;
    for(int i=0;i<tc;i++){
        fn(i+1);
    }
}
