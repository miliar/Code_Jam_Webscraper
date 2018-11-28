#include <stdio.h>
#include <fstream>
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
int main(){

    long cur, mult;
    ifstream ifs("test2.in");
    ofstream out;
    out.open("output.txt");
    int a, b;
    ifs >> a;
    long inputs[a];
    for(int i = 0; i < a; i++){
        ifs >> inputs[i];
    }



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