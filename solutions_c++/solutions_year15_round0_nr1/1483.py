#include <iostream>
using namespace std;

int n,stand,horse,i;
char s[1415];

int problem(){
    stand=0; horse=0;
    cin >> n >> s;
    for(i=0;i<n;i++){
        stand += s[i]-'0';
        if(stand<i+1){
            horse++;
            stand++;
        }
    }
    return horse;
}

int main(){
    int CASENO,TESTCASE;
    cin >> TESTCASE;
    for(CASENO=1;CASENO<=TESTCASE;CASENO++){
        cout << "Case #" << CASENO << ": " << problem() << endl;
    }
}
