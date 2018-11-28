#include <iostream>

using namespace std;

int main()
{
    int t;
    int k[100][1000];
    int s[100];
    char c;

    cin>>t;
    for (int i = 0; i < t; i++)
    {
        cin>>s[i];
        cin.ignore(1,'\0');
        for (int j = 0; j <= s[i]; j++)
        {
            cin.get(c);
            k[i][j] = c-'0';
        }
    }

    int f;
    int n;

    for (int i = 0; i < t; i++)
    {
        f = 0;
        n = 0;
        for (int j = 0; j <= s[i]; j++)
        {
            if (k[i][j] > 0 && j > n) {
                f+= j-n;
                n+= j-n;
            }
            n+= k[i][j];
        }
        printf("Case #%d: %d\n", i+1, f);
    }
    return 0;
}
