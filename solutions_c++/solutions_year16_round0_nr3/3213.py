#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <bitset>

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
    int N;
    int J;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    for (int i=0; i<cases; ++i) {
        outfile << "Case #" << i+1 << ": " << endl;
        int finished = 0;
        // read from file
        infile >> N;
        infile >> J;
        cout<<N<<" "<<J<<endl;
        string test_number;
        
        int long te = 1000000010110001;
        int te3 = 7;
        cout<< te%te3<< endl;
        int count = 0;
        //Generate All Permutations
        for(int z=0;z<pow(2,N);z++){
            test_number = std::bitset<32>(z).to_string();
            test_number=test_number.substr(32-N);
            //cout << test_number << endl;
            //Test if jamcoin
            if (test_number[0]=='1' && test_number[N-1]=='1') {
                //Gets Divisor
                int divisors[10]={};
                long int base = 0;
                int prime = 0;
                int rp = 0;
                //cout <<"TN: " <<test_number<< endl;
                for (int k=2; k<=10; ++k){
                    base = stol(test_number,nullptr,k);
                    cout <<"BASE: " <<base << endl;
                    int max = sqrt(base)+1;
                    for (int j = 2; j <= max; ++j){
                        if (base % j == 0){
                            cout <<"k:"<< k << endl;
                            cout << j << endl;
                            divisors[k]=j;
                            //cout << k << " " << j <<endl;
                            if (k==10) rp=1;
                            break;
                        }
                        if (j==max && divisors[k] == 0) prime = 1;
                    }
                    cout << k<< endl;
                    if (prime) break;
                }
                if (!prime && rp){
                    outfile << test_number << " ";
                    for (int q = 2; q<=10; ++q) {
                        if (q<10)outfile << divisors[q] << " ";
                        else outfile << divisors[q];
                    }
                    outfile << endl;
                    count++;
                }
            }
            if (count == J) break;
        }
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
