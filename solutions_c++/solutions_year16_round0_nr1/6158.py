#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

long long int cstr2usi(char temp[]){
    long long int out;
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
    unsigned long long int *CaseResults;
    unsigned long long int num_Cases;
    // <--->
    
    bool Sleep;
    unsigned short int Check[10];
    for(int i=0; i<10;++i)
        Check[i]=0;
    unsigned long long int N, Tmp, Tmp2, Tmp3;

    // <--->
    inFile.open("A-large.in.txt");

    inFile.getline(temp,100,'\n');
    num_Cases = cstr2usi(temp);

    cout<<"N Cases: "<<num_Cases<<endl;

    CaseResults = new unsigned long long int[num_Cases];
    Tmp3 = N;
    for(int i = 0; i < num_Cases; ++i){

        CaseResults[i] = 0;
        for(int i=0; i<10;++i)
            Check[i]=0;
        
        // Get N
        inFile.getline(temp,100,'\n');
        N = cstr2usi(temp);
        Tmp3 = N;
        //cout<<"N: "<< N <<endl;
        
        // <--->
        for(int j=0; j < 1000000; ++j){
            Tmp = N;
            //cout<<Tmp<<"->";
            while( Tmp > 0){
                Tmp2 = Tmp%10;
                Check[Tmp2] = 1;
                Tmp=Tmp/10;
                //cout<<Tmp2<<"-";
            }
            
            Sleep = true;
            for(int k=0; k<10; ++k)
                if(Check[k]==0)
                    Sleep = false;
            if (Sleep == true)
                break;
            
            N = N+Tmp3;
        }
        
        for(int j=0; j<10; ++j){
            if(Check[j]==0)
                CaseResults[i] = -1;
            else
                CaseResults[i] = N;
        }
        
        // <--->
        //cout<<"Case #"<<i<<": "<<CaseResults[i]<<endl;
        //cout<<"- - - - - - - - - - - - - - - - -"<<endl;
    }

    inFile.close();

    ofstream outFile;
    outFile.open("Small_Result.txt");
    for(int i = 0; i < num_Cases; ++i){
        if(CaseResults[i] == -1)
            outFile<<"Case #"<<i+1<<": "<< "INSOMNIA" << endl;
        else
            outFile<<"Case #"<<i+1<<": "<< CaseResults[i] << endl;
    
    }
    outFile.close();

    delete [] CaseResults;

    return 0;
}
