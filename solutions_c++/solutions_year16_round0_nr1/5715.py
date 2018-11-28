#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool checkcount(int counted[]);
void resetarray(int counted[]);

int main(){
    
    const string insom = "INSOMNIA";
    
    ifstream infile;
    ofstream outfile;
    
    infile.open("A-large.in");
    outfile.open("output.txt");
    
    int counted[10] = {0};
    int t = 0;
    int n = 0;
    int mul;
    unsigned int num,answer = 0;
    int digit;
    bool check = false;
    
    infile >> t;
    
    for(int i = 0; i<t; i++){
        infile >> n;
        
        mul = 1;
        resetarray(counted);
        check = false;
        
        while(!check && n != 0){
            num = answer = n*mul;
            
            while(num>0){
                digit = num%10;
                num/=10;
                counted[digit] = 1;
                check = checkcount(counted);
            }
            mul++;
        }

        if(n!=0){
            outfile<< "CASE #" << i+1 << ": " << answer << endl;
        }
        else{
            outfile<< "CASE #" << i+1 << ": INSOMNIA" << endl;
        }
    }
    
    
}

bool checkcount(int counted[]){
    
    for(int i = 0; i<10; i++){
        if (counted[i] == 0){
            return false;
        }
    }
    
    return true;
}

void resetarray(int counted[]){
    for(int i = 0; i<10; i++){
        counted[i] = 0;
    }
}