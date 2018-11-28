
#include <iostream>
using namespace std;
int main() {
    int T;
    cin>>T;
    const int Thold=T;
    while(T>0){
        int K,C,S;
        cin>>K>>C>>S;
        cout<<"Case #"<<Thold-T+1<<":";
        for(int i=0;i<S;i++){
            cout<<" "<<i+1;
        }
        cout<<endl;
        
        T--;
    }
    return 0;
}
