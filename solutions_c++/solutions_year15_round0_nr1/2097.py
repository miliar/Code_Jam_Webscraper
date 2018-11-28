#include <iostream>
#include <string>

using namespace std;



int main()
{
    int testy;
    string s;
    int n;
    cin>>testy;
    for(int i=1; i<=testy; i++)
    {
        cin >> n >> s;
        int ileakt = 0, iledolozylem = 0;
        for(int i=0; i<s.size(); i++)
        {
            if (s[i] > '0' && ileakt < i)
            {
                iledolozylem += i - ileakt;
                ileakt = i + s[i] - '0';
            }
            else
                ileakt += s[i] - '0';
        }
        cout << "Case #" << i << ": " << iledolozylem << endl;
    }
    
    return 0;
}
