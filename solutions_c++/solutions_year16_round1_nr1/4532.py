#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int test_cases;
    cin >> test_cases;

    for(int i = 1; i <= test_cases; i++) {
        cout << "Case #"<<i<<": ";
        
        string s;
        vector<string> sv;
        cin >> s;
        char c = s[0];
        string first(&c);
        sv.push_back(first);
        for(int j = 1; j < s.length(); j++) {
            vector<string> v;
            for(int k = 0; k < sv.size(); k++) {
                string tmp = sv[k];
                string tmp1 = tmp + s[j];
                string tmp2 = s[j] + tmp;
                v.push_back(tmp1);
                v.push_back(tmp2);                
                //cout << tmp1 << ": :" << tmp2 << endl;
            }
            sv.clear();
            sv = v;
        }
        sort(sv.begin(), sv.end());
        cout << sv[sv.size() - 1] << endl;
    }
    return 0;                
}
