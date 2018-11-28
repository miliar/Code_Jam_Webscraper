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

vector<long long > b(2505,0);
vector<long long > a;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        vector<long long > b(2505,0);
        vector<long long > a;
        int n;
        cin >> n;
        for (int j=0;j<((2*n)-1)*n;j++)
        {
            int x;
            cin >> x;
            b[x]++;
        }
        //cout << b[1]<< endl;
        for (int j=1;j<=2500;j++)
        {
            if ((b[j]%2)==1)
            {
                a.push_back(j);
            }
        }
        sort(a.begin(),a.end());
        cout << "Case #" << i+1 << ": ";
        for (int j=0;j<n-1;j++)
        {
            cout << a[j] << " ";
        }
        cout << a[n-1] << endl;

    }
}
