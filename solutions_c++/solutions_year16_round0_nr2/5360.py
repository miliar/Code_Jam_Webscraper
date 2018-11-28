#include <iostream>

using namespace std;

void flip(string &s, int index){
    for(int i = 0; i <= index; i++){
        if(s[i] == '+') s[i] = '-';
        else s[i] = '+';
    }
}

int main()
{
    int T;
    string temp;
    getline (cin,temp);
    T = stoi(temp);
    int X = 1;
    while(X <= T){
        int index = 0;
        bool flag = true;
        int c=0;
        string s;
        getline (cin,s);
        while(flag){
            int maxim = -1;
            for(int i = 0; i < s.size() ; i++){
                //cout << "radi" <<endl;
                if(s[i] == '-' && i > maxim) {
                    maxim = i;
                    //cout << i;
                }
            }
            if(maxim == -1){
                    flag = false;
                    break;
                }
            //cout << "radi" <<endl;
            flip(s, maxim);
            //cout << s << endl;
            c++;
        }
        cout << "Case #" << X <<": " << c << endl;
        X++;
    }
    return 0;
}
