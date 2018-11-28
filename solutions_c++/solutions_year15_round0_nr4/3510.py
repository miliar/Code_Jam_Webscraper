#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream inFile;
    ofstream outFile;
    inFile.open("Small.txt");
    outFile.open("SmallAnswer.txt");
    //Check for error
    if(inFile.fail())
    {
        cerr << "File not found" << endl;
        exit(1);
    }
    string item;
    int T = 0;
    
    inFile >> T;
    
    for(int i=0;i<T;i++)
    {
        string result;
        int X,R,C;
        inFile >> X>> R>>C;
        //cout<< X<< " " <<R << " " <<C<<endl;
        int greater,smaller;
        if(R>C)
        {
            greater = R; smaller = C;
        }
        else
        {
            greater = C; smaller = R;
        }
        if( ((R*C)%X != 0) || ((R==1 || C==1 || ((R*C)/X ==1)) && X>2))
        {
            result = "RICHARD";
        }
        else if(R!=C && greater/2<=smaller && greater%smaller == 0 && X>2)
        //else if((X-1) < ((R*C)/X))
        {
            result = "RICHARD";
        }
        else
        {
            result = "GABRIEL";
        }
        outFile<<"Case #"<<i+1<<": "<<result<<endl;
        
    }
    
    inFile.close();
    outFile.close();
    
}
