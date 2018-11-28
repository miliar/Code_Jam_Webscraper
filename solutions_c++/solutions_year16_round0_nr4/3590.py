#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>


using namespace std;

//vector<long long > a,b;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i+1 << ": ";
        for (int j=1;j<s;j++)
        {
            cout << j << " ";
        }
        cout << s << endl;


    }
}
