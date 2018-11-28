#include <iostream>
#include <cstdlib>
#include <math.h>
using namespace std;
typedef long long int ll;
int main()
{
    int t, len;
    char a[1001], b[1001];
    cin>>t;
    for (int x = 1; x <= t; x++)
    {
        cin>>a;
        cout<<"Case #"<<x<<": ";
        for (len = 0; a[len] != '\0'; len++);
        for (int i = 0; i < len; i++)
        {
            if (i == 0)
                b[i] = a[i];
            else
            {
                if (a[i] >= b[0])
                {
                    for (int j = i; j > 0; j--)
                    {
                        b[j] = b[j-1];
                    }
                    b[i+1] = '\0';
                    b[0] = a[i];
                }
                else
                    b[i] = a[i];
            }
        }
        for (int i = 0; i < len; i++)
            cout<<b[i];
        cout<<endl;
    }
}
