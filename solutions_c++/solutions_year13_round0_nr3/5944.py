#include <iostream>
#include <string>
#include <cmath>
#include <boost/lexical_cast.hpp>

using namespace std;
using boost::lexical_cast;

bool is_palindrome(long);

bool is_fair_square(long num){
    if(!is_palindrome(num))
        return false;
    long s=static_cast<long>(sqrt(num));
    if(s*s != num)
        return false;
    return is_palindrome(s);
}

bool is_palindrome(long num){
    string s=lexical_cast<string>(num);
    //cout<<s<<endl;
    for(int c=0;c<=s.size()/2;c++){
        if(s[c] != s[s.size()-c-1]){
            //cout<<s[c]<<" "<<s[s.size()-c-1]<<endl;
            return false;
        }
    }
    return true;
}

long num_fair_square(long begin,long end){
    long count=0;
    for(long i=begin;i<=end;i++){
        if(is_fair_square(i)){
            count++;
        }
    }
    return count;
}

int main(){
    long num_cases;
    cin>>num_cases;
    for(long c=1;c<=num_cases;c++){
        long a,b;
        cin>>a>>b;
        cout<<"Case #"<<c<<": "<<num_fair_square(a,b)<<endl;
    }
    return 0;
}
