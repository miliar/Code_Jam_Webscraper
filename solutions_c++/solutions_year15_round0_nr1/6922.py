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

int main(){
    
    unsigned short int *CaseResults;
    
    unsigned short int num_TestCases;
    unsigned short int num_MaxShyness;
    unsigned short int num_Cases;
    
    int tot;
    
    stringstream strStream;
    
    unsigned short int *Shyness;
    
    char temp[101];
    
    ifstream inFile;
    inFile.open("A-large.in.txt");
    
    inFile.getline(temp,100,'\n');
    num_Cases = cstr2usi(temp);
    
    cout<<"N Cases: "<<num_Cases<<endl;
    
    CaseResults = new unsigned short int[num_Cases];
    
    
    for(int i = 0; i < num_Cases; ++i){
        
        CaseResults[i] = 0;
        tot = 0;
        
        // Get MaxShyness
        inFile.getline(temp,10,' ');
        num_MaxShyness = cstr2usi(temp);
        
        cout<<"MaxShyness: "<<num_MaxShyness<<endl;
        
        // Allocate memory for Shyness (numbers MaxShyness+1)
        Shyness = new unsigned short int[num_MaxShyness+1];
        
        // Read Shyness Data
        inFile.getline(temp,1005,'\n');
        for(int j = 0; j < num_MaxShyness+1; ++j)
            Shyness[j]=(int)temp[j]-48;
        
        //DataOutput
        cout<<"     : "<<temp<<endl;
        
        // -----------------------------------------
        
        
        for(int j = 0; j < num_MaxShyness+1 ; ++j){
            if(j == 0)
                tot = Shyness[j];
            else{
                if(tot < j && Shyness[j] != 0){
                    CaseResults[i] = CaseResults[i] + j - tot;
                    tot = j + Shyness[j];
                }
                else if( tot >= j){
                    tot = tot + Shyness[j];
                }
            }
        }
        
        // -----------------------------------------
        
        // Delete Allocated memory
        delete [] Shyness;
        
        cout<<"- - - - - - - - - - - - - - - - -"<<endl;
    }
    
    inFile.close();
    
    ofstream outFile;
    outFile.open("Small_Result.txt");
    for(int i = 0; i < num_Cases; ++i)
        outFile<<"Case #"<<i+1<<": "<< CaseResults[i] << endl;
    outFile.close();
    
    delete [] CaseResults;
    
    return 0;
}