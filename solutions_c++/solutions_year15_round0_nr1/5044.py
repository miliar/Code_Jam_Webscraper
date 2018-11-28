#include <bits/stdc++.h>
using namespace std;

long long int has[1005] = {0},arr[1005];

int main() {

    long long int t,sm,c,i,counter;
    string str,tmp;
    cin >> t;
    for (c=1;c<=t;c++) {
        str = tmp;
        cin >> sm >> str;
        has[0] = str[0] - '0';
        arr[0] = str[0] - '0';
        //cout << has[0] << " ";
        for (i=1;i<=sm;i++) {

            has[i] = has[i-1] + str[i] - '0';
            arr[i] = str[i] - '0';
            //cout << has[i] << " ";

        }
        //cout << endl;
        counter = 0;
        //cout << counter << " ";
        for (i=1;i<=sm;i++) {

            if (i > has[i-1] + counter) {

                counter = counter + i - has[i-1] - counter;

            }
            //cout << counter << " ";

        }
        //cout << endl;

        cout << "Case #" << c << ": " << counter << endl;

    }

}
