//postfix calculator

#include <iostream>
#include <vector>
#include <utility> 
#include <algorithm>
#include <fstream>
#include <iostream>     // std::cout, std::fixed
#include <iomanip> 

using namespace std;

bool smaller(const pair <char, double> &i, const pair <char,double> &j) {
    return i.second < j.second;
}

int main() {
    ofstream fOutput;
    fOutput.open ("result.out");
    //number, money
    int testCases,n;
    double temp;
    cin >> testCases;
    for (int i = 1; i <= testCases; i++) {
        cin >> n;
        vector < pair <char,double> > items;
        for (int k = 1; k <= n; k++) {
            cin >> temp;
            items.push_back(make_pair('n', temp));
        }
        for (int k = 1; k <= n; k++) {
            cin >> temp;
            items.push_back(make_pair('k', temp));
        }

        sort(items.begin(), items.end(), smaller);

        int war = 0; int ken = 0;
        for (int l = (n*2) -1; l >= 0; l--) {
            if (items[l].first == 'n' && ken <= 0) {
                war++;
            } else if (items[l].first == 'n' && ken > 0) {
                ken--;
            } else {
                ken++;
            }
        }
        int dec = 0; ken = 0;
        for (int l = 0; l < n*2; l++) {
            if(items[l].first == 'k') {
                ken++;
            } else { //=='n'
                if (ken > 0) {
                    dec++;
                    ken--;
                }
            }
        }
        fOutput << "Case #" << i << ": ";
        fOutput << dec << " " << war << endl;

    }

    return 0;
        
}
