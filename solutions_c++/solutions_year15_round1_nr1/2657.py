#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        int n;
        cin >> n;
        int m[n];
        for(int j=0; j<n; j++)
            cin >> m[j];
        int y=0, z=0, mm=0;
        for(int j=0; j<n-1; j++)
        {
            if(m[j]-m[j+1] > 0)
                y += m[j]-m[j+1];
            if(m[j]-m[j+1] > mm)
                mm = m[j]-m[j+1];
        }
        for(int j=0; j<n-1; j++)
        {
            if(m[j] > mm)
                z += mm;
            else
                z += m[j];
        }

        cout << "Case #" << i+1 <<": "<< y <<' '<< z << endl;
    }
    return 0;
}
