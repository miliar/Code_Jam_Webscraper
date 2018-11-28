#include <bits/stdc++.h>
using namespace std;

// bool wayToSort(int i, int j) { return i > j; }

int main()
{
    ofstream outfile;
    ifstream inpfile;
    inpfile.open("A-large.in");
    outfile.open("outputLarge.txt");

    int t, counter = 1;
    inpfile >> t;
    while (t > 0)
    {
        string s, ans;
        inpfile >> s;

        int n = s.length();
        ans.push_back(s[0]);
        for (int i = 1; i < n; i++)
        {
            if (s[i] >= ans[0])
            {
                // append at the begining
                string temp;
                temp.push_back(s[i]);
                temp.append(ans);
                ans = temp;
            }
            else
            {
                ans.push_back(s[i]);
            }
        }
        outfile << "Case #" << counter << ": " << ans << endl;
        counter++;
        t--;
    }

    outfile.close();
    inpfile.close();

    return 0;
}
