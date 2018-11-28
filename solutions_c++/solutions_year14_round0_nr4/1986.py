#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{   ofstream output("solved.out");
    ifstream input("test.in");
    int test_cases;
    input >> test_cases;
    for (int iterate = 0; iterate < test_cases; iterate++) {
    int size;
    input >> size;
    double block;
    vector<double> naomi;
    vector<double> ken;

    for (int i = 0; i < size; i ++) {
        input >> block;
        naomi.push_back(block);
    }

      for (int i = 0; i < size; i ++) {
        input >> block;
        ken.push_back(block);
    }

    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());


    int k = 0;
    int n = 0;
    int points_dwar = 0;
    int points_war = 0;

        for (n; n < size;) {
            if (naomi[n] > ken[k]) {
                points_dwar++;
                k++;

            }

        n++;

        }

        n = size-1;
        k = size-1;

        for(n; n>=0;) {
            if(naomi[n] > ken[k]) {
                points_war++;
               k++;
            }
            n--;
            k--;
        }

    output << "Case #" << iterate+1 << ": " << points_dwar << " " << points_war << endl;
    }
    return 0;
}
