#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int num=0,roll=0;
    cin>>num;
    while(num--){
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<++roll<<": ";
        for(int i=1;i<=k;i++){
            cout<<i<<" ";
        }
        cout<<endl;
    }
}
