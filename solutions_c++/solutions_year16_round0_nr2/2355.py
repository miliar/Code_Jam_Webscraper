
#include <iostream>
#include <fstream>
#include <string>
#include <vector>   
using namespace std;
 
#define SIZE 10000
char line[SIZE];

string reverse(string cases, int idx){
    int i,j;
    for (i=0, j=idx; i<=j; i++, j--){
        char c = (cases[i]=='+')?'-':'+';
        cases[i] = (cases[j]=='+')?'-':'+';
        cases[j] = c;
    }
    return cases;
}
 
int main(int argc, char** argv){
    fstream fin;
    fin.open(argv[1]);
    fin.getline(line,sizeof(line),'\n');

    int casenum = atoi(line);
    ofstream fout (argv[2]);

    for(int i=1; i<= casenum; i++){
    	fin.getline(line,sizeof(line),'\n');
        string cases = line;

        int rounds = 0;
        int idx = cases.length()-1;

    	while (idx >= 0){
                while(cases[idx]=='+' && idx>=0) --idx;
                if (idx<0) break;

                if(cases[0] == '-')
                    cases = reverse(cases,idx);
                else {
                    int tmpidx = idx;
                    while(cases[tmpidx]=='-') tmpidx --;
                    cases = reverse(cases,tmpidx);
                }
                rounds++;  
        }

        fout<<"Case #"<<i<<": "<<rounds<<endl;
     }
     fout.close();
}
