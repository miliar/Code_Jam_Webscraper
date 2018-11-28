#include <istream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void calculate(int t){
    string str ;
    cin >> str ;
    int cnt = 0 ;
    char ch = str[0] ;
    
    for(int i = 0; i < str.size(); i++) {
        if(str[i] == ch)
            continue ;
        cnt++ ;
        ch = str[i] ;
    }
    if(ch == '-')
        cnt++ ;
    
    cout << "Case #" << t+1 << ": " << cnt << endl ;
}

int main(){
    int t ;
    cin >> t ;
    for(int i = 0; i < t; i++)  calculate(i) ;
}
