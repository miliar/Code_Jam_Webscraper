#include<iostream>
#include<fstream>
using namespace std;

int main() {

    ifstream infile("temp.txt");
    
    
    int num;
    infile>>num;
    
    for(int i=0; i<num; i++)
    {
        int smax;
        infile>>smax;
        
        int count=0;
        for(int j=0; j<=smax; j++)
        {
            char ppl;
            infile>>ppl;
            
            if(ppl == '0')
                count++;
        }
        
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    

    return 0;
}