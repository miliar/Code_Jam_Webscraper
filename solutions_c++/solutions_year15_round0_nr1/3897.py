#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    int t;
    cin >> t;
    for (int k=0; k<t; ++k)
    {
        int Smax;
        cin >> Smax;
        string wejscie;
        cin >> wejscie;
        vector <int> liczby (Smax+1);
        for (int i=0; i<wejscie.size(); ++i)
        {
            liczby[i]=(int)wejscie[i]-48;
        }
        int ile = 0;
        int result = 0;
        for (int i=0; i<=Smax; ++i)
        {
            if (ile<i)
            {
                result+=i-ile;
                ile=i;
            }
            ile+=liczby[i];
        }
        cout << "Case #" << k+1 << ": " << result << endl;
    }
}
