#include <fstream>
#include <iostream>

#define INPUT_FILE "A.in"
#define OUTPUT_FILE "A.out"

using namespace std;


unsigned long long solve(unsigned long N)
{
    unsigned long long res = N ,tmp=N;
    
    int marks[] ={0,0,0,0,0,0,0,0,0,0};
    
    while(N)
    {
        marks[N%10] =1;
        N=N/10;
    }
    while (!(marks[0] & marks[1] & marks[2] & marks[3] & marks[4] & marks[5] & marks[6] & marks[7] & marks[8] & marks[9] ))
    {
        res+=tmp;
        N = res;
        while(N)
        {
            marks[N%10] =1;
            N=N/10;
        }
    }
    
    return res;
}


int main()
{
    //input file 
    ifstream fin;
    //output file
    ofstream fout;
    
    fin.open(INPUT_FILE);
    fout.open(OUTPUT_FILE);
    
    int T,i=1;
    unsigned long N;
    unsigned long long result;
    
    fin >> T;
    cout << T;
    while(i<=T)
    {
        fin >> N ;
        fout << "Case #" << i << ": ";
        if(N==0)
        {
            fout << "INSOMNIA" << endl;
        }
        else
        {
            fout << solve(N) << endl;
        }
        
        i++;
    }
    
    return 0;
}