#include <iostream>
#include <string>

using namespace std;
int f(string w) {
    int aP[1024];
    int aN[1024];

    if (w[0] == '+') {
        aP[0] = 0;
        aN[0] = 1;
    }
    else {
        aP[0] = 1;
        aN[0] = 0;
    }

    for (int i = 1; i< w.size(); i++)
        if (w[i] == '+') {
            aP[i] = aP[i-1];
            aN[i] = aP[i-1]+1;
        }
        else {
            aP[i] = aN[i-1]+ 1;
            aN[i] = aN[i-1];
        }
    return aP[w.size()-1];
}
int main() {
    int nn;
    cin >> nn;
    for (int i = 1; i<=nn; i++) {
        cout << "Case #"<<i<<": ";
        string t;
        cin >> t;
        cout << f(t)<< endl;
    }



}
