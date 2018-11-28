#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int k;
        cin>>k;
        char str[10000];
        cin>>str;
//        cout<<str<<endl;
        int arr[k+1];
        for(int i=0;i<strlen(str);i++){
            arr[i]=str[i]-'0';
        }
        int cnt=arr[0],ins=0;
        for(int i=1;i<strlen(str);i++){
            if(i>cnt){
                ins+= i-cnt;
                cnt+= i-cnt;
            }
            cnt+=arr[i];
//            cout<<i<<", "<<ins;
        }
        cout<<"Case #"<<j<<": "<<ins<<endl;
    }
}
