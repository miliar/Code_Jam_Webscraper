#include <iostream>
#include <string>

using namespace std;

int main()
{
    int cases;
    cin >> cases;

    for(int c=1; c<=cases; c++)
    {
        int m;
        string s;
        cin >> m >> s;
        
        int f = 0;
        int u = 0;

        for(int i=0; i<=m; i++)
        {
            if(i > (u+f))
            {
                f += i-(u+f);
            }

            u += s[i]-'0';
        }

        cout << "Case #" << c << ": " << f << endl;
    }

    return 0;
}
