#include <iostream>
#include <cmath>
#include <string>
#include <bitset>

using namespace std;
int t,n,j;
typedef unsigned long long ull;

int main(){
    cin>>t;
    for(int x=0;x<t;x++){
        cout<<"Case #"<<x+1<<": "<<endl;
        cin>>n>>j;
        int divs[11];
        int count=0;

        for(int i=32769;i<65536;i+=2){
            string s=bitset<16>(i).to_string();
            for(int j=2;j<12;j++){
                if(j==11){
                    cout<<s;
                    for(int k=2;k<11;k++){
                        cout<<" "<<divs[k];
                    }
                    cout<<endl;
                    count++;
                    if(count==50){
                        return 0;
                    }
                }
                ull m=stoull(s,0,j);
                divs[j]=-1;
                for(int l=2;l<m;l++){
                    if(m%l==0){
                        divs[j]=l;
                        break;
                    }
                }
                if(divs[j]==-1){
                    break;
                }
            }
        }
    }
    return 0;
}
