#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool is_palindrome(long long orig){
    long long reversed = 0;
    long long n = orig;
    while(n > 0){
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return orig == reversed;
}
int main(){
    vector<long long> squares;
    for(long long i=1; i * i <= 1e14 + 1;i++)
        if(is_palindrome(i))
            squares.push_back(i * i);

    vector<long long> palin;
    for(int i=0;i < squares.size();i++){
        if(is_palindrome(squares[i]))
            palin.push_back(squares[i]);
    }

    int t;
    cin>>t;
    for(int l = 1; l <= t; l++){
        long long a, b;
        cin>>a>>b;
        int count = 0;
        for(int i=0; i < palin.size();i++){
            if(palin[i] >= a && palin[i] <=b)
                count += 1;
        }
        cout<<"Case #"<<l<<": "<<count<<endl;
    }
}

