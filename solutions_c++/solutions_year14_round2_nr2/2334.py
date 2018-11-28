    #include <iostream>
    using namespace std;
     
     
     
    int main() {
    int test=0;
    cin>>test;
    int test_case=1;
    while(test--){
     
    long long int A,B,K;
    cin>>A;
    cin>>B;
    cin>>K;
    long long int count=0;
    for(long long int i=0;i<A;i++){
    for(long long int j=0;j<B;j++){
    if((i&j)<K)
    count++;
    }
    }
    cout<<"Case #"<<test_case<<": "<<count<<endl;
    test_case++;
    }
    }