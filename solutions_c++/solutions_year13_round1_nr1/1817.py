#include <iostream>
#include <fstream>
//#include <math>
#include<vector>

using namespace std;

unsigned int base[]={1,4,9,121,484};


int main(){
    ifstream fin;
    ofstream fout;
    //  fstream fi=("",in);
    fin.open("/Users/xianpan/Desktop/code/codejam13/A-small-attempt0-1.txt");
    fout.open("/Users/xianpan/Desktop/code/codejam13/A-small-attempt0-1res.txt");
    if(!fin.is_open())
        cout<<"in open error"<<endl;
    if(!fout.is_open())
        cout<<"out open error"<<endl;
    
    int cases=0;
    fin>>cases; cout<<cases<<endl;
    char ch;
    //    fin.get(ch);
    
    int cc=0; unsigned long long i=0; unsigned long long j=0;
    unsigned long long r=0; unsigned long long t=0; 
    unsigned long long total=0;
    for(cc=1; cc<=cases; cc++){
        fout<<"Case #"<<cc<<": ";
        
        fin>>r; cout<<r<<"  ";
        fin>>t; cout<<t<<endl;
        
        unsigned long long test= (r+1)*(r+1)-r*r;
        while(test<=t){
            total++;
            i++;
            j=2*i;
            long temp = r+j;
            test += (r+j+1)*(r+j+1)-temp*temp;
        }
        fout<<total<<endl;
        total = 0;
        i=0; j=0;
    }
    
    fin.close();
    fout.close();
}