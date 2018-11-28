#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream inp("filei.txt");
    ofstream oup("fileo.out");
    int t;
    inp>>t;
    for(int j=1;j<=t;j++){
        int n,c=0,ans=0;
        char arr[1000];
        inp>>n;
        inp>>arr;
        for(int i=0;i<=n-1;i++){
            c=c+arr[i]-48;
            if(arr[i+1]-48>0&&c<i+1){
                ans=ans+i+1-c;
                c=i+1;
            }
        }
        oup<<"Case #"<<j<<": "<<ans<<endl;
    }

}
