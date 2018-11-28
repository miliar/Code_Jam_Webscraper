#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for(int ii = 1; ii<=n; ++ii) {
        vector<bool> digit(10, false);
        int num, Num; string numStr;

        cin >> num;
        printf("Case #%d:  ",ii);
        if (num == 0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }

        Num = 0;
        bool check;
        int cnt = 0;
        do {
            Num+=num; ++cnt;
            ostringstream convert;
            convert << Num;
            numStr = convert.str();

            for(int c = 0; c<numStr.size(); ++c)
                digit[numStr[c]-'0'] = true;

            check=true;
            for(int i = 0; i<10; ++i)
                if(!digit[i]) check = false;

        } while(!check);
        cout<<Num<<endl;
    }
    return 0;
}
