#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int k=1;k<=t;k++)
    {
        int l;
        string s;
        cin >> l >> s;
        int licz=s[0]-'0';
        int extra=0;
        for(int i=1;i<=l;i++)
        {
            if(s[i]-'0'>0 && licz<i)
            {
                extra+=i-licz;
                licz=i;
            }
            licz+=s[i]-'0';
        }
        cout << "Case #" << k << ": " << extra << endl;
    }
    return 0;
}

