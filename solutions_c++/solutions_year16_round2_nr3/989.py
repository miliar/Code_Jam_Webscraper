#include<bits/stdc++.h>
using namespace std;
string arr[16][2],oarr[16][2],farr[16][2];
int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        int n;
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>arr[i][0]>>arr[i][1];
        }
        int ans=0;
        for(int bit=0;bit<(1<<n);bit++){
            int cnt=0,fcnt=0;
            for(int i=0;i<n;i++){
                if(bit&(1<<i)){
                    oarr[cnt][0]=arr[i][0];
                    oarr[cnt][1]=arr[i][1];
                    cnt++;
                }
                else{
                    farr[fcnt][0]=arr[i][0];
                    farr[fcnt][1]=arr[i][1];
                    fcnt++;
                }
            }
            bool flag=true;
            for(int i=0;i<fcnt;i++){
                bool tmp1=false,tmp2=0;
                for(int j=0;j<cnt;j++){
                    if(oarr[j][0]==farr[i][0])
                        tmp1=1;
                    if(oarr[j][1]==farr[i][1])
                        tmp2=1;
                }
                if(tmp1 and tmp2){
                    flag=1;
                }
                else{
                    flag=0;
                    break;
                }
            }
            if(flag)
                ans =max(ans,fcnt);
        }
        cout<<ans<<endl;
    }
}
