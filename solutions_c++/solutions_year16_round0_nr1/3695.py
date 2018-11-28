#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char* args[]){
    ifstream infile;
    ofstream outfile;
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        infile.open("small.in");
        outfile.open("small.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        infile.open("large.in");
        outfile.open("large.out");
    }
    
    int cases;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    int orig_number;
    
    for (int i=0; i<cases; ++i) {
        int digits[10]={};
        int finished = 0;
        // read from file
        infile >> orig_number;
        //cout << stack << endl ;
        int round = 0;
        while (!finished){
            round++;
            int number = orig_number*round;
            if (number == 0) break;
            //if (round == 10000) break;
            while(number)
            {
                if (digits[number % 10]==0) digits[number % 10]=1;
                number /= 10;
            }
            for (int j=0; j < 10; ++j) {
                if (digits[j]==0) break;
                if (j==9) finished = 1;
            }
        }
        outfile << "Case #" << i+1 << ": ";
        if (finished){
            outfile << round * orig_number << endl;
        }else{
            outfile << "INSOMNIA" << endl;
        }

    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
