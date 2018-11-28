#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    int T;
    ifstream cin("A-large.in");
    cin>>T;
    for (int i=0;i<T;i++) {
        int n;
        cin>>n;
        if (n==0) {
            cout << "Case #" << i+1 << ": " << "INSOMNIA"<<endl;
            continue;
        }
        vector<int> d(10,0);
        int check = 0;
        int acc = 0;
        while (check!=10) {
            acc += n;
            string s = to_string(acc);
            //cout<<s<<" "<<check<<endl;
            for (int j=0;j<s.size();j++) {
                d[s[j]-'0']++;
                if (d[s[j]-'0']==1)
                    check++;
            }

        }
        cout << "Case #" << i+1 << ": " << acc<<endl;
    }
    return 0;
}