#include <bits/stdc++.h>
using namespace std;
int small[16];
long long nontrivial;
string toBinary(int n)
{
    std::string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return r;
}
vector <string> possibilities;
long long poww(long long x, int p){
    long long tmp = 1;
    for(int i =0;i<p;i++){
        tmp *= x;
    }
    return tmp;
}
long long baseval(string cur,long long b){
    long long total = 0;
    for(long long i = 15;i>=0;i--){
        //cout << (long long)poww(b,i)*(cur[15-i]-'0') << endl;
        total += (long long)(poww(b,i))*(cur[15-i]-'0');
    }
    return total;
}
bool isprime(long long what){
    for(long long i = 2;i<(long long)sqrt(what)+5;i++){
        if(what%i==0){
            nontrivial = i;
            return false;
        }
    }
    return true;
}
bool check(string s){
    for(long long i=2;i<=10;i++){
        long long cur = baseval(s,i);
        if(isprime(cur)){
            return false;
        }
    }
    cout << s << " ";
    for(long long i=2;i<=10;i++){
        long long cur = baseval(s,i);
        if(!isprime(cur)){
            cout << nontrivial << " ";
        }
    }
    return true;
}
int main()
{
    freopen("code.out","w",stdout);
    for(int i=(1<<15);i<(1<<16);i++){
        string whatevs = toBinary(i);
        if(whatevs[15]=='1'){
            possibilities.push_back(whatevs);
        }
    }
    int counter = 0;
    cout << "Case #1:" << endl;
    for(int i=0;i<possibilities.size();i++){
        //cout << possibilities[i] << endl;
        if(counter == 50)break;
        string bb = possibilities[i];
        if(check(bb)){
            counter ++;
            cout << endl;
        }
    }
    //cout << baseval("0000000000000111",3) << endl;
    //for(int i=0;i<possibilities.size();i++)
    return 0;
}
