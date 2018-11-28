#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

void intoSegs(string str, string* myArray, int num) {
    int iter = 0;
    int prevIndex = 0;
    int consumedCharsCount = 0;
    while(iter < num+1){
        int index = str.find(" ", prevIndex);
        if(index > -1){
            myArray[iter] = str.substr(prevIndex, index-consumedCharsCount);
            consumedCharsCount += myArray[iter].size() +1;
            prevIndex = index +1;
            iter++;    
        } else {
            break;
        }                    
    }
    
    myArray[num] = str.substr(prevIndex, str.size() -1);
    
    return;
}

bool isPal(string strnum){
     for(int i = 0; i< (strnum.length()/2) +1 ; i++)
        if ((strnum[i]) != strnum[strnum.length() -1 -i]) return 0;
     return 1;
     }

     
bool isSquareAndPal(double num) { 
     float root = sqrt(num);
     stringstream myss (stringstream::in | stringstream::out);
     myss << root;
     string stroot = myss.str();
     return((root == floorf(root))&&(isPal(stroot)));
}

int main(){
    ifstream file("C-small-attempt0.in");
    ofstream file2("Output.out");
    string strNumCases;
    int numCases;
    getline(file, strNumCases);
    istringstream(strNumCases) >> numCases;
    for (int i = 0; i < numCases; i++){
        string str ;
        getline(file, str);
        string segments[2];
        intoSegs(str, segments, 1);
        int counter = 0;
        for (int it = atoi(segments[0].c_str()); it < atoi(segments[1].c_str())+1;it++ ){
            string strit ;
            stringstream ss;
            ss << it;
            strit = ss.str();
            if ((isSquareAndPal(it))&&(isPal(strit))) counter++;
            }
        file2 << "Case #" << i+1 << ": " << counter << endl;
        }
    file.close();
    file2.close();
    system("PAUSE");
    return 0;
    }
