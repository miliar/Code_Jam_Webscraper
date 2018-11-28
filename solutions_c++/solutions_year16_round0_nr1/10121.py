/*
 * @author Paulostar <paulostar1995@gmail.com>
 * @object code jam purpose
 * Created on 9 avril 2016, 00:07
 */

/* Bleatrix Trotter Problem */

#include <vector>
#include <fstream>
#include <ostream>

using namespace std;


bool verifDigit( int n, int digit){
    int moduloDivPer10 = 0;
    while ( n != 0 ){
        moduloDivPer10 = n%10;
        if ( moduloDivPer10 == digit){
            return true;
        }
        n = n/10;
    }
}

int main(int argc, char** argv) {
    vector<int> numberChoosenArray;
    int testCaseNumber = 0;
    int numberChoosen = 0;
    ifstream inputFile("in.txt");
    ofstream outputfile("out.txt");
    
    if ( inputFile ){
        inputFile >> testCaseNumber;
        for ( int k=0; k<testCaseNumber; k++){
            inputFile >> numberChoosen;
            numberChoosenArray.push_back(numberChoosen);
        }
        
        for ( int i=0; i<testCaseNumber; i++){
            numberChoosen = numberChoosenArray[i];
            if ( numberChoosen != 0 ){
                int multiFactor = 1;
                int maxNumber = 0;
            
                for ( int j = 0; j<10 ; j++ ){
                    multiFactor = 1;
                    while ( verifDigit(multiFactor*numberChoosen,j) == false){
                        multiFactor++;
                    }
                    if ( maxNumber < multiFactor * numberChoosen){
                       maxNumber = multiFactor * numberChoosen;
                    }
                }
                outputfile << " case #"<< i+1 << ": " << maxNumber << endl;  
            }else{
                outputfile << " case #"<< i+1 << ": INSOMNIA" << endl;
            }
            
        }
    }
    
    return 0;
}

