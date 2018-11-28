
#include <iostream>
#include <fstream>
#include <string>
#include <vector>   
using namespace std;
 
#define SIZE 10000000000
char line[SIZE];
 
int main(int argc, char** argv){
    fstream fin;
    fin.open(argv[1]);
    fin.getline(line,sizeof(line),'\n');

    int casenum = atoi(line);
    long double* cases =  new long double[casenum];

    ofstream fout (argv[2]);

    for(int i=1; i<= casenum; i++){
    	fin.getline(line,sizeof(line),'\n');
    	cases[i] = atoi(line);
    	bool test[10];
    	bool complete = false;

    	for(int ii=0; ii<10; ii++) test[ii] = false;

        if(cases[i] == 0) 
        	fout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else{
    	    int rounds = 1; 
    		while (complete == false){
    			int  tmp = cases[i]*rounds;
                int dignum =1;
                for(; tmp/10 > 0; dignum++) tmp/=10;                	
                tmp = cases[i]*rounds;

    			for(int j=0; j< dignum;j++){
    				int k = tmp%10;
    				if(!test[k]) test[k] = true;
    				tmp = tmp/10;
    			}
                
    			complete = true;
    			for(int ii=0; ii<10; ii++) 
    				if(!test[ii]) complete = false;
        	    rounds ++;
        	}
        	int kk = cases[i]*(rounds-1);
        	cout<<"l = "<<kk <<endl;
           fout<<"Case #"<<i<<": "<<kk<<endl;
        }

    }
     fout.close();
}