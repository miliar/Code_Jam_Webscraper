#include <iostream>
using namespace std;

int main() {
    int test=0;
    int test_case=1;
    cin>>test;
    int A, B, K, count;
    while(test--){

        cin>>A;cin>>B;cin>>K;
        count =0;
        for(int i=0;i<A;i++){
            for(int j=0;j<B;j++){
                if((i&j) < K)
                   count++;
           }
        }

                cout<<"Case #"<<test_case<<": "<<count<<endl;

        test_case++;
    }
    return 0;
}
