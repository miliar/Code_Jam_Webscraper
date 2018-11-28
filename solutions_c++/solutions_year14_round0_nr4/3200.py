#include <algorithm>
#include <iostream>
#include <istream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
    ifstream reader("input.txt");
	ofstream writer("output.txt");
	int t, n, Optomi, Dectomi;
    double temp;
    reader >> t;
    for(int i = 0; i < t; i++) {
        vector<double> omi, omi1;
        vector<double> ken, ken1;
        vector<double>::iterator omiIt;
        vector<double>::iterator kenIt;
        reader >> n;
        Optomi = Dectomi = 0;
        for(int j = 0; j < n; j++) {
            reader >> temp;
            omi.push_back(temp);
            omi1.push_back(temp);
        }
        for(int j = 0; j < n; j++) {
            reader >> temp;
            ken.push_back(temp);
            ken1.push_back(temp);
        }
        sort(omi.begin(), omi.end());
        sort(ken.begin(), ken.end());
        sort(omi1.begin(), omi1.end());
        sort(ken1.begin(), ken1.end());
        for(int j = 0; j < n; j++) {
            omiIt = omi.end() - 1;
            kenIt = ken.end() - 1;
            if(*omiIt > *kenIt) {
                Optomi++;
                omi.erase(omi.end() - 1);
                ken.erase(ken.begin());
            }
            else {
                omi.erase(omi.end() - 1);
                ken.erase(ken.end() - 1);
            }
        }
        for(int j = 0; j < n; j++) {
            omiIt = omi1.begin();
            kenIt = ken1.begin();
            if(*omiIt > *kenIt) {
                Dectomi++;
                omi1.erase(omi1.begin());
                ken1.erase(ken1.begin());
            }
            else {
                omi1.erase(omi1.begin());
                ken1.erase(ken1.end() - 1);
            }
        }
    writer << "Case #" << i + 1 << ": " << Dectomi << " " << Optomi << endl;
    }
    return 0;
}
