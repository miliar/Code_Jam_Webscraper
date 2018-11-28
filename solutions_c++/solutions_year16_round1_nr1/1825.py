#include <iostream>
#include<string>
using namespace std;
void prob1 ()
{
    int T;
    cin >> T;
    string s;
    string res; //= "0";
    string tmp;// = "0";
    for (int c=1; c<=T; c++)
    {
        cin >> s;

        res = "0";
        tmp = "0";
        res[0] = s[0];
        int sz = s.size();
        for (int i=1; i<sz; i++){
            tmp[0] = s[i];
            if(s[i] >= res[0]){
                res = tmp + res;
            }
            else
                res = res + tmp;
        }

        cout << "Case #" << c << ": " <<  res << endl;
    }
}

void gen()
{
    for (int i=0; i<100; i++) {
        for (int j=0; j<500; j++)
            cout <<"AZ";
        cout << endl;
    }
}
using namespace std;

int main() {

    freopen("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    prob1();


   // gen();
    return 0;
}