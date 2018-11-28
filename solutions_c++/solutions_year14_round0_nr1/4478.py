#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int t,c=1;
    cin>>t;
    while(t--){
        int arr[4][4];
        int fr[4],ans,sec,count=0,res;
        cin>>ans;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
               cin>>arr[i][j];
               if(i==ans-1)
                fr[j]=arr[i][j];
            }
        }
        cin>>sec;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>arr[i][j];
                if(i==sec-1){
                for(int k=0;k<4;k++)
                    if(arr[i][j]==fr[k]){
                        count++;
                        res=fr[k];
                    }
               }
            }
        }
        cout<<"Case #"<<c<<":";
        if(count==1)
            cout<<res<<endl;
        else if(count>1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<"Volunteer cheated!"<<endl;
        c++;
    }
}
