// Compiled with gcc in Ubuntu 16.04 with c++11 features.

#include <stdint.h>

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int main (int, char*[])
{
    int num_of_cases;
    std::cin >> num_of_cases;
    std::string str;
    std::getline(std::cin, str);

    for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
        std::cout << "Case #" << case_num << ": ";
        int n, k;
        std::cin >> n >> k;

        std::vector<double> prob(n);
        for (int i=0; i<n; ++i)
            std::cin >> prob[i];

        std::sort(prob.begin(), prob.end());

        double maxprob = 0;
        for (int mins = 0; mins <= k; ++mins) {
            std::vector<double> pdf(k+1);
            pdf[0] = 1.0f;
            for (int i = 0; i < mins; ++i) {
                std::vector<double> pdfnew(k+1);
                for (int j = 0; j < k ; ++j) {
                    pdfnew[j] += pdf[j] * (1.0f - prob[i]);
                    pdfnew[j+1] += pdf[j] * prob[i];
                }
                pdf = pdfnew;
            }
            for (int i = n - k + mins; i < n; ++i) {
                std::vector<double> pdfnew(k+1);
                for (int j = 0; j < k ; ++j) {
                    pdfnew[j] += pdf[j] * (1.0f - prob[i]);
                    pdfnew[j+1] += pdf[j] * prob[i];
                }
                pdf = pdfnew;
            }
            maxprob = std::max(maxprob, pdf[k/2]);
        }

        cout << maxprob << endl;
    }

    return 0;
}