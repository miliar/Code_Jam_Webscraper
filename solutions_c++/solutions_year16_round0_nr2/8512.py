#include <stdio.h>
#include <string>
#include <fstream>
int a;
using namespace std;
   int nums[10];
void zeroOut(){
for(int i = 0; i < 10; i++){
    nums[i] = 0;
}
}
getNums(long n){

    long x;
    while(n){
        x = n % 10;
        nums[x]++;
        n /= 10;
    }
}
bool checkWin(){
    for(int i = 0; i < 10; i++){
        if(!nums[i]){
            return false;
        }
    }
    return true;
}
int doString(string s){
    const char *  str = s.c_str();
    int ret = 0;
    bool k = false;
    int ss = 0;
    while(str[ss] == '-'){
        ss++;
    }
    if(ss)
        ret++;
    for(int i = ss; i < s.length(); i++){

        if(k && str[i] == '-')
            continue;
        if(!k && str[i] == '-')
            k = true;
        if(k && str[i] == '+'){
            ret +=2;
            k = false;
        }
    }
    if(k && s.length() != 1){
        ret += 2;
    }
    return ret;
}
int main(){

    long cur, mult;
    string s = "";
    ifstream ifs("test4.in");
    ofstream out;
    out.open("output.txt");
    int b;
    ifs >> a;
    long inputs[a];
    printf("A = %d", a);
    for(int i = 0; i < a; i++){
        ifs >> s;
        b = doString(s);
        out << "Case #" << i+1 << ": " << b << "\n";
        printf("Case #%d: %d", i+1, b);
    }

    return 0;


    for(int i = 0; i < a; i++){
        zeroOut();
        mult = 1;
        cur = inputs[i];
        while(1){
            if(cur <= 0){
                out << "Case #" << i+1 << ": INSOMNIA\n";
                break;
            }
            getNums(cur * mult);
            if(checkWin()){
                out << "Case #" << i+1 << ": " << cur*mult << "\n";
                break;
            }
            mult++;
        }

    }
    return 0;
}