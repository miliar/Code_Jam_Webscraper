#include <iostream>
#include <fstream>
//#include <math>
#include<vector>

using namespace std;

unsigned int base[]={1,4,9,121,484};


bool wingame(unsigned int z){//cout<<z<<endl;
    if(z==15 || z==240 || z==3840 || z==61440) return true;
    if(z==4369 || z==8738 || z==17476 || z==34952) return true;
    if(z==33825 || z==4680) return true;
    return false;
}

int main(){
    ifstream fin;
    ofstream fout;
    //  fstream fi=("",in);
    fin.open("/Users/xianpan/Desktop/code/codejam13/C-small-attempt0.txt");
    fout.open("/Users/xianpan/Desktop/code/codejam13/C-small-attempt0res.txt");
    if(!fin.is_open())
        cout<<"in open error"<<endl;
    if(!fout.is_open())
        cout<<"out open error"<<endl;
    
    int cases=0;
    fin>>cases; cout<<cases<<endl;
    char ch;
    //    fin.get(ch);
    
    int cc=0; int i=0;
    unsigned int a=0; unsigned int b=0; int count=0;
    for(cc=1; cc<=cases; cc++){
        fout<<"Case #"<<cc<<": ";
        
        fin>>a; cout<<a<<"  ";
        fin>>b; cout<<b<<endl;
        
        for(i=0;i<6;i++){
            if(base[i]>b) break;
            if(base[i]>=a && base[i]<=b) count++;
        }
        fout<<count<<endl;
        count = 0;
    }
    
    fin.close();
    fout.close();
}