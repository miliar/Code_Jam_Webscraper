#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <string>
#include <climits>
#include <algorithm>

using namespace std;

int main()
{
    int times;
    int a,b,c;
    cin >> times;
    for(int i = 1; i <= times;i++)
    {

        cin >> a >> b >> c;
        cout << "Case #" << i << ":";
        for(int j = 1; j <= a; j++)
        {
            cout << " "<< j;
        }
        cout << endl;
    }

}
