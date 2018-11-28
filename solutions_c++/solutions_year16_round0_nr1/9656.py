#include <iostream>
#include <string>
#include <cstring>
#include <vector>


using namespace std;


int main()
{
        int nt;
        cin >> nt;
        for (int i = 1; i <= nt; i++) {
                cout << "Case #" << i << ": ";
                int n;
                //cin >> n;
                //int nn = n;
                vector<int> v;
                string s;
                cin >> s;
                for (int j = s.size() -1; j >=0; j--) {
                        v.push_back(s[j] - '0');
                }
                /*
                if (nn == 0) {
                        v.push_back(0);
                }
                while (nn) {
                        int digit = nn % 10;
                        v.push_back(digit);
                        nn = nn / 10;
                
                }
                */
                vector<bool> visited(10, false);
                int cnt = 10;
                vector<int> vv;
                for (int j = 1; j < 1000 && cnt; j++) {
                        int carry = 0;
                        vv.clear();
                        for (int k = 0; k < v.size(); k++) {
                                int tmp = v[k] * j + carry;
                                vv.push_back(tmp % 10);
                                if (!visited[vv[k]]) {
                                        visited[vv[k]] = true;
                                        cnt--;
                                }
                                carry = tmp / 10;
                        }
                        while (carry) {
                                int tmp = carry;
                                vv.push_back(tmp % 10);
                                if (!visited[vv.back()]) {
                                        visited[vv.back()] = true;
                                        cnt--;
                                }
                                carry = tmp / 10;
                        }
                }
                if (cnt) {
                        cout << "INSOMNIA\n";
                } else if (vv.size() > 0) {
                        for (int j = vv.size() -1; j >= 0; j--) 
                                cout << vv[j];
                        cout << endl;
                }
        }
}
