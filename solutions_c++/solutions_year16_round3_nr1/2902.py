#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    int T;
    fstream cin("A-small-attempt0.in");
    cin>>T;
    for (int i=1;i<=T;i++) {
        int n;
        cin>>n;
        vector<int> p(n);
        string ans;
        for (int j=0;j<n;j++)
            cin>>p[j];
        int max1 = 0,max2 = 0,j1,j2;
        int check = 0;
        while (check!=n) {
            max1 = 0;
            max2 = 0;
            for (int j=0;j<n;j++) {
                if (p[j]>max1) {
                    max1 = p[j];
                    j1 = j;
                }
                if (p[j]>max2 && j!=j1) {
                    max2 = p[j];
                    j2 = j;
                }
            }

            p[j1] --;
            p[j2] --;
            if (p[j1]==0) check++;
            if (p[j2]==0) check++;
            //cout<<j1<<" "<<j2<<endl;
            if (check==n-1) {
                p[j2]++;
                check--;
                ans.push_back(j1+'A');
                ans.push_back(' ');
            } else {
                ans.push_back(j1+'A');
                ans.push_back(j2+'A');
                ans.push_back(' ');
            }
        }

        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}