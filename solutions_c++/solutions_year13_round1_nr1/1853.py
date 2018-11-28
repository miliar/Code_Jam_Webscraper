#include <iostream>
using namespace std;
int main()
{
    int T,r,t;
    int cnt=1;
    cin>>T;
    while(T--){
        cin>>r>>t;
        int c=0;
        while(t>0){
            for(int a=1;;a+=2){
                if(2*(r+a)-1<=t){
                    c++;
                    t-=(2*(r+a)-1);
                }else{
                    cout<<"Case #"<<cnt++<<": "<<c<<endl;
                    t=0;
                    break;
                }
            }
        }
    }
}