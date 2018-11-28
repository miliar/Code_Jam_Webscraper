#include<iostream>
#include<vector>
#include<cstdint>
#include<cmath>

using namespace std;


uint64_t is_prime(uint64_t x){
    double rt = sqrt(x);
    if(x%2 == 0)
        return 2;
    for(uint64_t i = 3;i<=rt;i++){
        if(x%i == 0)
            return i;
    }
    return 0;
}

bool is_coin(uint64_t N){
    //integer to binary
    vector<int> bin;

    vector<uint64_t> v(11,0);
    uint64_t n = N,x;
    int base,j;
    while(n){
        bin.push_back(n%2);
        n /= 2;
    }
    for(base = 2; base <= 10;base++){
        uint64_t num=0;
        for(j=1;j<bin.size();j++){
            if(bin[j] == 1)
                num += pow(base, j);
        }
        num++;
        if(!(x=is_prime(num))){
            return false;
        }else{
            v[base] = x;
        }
    }
        for(j=bin.size()-1;j>=0;j--){
        cout<<bin[j];
    }
    for(j = 2;j<=10;j++)
        cout<<" "<<v[j];
    cout<<endl;
    return true;
}

int main(){
    unsigned int t;
    cin>>t;
    int c_n,N,J;
    c_n = 1;
    while(t--){
        cin>>N>>J;
        cout<<"Case #"<<c_n<<":"<<endl;
        c_n++;
        int x=0;
        uint64_t f=pow(2, N-1);
        while(x < J){
            if(f%2 == 1){
                if(is_coin(f)){
                    x++;
                }
            }
        f++;
        }
    }
}