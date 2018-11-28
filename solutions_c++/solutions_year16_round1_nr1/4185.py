#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
    string s,r;
        int k;
    cin >> s;
        k=s.size();
        for(int j=0;j<k;j++){
            if(j==0)
                r[j]=s[j];
            else
                if(s[j]>=r[0]){
                for(int p=j-1;p>=0;p--){
                    r[p+1]=r[p];
                }
                r[0]=s[j];
            }
            else
                r[j]=s[j];
            }
        cout<<"Case #"<<i<<": ";
        for(int m=0;m<k;m++){
    cout<<r[m];
    }
        cout<<"\n";
    }
    return 0;
}