#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
typedef long long ll;

#define FR(i,en) for(int i=0; i<(int)(en); i++)
#define FOR(i,st,en) for(int i=(st); i<(int)(en); i++)

int main()
{
    int firstfour[4];
    int t,tmp,rowselected,res,rescount;
    cin >> t;
    FR (test_cases,t) {
        cout << "Case #" << test_cases+1 << ": ";
        cin >> rowselected;
        FR(i,4) FR(j,4) 
            if (i+1==rowselected) cin >> firstfour[j];
            else cin >> tmp;
        rescount = 0;
        cin >> rowselected;
        FR(i,4) FR(j,4) {
            cin >> tmp;
            if (i+1==rowselected) {
                FR(k,4) if (firstfour[k]==tmp) {
                  rescount++;
                  res=tmp;
                }
            }
        }
        if (rescount==0) cout << "Volunteer cheated!\n";
        if (rescount==1) cout << res << "\n";
        if (rescount>=2) cout << "Bad magician!\n";
    }
    return 0;
}
