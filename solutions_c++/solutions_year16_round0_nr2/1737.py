#include<iostream>
using namespace std;

int Calc(string cur, int pos, char m) {
    while(pos>=0&&cur[pos]==m) pos--;
    if(pos==-1) return 0;
    while(pos>=0&&cur[pos]!=m) pos--;
    if(pos==-1) return 1;
    return Calc(cur, pos, m=='-'?'+':'-') + 1;
}

int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        string s;
        cin>>s;
        cout<<"Case #"<<t<<": "<<Calc(s, s.length()-1, '+')<<endl;
    }
    return 0;
}
