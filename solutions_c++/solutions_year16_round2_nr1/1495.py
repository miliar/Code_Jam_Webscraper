#include <iostream>
#include <string>

using namespace std;

int numc[26];
int ans[10];

string harf[10] = {"ZERO", "XSI", "GEIHT","HTREE",  "SEVEN",  "VFIE", "FOUR", "TWO", "ONE", "NINE"};
int in[10] = {0, 6, 8, 3, 7, 5, 4, 2, 1, 9};
int cindex(char x)
{
    return x-'A';
}

int main()
{
    int testc = 0;
    int t; cin>>t;
    while (t--) {
        string s; cin>>s;
        testc++;
        memset(numc , 0, sizeof numc);
        memset(ans , 0, sizeof ans);
        for (int i =0; i < s.size(); ++i)
            numc [ cindex(s[i]) ] ++;

        for (int i =0; i < 10; ++i ) {

            string t = harf[i];
            while ( numc[cindex(t[0])] ) {

                for (int j = 0; j < t.size(); ++j) 
                    numc[cindex(t[j])]--;

                ans[in[i]]++;
            }
        }
        cout << "Case #" << testc << ": ";
        for (int i = 0; i < 10; ++i) 
            while(ans[i]) {
                cout << i;
                ans[i]--;
            }
        cout << endl;
    }
    return 0;
}
