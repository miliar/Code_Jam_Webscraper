#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;
void inc(string::reverse_iterator orig, string::reverse_iterator finish, string& s);
bool is_palindrome(long long s);
bool is_palindrome(string s);
bool win(long long i);
int main(){
    int n;
    int cas = 0;
    cin>>n;
    while(cas++ < n){
        long long A;
        long long B;
        cin >> A;
        cin >> B;
        int a = ceil(sqrt(A));
        int b = floor(sqrt(B));
        int tot = 0;
        while(a <= b){
            if(win(a)){
                tot++;
            }
            ++a;
        }
        cout <<"Case #"<<cas<<": " << tot << endl;
    }
}
bool win(long long i){
    return is_palindrome(i) && is_palindrome(i*i);
}
bool is_palindrome(long long i){
    long long l=1, r=pow(10,floor(log10(i)));
    do {
        if((i/l)%10!=(i/r)%10){
            return false;
        }
        l*=10;
        r/=10;
    } while (l<r);
    return true;
}
bool is_palindrome(string str){
    int l=0, r=str.length()-1;
    do {
        if(str[l++]!=str[r--]){
            return false;
        }
    } while (l<r);
    return true;
}
void inc(string::reverse_iterator orig, string::reverse_iterator finish, string& s){
    if(orig != finish){
        (*orig)++;
        if(*orig > '2'){
            *orig = '0';
            inc(++orig, finish, s);
        }
    }else{
        s = "1" + s;
    }
}
