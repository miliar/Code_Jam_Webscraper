#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

unsigned short int cstr2usi(char temp[]){
    unsigned short int out;
    stringstream strStream;
    strStream << temp;
    strStream >> out;
    return out;
}

class Member{
    int ID;
    string Name;
};

int main(){

    char temp[101];
    ifstream inFile;
    unsigned short int *CaseResults;
    unsigned short int num_Cases;
    // <--->
    
    bool endFlips;
    char S[110];
    unsigned short int Slen, flipN;
    
    // <--->
    inFile.open("B-large.in.txt");

    inFile.getline(temp,100,'\n');
    num_Cases = cstr2usi(temp);

    cout<<"N Cases: "<<num_Cases<<endl;

    CaseResults = new unsigned short int[num_Cases];

    for(int i = 0; i < num_Cases; ++i){

        CaseResults[i] = 0;

        // Get S
        inFile.getline(S,110,'\n');
        Slen = strlen(S);
        
        cout<<"Size: "<<Slen<<"|"<<"S: "<< S <<endl;
        
        // <--->
        // Slen max flips
        for(int j=0; j <= Slen; ++j){
            
            endFlips = true;
            for(int k=0; k < Slen; ++k)
                if(S[k] == '-')
                    endFlips = false;
            
            if(endFlips == true){
                CaseResults[i] = j;
                break;
            }
            else{
                // Flip
                for(flipN=0; flipN < Slen-1; flipN++){
                    if(S[flipN] != S[flipN+1])
                        break;
                }
                
                for(int n=0; n <= flipN; ++n){
                    if(S[n] == '-')
                        S[n] = '+';
                    else
                        S[n] = '-';
                }
                cout<<flipN<<"->"<<S<<endl;
            }
        }
        
        // <--->

        cout<<"- - - - - - - - - - - - - - - - -"<<endl;
    }

    inFile.close();

    ofstream outFile;
    outFile.open("Large_Result.txt");
    for(int i = 0; i < num_Cases; ++i)
        outFile<<"Case #"<<i+1<<": "<< CaseResults[i] << endl;
    outFile.close();

    delete [] CaseResults;

    return 0;
}
