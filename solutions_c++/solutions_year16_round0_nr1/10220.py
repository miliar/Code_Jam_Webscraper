
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iterator>

using namespace std;

bool if_all_set(vector<bool> &b){
    for(auto x:b){
        if(x == 0) return false;
    }
    return true;
}

void set_all_bits_in_num(vector<bool> &a,long long int v){
    while(v){
        a[(v%10)] = 1;
        v/=10;
    }
}

int main(int argc,char *argv[]){
    int t,Case=1;
    long long int n;
    cin>>t;

    while(t--){
        cin>>n;
        cout<<"Case #"<<Case++<<": ";
        if(n == 0){
            cout<<"INSOMNIA\n";
        }
        else{
            long long int i=0;
            vector<bool> digits(10);
            do{
                i++;
                set_all_bits_in_num(digits,(i*n));
            }while(!if_all_set(digits));
            cout<<(i*n)<<'\n';
        }
    }


    return 0;
}
