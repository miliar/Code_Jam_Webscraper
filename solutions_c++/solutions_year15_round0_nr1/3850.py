#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>

using namespace std;

string b;
int a[1005];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int icase=0;
    while(T--){
        icase++;
        int n;
        cin>>n;
        cin>>b;
        for(int i=0;i<=n;i++){
            a[i]=b[i]-'0';
        }
        int res=0;
        int cnt=a[0];
        for(int i=1;i<=n;i++){
            while(cnt<i){
                cnt++;
                res++;
            }
            cnt+=a[i];
        }
        cout<<"Case #"<<icase<<": "<<res<<endl;
    }
    return 0;
}
