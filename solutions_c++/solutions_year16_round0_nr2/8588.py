#include <iostream>

using namespace std;

int main()
{
    int t, m;
    cin >> t;
    string s;
    char p;
    for(int i = 1; i <= t; i++)
    {
        cin >> s;
        p = s[0];
        m = 0;
        for(int j = 1; j < s.length(); j++){
            if(p != s[j]){
                m++;
                p = s[j];
            }
        }
        if(p == '-')
            m++;
        cout << "Case #" << i << ": " << m << endl;
    }
    return 0;
}
