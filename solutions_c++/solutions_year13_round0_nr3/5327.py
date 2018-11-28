#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
using namespace std;

string ntos ( int num ){
	stringstream ss;
	ss << num;
	return ss.str();
}

bool ispalindrome(string n){
    int i=0, j=0;
    while(j<n.length()){
        if(n.at(i) == n.at(n.length()-1-i)){
            i++;
        }
        j++;
    }
    return (i== n.length()) ? true:false;
}

int main(void){
ifstream fin ("C-small-attempt0.in");
ofstream fout ("output.out");

int T, counter;

unsigned long long int A, B;

fin >> T;

for(int i=0; i<T; i++){
    counter = 0;

    fin >> A >> B;

    for(unsigned long long int j = A ; j <= B; j++){
        string js = ntos(j);
        int lastdig = j%10;

        if(lastdig == 2 || lastdig == 3 || lastdig == 7 || lastdig == 8){
            continue; //square number can end only with digits 0,1,4,6,9, or 25 in base 10,
        }

        if(ispalindrome(js)){
            unsigned long long int root = (unsigned long long int) sqrt((double) j);
            if((root * root == j) || ((root+1) * (root+1) == j)){  // in case of an off-by-one float error
                 if(ispalindrome(ntos(root))){
                    counter++;
                 }
            }
        }
    }

    fout << "Case #" << (i+1) << ": " << counter;
    if(i!= (T-1)){
        fout << endl;
    }
}


return 0;
}
