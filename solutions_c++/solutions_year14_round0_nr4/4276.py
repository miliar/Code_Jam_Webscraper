#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int testcase(0); testcase != t; ++testcase) {
        cout << "Case #" << testcase + 1 << ": ";
        int n;
        cin >> n;
        vector<double> naomi;
        for(int i(0); i != n; ++i) {
            double temp;
            cin >> temp;
            naomi.push_back(temp);
        }
        vector<double> ken;
        for(int i(0); i != n; ++i) {
            double temp;
            cin >> temp;
            ken.push_back(temp);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        //compute Naomi's points for war
        int war_score = 0;
        int ken_index = 0;
        for(int i(0); i != n; ++i) {
            while(ken_index < n && ken[ken_index] < naomi[i]) {
                ++war_score;
                ++ken_index;
            }
            ++ken_index;
        }
        //compute points for deceit war
        int deceit_score = 0;
        int naomi_index = 0;
        ken_index = 0;
        while(naomi_index < n && ken_index < n) {
            if(naomi[naomi_index] > ken[ken_index]) {
                ++deceit_score;
                ++ken_index;
            }
            ++naomi_index;
        }
        cout << deceit_score << " " << war_score << endl;
    }
}
