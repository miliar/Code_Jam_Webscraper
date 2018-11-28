#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int t_i = 0; t_i < n; t_i++)
    {
        int k, c, s;
        cin >> k >> c >> s;

        cout << "Case #" << t_i + 1 << ":";
        
        for (int i = 1; i < k + 1; i++)
            cout << " " << i;

        cout << endl;
    }

}
