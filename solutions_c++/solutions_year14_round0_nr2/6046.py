#include <iostream>

using namespace std;

int main()
{
    int N, i;
    double c, f, x, z, y, t, ti;
    
    cin >> N;
    cout.precision(7);
    for (i = 1; i <= N; i++)
    {
        cin >> c >> f >> x;
        y = 0.0; z = 2.0;
        ti = y + (x / z);
        while(true)
        {
            t = ti;
            y += c / z;
            z += f;
            ti = y + (x / z);
            if (t < ti)
                break;
        }
        cout << "Case #" << i << ": " << fixed << t << endl;
    }
}
