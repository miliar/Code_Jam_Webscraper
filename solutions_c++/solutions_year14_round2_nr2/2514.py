#include <iostream>

using namespace std;

int main(){

    unsigned long long int A, B, K, counter;
    int T;
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>A>>B>>K;
        counter=0;
        for(int j=0; j<A; j++){
            for(int l=0; l<B; l++){
                if((j&l)<K){
                    counter++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<counter<<endl;
    }

    return 0;
}
