
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    //-- check if the files were opened successfully 
    //if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    //if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int T;
    fin >> T;
    const unsigned NDIGITS = 10;
    for (int i = 1; i <= T; ++i) {
        int N;
        fin >> N;
        bool allSee = false;
        unsigned j = 1;
        string answer = " ";
        bool digits[NDIGITS] = {false};
        while(!allSee){ 
            if(N == 0){
                answer = "INSOMNIA";
                allSee = true;
            }
            else{
                allSee = true; // need to be true to do &&
                for(unsigned k = 0; k < NDIGITS; k++){
                    allSee &= digits[k];
                }
                answer = to_string(N*(j-1));
                int temp = N * j;
                do {
                    int digit = temp % 10;
                    digits[digit]= true;
                    temp /= 10;
                } while (temp > 0);
                j++; 
            }
        }
        fout << "Case #" << i << ": "<< " " << answer << endl;  
    }
}