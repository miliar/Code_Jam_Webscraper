#include<iostream>
#include<string>
#include<sstream>
#include<cstdio>
using namespace std;

int main() {
    int T,m,n;
    bool completed, found[10];
    string str;
    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        cin >> n;
        if(n==0) {
            cout << "Case #" << tc << ": INSOMNIA" << endl;
            continue;
        }
        for(int c=0;c<10;c++) {
            found[c] = false;
        }
        completed = false;
        for(int c=1;!completed;c++) {
            m = n*c;
            str = static_cast<ostringstream*>( &(ostringstream() << m) )->str();
            for(int d=0;d<str.length();d++) {
                found[str[d]-'0'] = true;
            }
            /*cout << str << endl;
            for(int d=0;d<10;d++) cout << found[d] << " ";
            cout << endl;
            getchar();*/
            completed = true;
            for(int d=0;d<10;d++) {
                completed &= found[d];
            }
        }
        cout << "Case #" << tc << ": " << m << endl;
    }
    return 0;
}
