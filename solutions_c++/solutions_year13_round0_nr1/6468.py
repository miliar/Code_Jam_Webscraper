#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
void inc(string::reverse_iterator orig, string::reverse_iterator finish, string& s);
bool is_palindrome(long long s);
bool is_palindrome(string s);
bool win(long long i);
bool draw(vector<string> b){
    for(auto row : b){
        for(char c : row){
            if(c == '.')
                return false;
        }
    }
    return true;
}
bool row(vector<string> b, char p, int r){
    for(int i = 0; i < 4; ++i) if(b[r][i] != p&&b[r][i] !='T') return false;
    return true;
}
bool col(vector<string> b, char p, int c){
    for(int i = 0; i < 4; ++i) if(b[i][c] != p&&b[i][c] !='T') return false;
    return true;
}
bool diag1(vector<string> b, char p){
    for(int i = 0; i < 4; ++i) if(b[i][i] != p&&b[i][i] !='T') return false;
    return true;
}
bool diag2(vector<string> b, char p){
    for(int i = 0; i < 4; ++i) if(b[i][3-i] != p&&b[i][3-i] !='T') return false;
    return true;
}
bool Awin(vector<string> b, char p){
    for(int i = 0; i < 4; ++i){
        if(row(b,p,i)||col(b,p,i)) return true;
    }
    return diag1(b,p)||diag2(b,p);
}
int main(){
    int n;
    int cas = 0;
    cin>>n;
    while(cas++ < n){
        vector<string> b(4);
        cin >> b[0] >> b[1] >> b[2] >> b[3];
        cout <<"Case #"<<cas<<": ";
        if(Awin(b, 'X')) cout << "X won" << endl;
        else if(Awin(b, 'O')) cout << "O won" << endl;
        else if(draw(b)) cout << "Draw" << endl;
        else cout << "Game has not completed" << endl;

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
