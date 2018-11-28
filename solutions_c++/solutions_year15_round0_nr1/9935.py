/*
ID: vizay.08
PROG: standing ovation
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string.h>


using namespace std;
int main(){
    ifstream ifile("sample.in");
    ofstream ofile("sample.out");
    
    int T,KMAX,TCOUNT,NCOUNT,x,y,diff;
    string kstring;
    
    ifile>>T;
    for(int i = 1;i<=T;i++){
            TCOUNT = 0;
            NCOUNT = 0;
            ifile>>KMAX>>kstring;
           
            x=0;
            y=1;
            TCOUNT = kstring[0]-'0';
             while(y <= KMAX && x!= KMAX){
                     if(kstring[x]-'0' == 0){
                                       while(kstring[y]-'0' == 0){
                                                            y++;
                                       }
                                       x = y-1;                  
                                                            
                     }       
                     diff = 0;                     
                     if(y>TCOUNT){
                                  
                                  diff = y-TCOUNT;
                                  
                                  }
                                  
                     TCOUNT += diff + (kstring[y]-'0');
                     NCOUNT +=  diff;
                     
                     

                     x++;
                     y++;
                     
             }
             

             ofile<<"Case #"<<i<<": "<<NCOUNT<<endl;
             
    }
    
    
    ifile.close();
    ofile.close();

    return 0;
}
