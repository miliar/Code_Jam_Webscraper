#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream myReadFile;
    myReadFile.open("input.txt");
    
    int length = 0;
    myReadFile >> length;
    
    int caseNum = 0;
    while(!myReadFile.eof()) {
        caseNum++;
        int row1[4];
        int row2[4];
        int pRow1 = 0;
        int pRow2 = 0;
        
        int temp;
        myReadFile >> pRow1;
        for(int rowNum=1;rowNum <= 4;rowNum++) {
            if(rowNum == pRow1) {
                for(int i=0;i<4;i++) {
                    myReadFile >> row1[i];
                }
            } else {
                for(int i=0;i<4;i++) {
                    myReadFile >> temp;
                }
            }
        }
        myReadFile >> pRow2;
        for(int rowNum=1;rowNum <= 4;rowNum++) {
            if(rowNum == pRow2) {
                for(int i=0;i<4;i++) {
                    myReadFile >> row2[i];
                }
            } else {
                for(int i=0;i<4;i++) {
                    myReadFile >> temp;
                }
            }
        }
        int dup = 0;
        int num = 0;
        for(int i = 0; i<4;i++) {
            for(int j = 0; j<4;j++) {
                if(row1[i] == row2[j]) {
                    dup++;
                    num = row1[i];
                }
            }   
        }
        if(dup == 0) {
            cout << "Case #"<<caseNum<<": Volunteer cheated!" << endl;
        } else if (dup > 1) {
            cout << "Case #"<<caseNum<<": Bad magician!" << endl;
        } else {
            cout << "Case #"<<caseNum<<": " << num << endl;
        }
    }
    return 0;
}