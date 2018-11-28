#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long myLong;
//  myLong max = 18446744073709551615ULL;
//  myLong can be used upto 10 ^ 19.


#define For(i,n) for (int i=1;i<(int)(n+1);i++) 
#define FOR(i,n) for (int i=0;i<(int)(n);i++) 

void solve_case()
{
    string a;
    long n;

    cin >> a >> n;
    
    long l = a.size();
    
    char v_pos[l];
    for (long i=0; i < l; i++)
        if (a[i] == 'a' || a[i] == 'e' ||a[i] == 'i' ||a[i] == 'o' ||a[i] == 'u')
            v_pos[i] = '1';
        else
            v_pos[i] = '0';
    
    string c = "";
    for (long i=0; i < n; i++)
        c+= "0";

    string s(v_pos);

    unsigned long long res = 0;

    for (long i = 0; i < l; i++)
        for (long j = n; i+ j <= l; j++)
        {
//            cout << i << "   " << j << "    " << n << endl;
//            cout << s << endl;
            string s1 = s.substr(i,j);
            if (s1.find(c) != string::npos)
                res++;
        }
    cout << res;
}

main()
{
    unsigned int tests;
    cin >> tests;
    for (unsigned int tests_index = 1; tests_index < tests +1; tests_index++)
    {
        cout << "Case #" << tests_index << ": ";
        solve_case();
        cout << endl;
    }

}
