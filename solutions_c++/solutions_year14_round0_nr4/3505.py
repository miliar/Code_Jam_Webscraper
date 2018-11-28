#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

const double kEpsilon = 0.000001;

int deceitfulWar(vector<double> naomi, vector<double> ken, int n) {
    int ret = 0;
    if (naomi.size() < n || ken.size() < n) return 0;

    while (naomi.size() > 0) {
        if (naomi[0] > ken[0]) {
            naomi.erase(naomi.begin());
            ken.erase(ken.begin());
            ret++;
        } else {
            naomi.erase(naomi.begin());
            ken.pop_back();
        }
    }

    return ret;
}
int war(vector<double> naomi, vector<double> ken, int n) {
    int ret = 0;
    if (naomi.size() < n || ken.size() < n) return ret;


    for (int i=0; i<n; i++) {
        bool foundBigKen = false;
        for (int j=0; j<ken.size(); ) {
            if (ken[j] > naomi[i]) {
                ken.erase(ken.begin()+j);
                foundBigKen = true;
                break;
            } else {
                j++;
            }
        }
        if (foundBigKen) {
        } else {
            ret++;
            ken.erase(ken.begin());
        }
    }

    // asert(ken.size() == 0);

    return ret;
}

int main(int argc, char *argv[]) {
    int T = 0;
    cin >> T;
    vector<int> warResult, deceitfulResult;
    for (int t=0; t<T; t++) {
        int n;
        vector<double> naomi, ken;
        cin >> n;
        double temp;
        for (int i=0; i<n; i++) {
            cin >> temp;
            naomi.push_back(temp);
        }
        for (int i=0; i<n; i++) {
            cin >> temp;
            ken.push_back(temp);
        }
        //make the two list sorted
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        //for (int i=0; i<n; i++) {
        //    cout << naomi[i] << " ";
        //}
        //cout << endl;
        //for (int i=0; i<n; i++) {
        //    cout << ken[i] << " ";
        //}
        //cout << endl;

        int result;
        result = deceitfulWar(naomi, ken, n);
        deceitfulResult.push_back(result);


        result = war(naomi, ken, n);
        warResult.push_back(result);
    }
    //cout.precision(7);
    for (int t=0; t<T; t++) {
        cout << "Case #" << t+1 << ": " << deceitfulResult[t] << " " << warResult[t] << endl;
    }
}
