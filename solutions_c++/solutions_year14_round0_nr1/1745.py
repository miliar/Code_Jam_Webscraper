#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    std::istream& in = std::cin;

    int cases; 
    in >> cases;
    
    int case_no = 0;
    while(case_no != cases) {
        case_no += 1;

        int arr1[4][4];
        int arr2[4][4];
    
        int ans1, ans2;
        in >> ans1;
        for (int i=0; i<4; ++i)         
            for (int j=0; j<4; ++j)
                in >> arr1[i][j];

        in >> ans2;

        for (int i=0; i<4; ++i)         
            for (int j=0; j<4; ++j)
                in >> arr2[i][j];

        
        bool found = false;
        bool unique = true;
        int no = -1;

        for (int i=0; i < 4; ++i) {
            for (int j=0; j < 4; ++j) {
                if (arr1[ans1-1][i] == arr2[ans2-1][j]) {
                    if (found == true) {
                        unique = false;
                    }
                    found = true;
                    no = arr1[ans1-1][i];
                }
            }
        }
        
        cout << "Case #" << case_no << ": ";
        if (found && unique) {
            cout << no << endl;
        } else if (found && !unique) {
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }

    }
}
