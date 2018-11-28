#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

char output [4001];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    //cout << s.compare(ss); // return 1 is s is down the alphabet from ss

    int n;
    int l,r;
    string s;
    cin >> n;
    cin.ignore();

    for (int i = 1; i <= n; i++) {
        l = 0;
        r= 0;
        memset(output,0,sizeof output);

        cin >> s;
        output[2000] = s[0];

        for (int j = 1; j < s.length(); j++) {
            if (s.substr(j,1).compare(string(1,output[2000-l])) >= 0) {
                output[2000-l-1] = s[j];
                l++;
            }
            else {
                output [2000+r+1] = s[j];
                r++;
            }
        }
        cout << "Case #" << i << ": ";

        for (int j = 2000-l; j <= 2000+r; j++)
            cout << output[j];
        cout << endl;
    }


}
