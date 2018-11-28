#include <iostream>
using namespace std;

int n,stand,horse,i;
char s[1415];

bool problem(int x, int r, int c){
    if(x==1){
        return true;
    } else if(x==2){
        if((r*c)%2==0) return true;
        else return false;
    } else if(x==3){
        if((r*c)%3==0&&r!=1&&c!=1) return true;
        else return false;
    } else if(x==4){
        if((r*c)%4==0&&(r>3||c>3)&&r!=1&&c!=1&&r!=2&&c!=2) return true;
        else return false;
    }
}

int main(){
    int CASENO,TESTCASE;
    int x,r,c;
    cin >> TESTCASE;
    for(CASENO=1;CASENO<=TESTCASE;CASENO++){
        cin >> x >> r >> c;
        cout << "Case #" << CASENO << ": ";
        if(problem(x,r,c)) cout << "GABRIEL";
        else cout << "RICHARD";
        cout << endl;
    }
}
