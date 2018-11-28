#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int k=1; k<=T; k++)
    {
        int Sm;
        cin >> Sm;
        string s;
        cin >> s;
        int tot = s[0]-'0';
        int ext = 0;
        for(int i=1; i<=Sm; i++)
        {
            if(s[i]=='0') continue;
            if(i>tot) {ext+=(i-tot); tot=i;}
            tot += (s[i]-'0');
        }
        cout << "Case #" << k << ": " << ext << endl;
    }
    return 0;
}
