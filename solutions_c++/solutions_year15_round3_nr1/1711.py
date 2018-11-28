#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int n,m,w,t;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (int k = 1; k <= t; ++k)
    {
        cin >> n >> m >> w;
        cout << "Case #" << k << ": " << (ceil(1.*m/w) + w-1)*n << endl;
    }
    return 0;
}
