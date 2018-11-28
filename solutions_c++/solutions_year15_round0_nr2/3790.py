#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;

int main()
{
    int z;
    cin >> z;
    for (int k=0; k<z; ++k)
    {
        int n;
        cin >> n;
        vector <int> liczby (n);
        int max = -1;
        for (int i=0; i<n; ++i)
        {
            cin >> liczby[i];
            if (liczby[i]>max) max=liczby[i];
        }
        int min=1000000000;
        for (int i=1; i<=max; ++i)
        {
            int result=i;
            for (int a=0; a<n; ++a)
            {
                result+=(liczby[a]%i==0) ? liczby[a]/i-1 : liczby[a]/i;
            }
            if (result<min) min = result;

        }
        cout << "Case #" << k+1 << ": " << min << endl;
    }
}
