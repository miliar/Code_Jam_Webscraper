
#include <iostream>
#include <string>

using namespace std;


int main()
{
    ios_base::sync_with_stdio(0);

    int z;
    cin >> z;
    for(int j=1; j<=z; j++)
    {
        int stand = 0, add = 0;

        int smax;
        cin >> smax;

        string s;
        cin >> s;

        for(int i=0; i<s.size(); i++)
        {
            if(stand + add < i)
                add += (i - stand - add);

            stand += (s[i] - '0');
        }

        cout << "Case #" << j << ": " << add << endl;
    }

    return 0;

}
