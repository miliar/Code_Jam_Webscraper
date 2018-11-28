#include <iostream>
#include <string>

using namespace std;

int min2 (int a, int b) {
    if (a<b) return a;
    else return b;
}

int max2 (int a, int b) {
    if (a>b) return a;
    else return b;
}

int main()
{
    int t, k, i, j, m, impossible;
    int solution[1000], y, length, currsum;
    string s;
    cin >> t;
    for (i=1; i<=t; i++) {
        cin >> s >> k;
        length=s.length();
        impossible=0;
        for (j=0; j<=length-k; j++) solution[j]=-1;
        //j=0
        solution[0]=(s[0]=='-');  //1 if '-', 0 if '+'
        for (j=1; j<length; j++) {
            //cout << "j=" << j << endl;
            if (j<=length-k) {//solution not filled out; keep generating solution
                currsum=0;
                for (m=max2(0, j-k+1); m<min2 (j, length-k); m++) currsum+=solution[m];
                //cout << s[j];
                //cout << "currsum=" <<currsum <<endl;
                solution[j]=(( (s[j]=='-')   -currsum + 2000)%2);
            } else {//solved; check for contradiction
                currsum=0;
                for (m=max2(0, j-k+1); m<=length-k; m++) currsum+=solution[m];
                if (( (s[j]=='-')   -currsum)%2!=0) {
                    impossible=1;
                    break;
                }
            }
        }
        if (impossible) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else {
            y=0;
            //for (j=0; j<=length-k; j++) cout << solution[j] << " " ;
            //cout << endl;
            for (j=0;j<=length-k;j++) y+=solution[j];
            cout << "Case #" << i << ": " << y << endl;
        }
    }
    return 0;
}
