

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{
    string caseNumber;
    int cn = 0;
    
    string tempAns1;
    string tempAns2;
    int rowAns1;
    int rowAns2;
    
    string cardNumber;
    string cardNumber1;
    int initialArray[4][4];
    int compareArray[4][4];
    
    int count = 0;
    
    int result = 0;
    string ans;
    
    
    ifstream myfile ("A-small-attempt3.in.txt");
    if (myfile.is_open())
    {
        do {
            getline(myfile, caseNumber);
            cout << caseNumber << "\n";
            istringstream(caseNumber) >> cn;
        } while (cn == 0);
        
        string results[200];
        
        for (int i = 0; i < cn; i++) {
            getline(myfile, tempAns1);
            istringstream(tempAns1) >> rowAns1;
            cout << rowAns1 << "\n";
            for (int x = 0; x < 4; x++) {
                getline(myfile, cardNumber);
                cout << cardNumber << "\n";
                stringstream ssin(cardNumber);
                vector<int> out;
                int j;
                while (ssin >> j) {
                    out.push_back(j);
                }
                for (size_t k = 0; k < out.size(); k++) {
                    initialArray[x - 1][k] = out[k];
                }
            }
            
            getline(myfile, tempAns2);
            istringstream(tempAns2) >> rowAns2;
            cout << rowAns2 << "\n";
            for (int y = 0; y < 4; y++) {
                getline(myfile, cardNumber1);
                cout << cardNumber1 << "\n";
                stringstream si(cardNumber1);
                vector<int> out;
                int m;
                while (si >> m) {
                    out.push_back(m);
                }
                for (size_t t = 0; t < out.size(); t++) {
                    compareArray[y - 1][t] = out[t];
                }
            }
            
            count = 0;
            
            for (int l = 0; l < 4; l++) {
                for (int p = 0; p < 4; p++) {
                    if (initialArray[rowAns1 - 2][l] == compareArray[rowAns2 - 2][p]) {
                        result = initialArray[rowAns1 - 2][l];
                        count++;
                    }
                }
            }
            
            if (count == 0) {
                ans = "Volunteer cheated!";
            } else if (count == 1) {
                ostringstream oss;
                oss << result;
                ans += oss.str();
            } else {
                ans = "Bad magician!";
            }
            results[i] = ans;
            ans.clear();
        }
        
        ofstream output ("out.txt");
        if (output.is_open()) {
            for (int z = 0; z < cn; z++) {
                output << "Case #" << z + 1 << ": " << results[z] << "\n";
            }
        }
        output.close();
    }
    
    return 0;
}
