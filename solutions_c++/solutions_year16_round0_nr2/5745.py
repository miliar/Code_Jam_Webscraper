#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        string cookies;
        cin >> cookies;
        char temp;
        int num = 0, j = cookies.length()-1;
        temp = cookies[j];
        if(temp == '-') num++;
        j--;
        for(j; j >= 0; j--)
        {
            if(cookies[j] == temp)
                continue;
            else
            {
                temp = cookies[j];
                num++;
            }

        }
        cout << "Case #" << i << ": " << num << endl;
    }
    return 0;
}
