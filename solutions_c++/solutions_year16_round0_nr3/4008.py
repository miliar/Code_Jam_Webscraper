#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cmath> 

using namespace std;

long long isnotprime(long long n){
    for(int i=2;sqrt(n)>i;i++){
        if(n%i == 0) return i;
    }
    return 0;
}

long long base(long long n, int base_base, int count){
    if(n == 0) return 0;
    return (n%10)*pow(base_base,count) + base((n-n%10)/10, base_base, count+1);
}

vector<long long> bases(long long n){
    vector <long long> v;
    for(int i=2;i<=9;i++){
        v.push_back(base(n,i,0));
    }
    v.push_back(n);
    return v;
}

long long join(vector<int> v){
    long long num=pow(10,v.size()+1);
    int count = 1;
    for(int j=v.size()-1;j>=0;j--){
        num += v[j]*pow(10,count);
        count++;
    }
    return num+1;
}

void solve(vector<int> &digits, int req){
    long long num=0;
    for(int i=0;i<digits.size()&&req>0;i++){
        digits[digits.size()-1-i] = 1;
        do{
            num = join(digits);
            vector <long long> listbase = bases(num);
            for(int j=0;j<listbase.size();j++){
                if(!isnotprime(listbase[j])){
                    break;
                }
                else if(j == listbase.size()-1){
                    req--;
                    cout << num;
                    for(int j=0;j<listbase.size();j++){
                        cout <<" "<<isnotprime(listbase[j]);
                    }
                    cout <<endl;
                    break;
                }
            }
        }while(next_permutation(digits.begin(),digits.end())&&req>0);
    }
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,N,J;
    long long num;
    cin >> t;
    for(int q=0;q<t;q++){
        cout << "Case #" << q+1 << ":"<<endl;
        cin >> N >> J;
        vector <int> digits(N-2,0);
        solve(digits, J);


    }


    return 0;
}