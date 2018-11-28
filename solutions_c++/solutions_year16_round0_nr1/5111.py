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

string int_to_str(int val)
{
    string res;
    ostringstream convert;
    convert << val;
    res = convert.str();
    return res;

}



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        int v;
        cin >> v;
        if (v==0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }
        vector<int > a(10,0);
        int cnt=0;
        int x=0;
        while (cnt!=10)
        {
        x=x+v;
        int k=x;
        while (k)
        {
            if (a[k%10]==0){a[k%10]=1;cnt++;}
            k/=10;
        }

        }
        cout << "Case #" << i+1 << ": " << x << endl;

    }
}
