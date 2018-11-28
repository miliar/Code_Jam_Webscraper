#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;

int t, ans;

int n;
vector<string> ss;

int L[101][101]; 
int P[101][101];

//A
int main()
{
    cin >> t;
    
    for (int c = 1; c <= t; c++)
    {
        cin >> n;
        ss = vector<string>(n);
        for (int i = 0; i < n; i++)
        {
            cin >> ss[i];
        }  

        string s1 = ss[0];
        string s2 = ss[1];

        if (s1.length() < s2.length())
            std::swap(s1, s2); 

        int ans = 0;
        int l1 = 0, l2 = 0;
        bool valid = true;

        while (l1 < s1.length())
        {
            if (s1[l1] != s2[l2])
            {
                valid = false;
                break;
            }

            char cur = s1[l1];

            int c1 = 1, c2 = 1;
            while (l1 < s1.length() && s1[l1 + 1] == cur) { l1++; c1++; }
            while (l2 < s2.length() && s2[l2 + 1] == cur) { l2++; c2++; }

            ans += abs(c1 - c2);

          //  cerr << "cur = "<<cur<<" c1 = " << c1 << " c2 = " << c2 << endl;
          //  cerr << "ans = " << ans << endl;

            l1++;
            l2++;
        }

        // cout << L[ss[0].length()][ss[1].length()] << endl;

      

        cout << "Case #" << c << ": ";

        if (valid)
            cout << ans << endl;
        else
            cout << "Fegla Won" << endl;
    }
    return 0;
}

////////////////////////////////////////////////////////////
// B
////////////////////////////////////////////////////////////
//int main()
//{
//    cin >> t;
//    int a, b, k;
//    for (int c = 1; c <= t; c++)
//    {
//        cin >> a >> b >> k;
//
//        ans = 0;
//
//        if (a > b) std::swap(a, b);
//
//        for (int i = 0; i < a;i++)
//        for (int j = 0; j < b; j++)
//        {
//            int s = i&j;
//            if (s < k)
//                ans++;
//        }
//        cout << "Case #" << c << ": " << ans << endl;
//    }
//    return 0;
//}