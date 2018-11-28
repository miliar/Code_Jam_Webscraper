#include <fstream>
#include <cstring>
#include <cstdlib>
#include <math.h>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    int amount;
    fin>>amount;

    unsigned long long r,t,b,e,j,c;
    ofstream fout("A-small-attempt0.out");
    
    for(int i=0;i<amount;i++){
            fout<<"Case #"<<i+1<<": ";
            fin>>r>>t;
            
            b=1;
            e=(unsigned long long)((sqrt(8*t+1)-1)/4+1);
            j=b+e/2;
            
            while(b<e-1){
                        c=2*j*j+(2*r-1)*j;
                        
                        if(c==t) {
                                b=j;
                                e=j; 
                                break;
                        }
                        
                        if(c<t){
                             b=j;
                        }
                        else{
                             e=j;
                        }
                        j=(b+e)/2;
            }
            
            c=2*b*b+(2*r-1)*b;
            if(c==t){
                     fout<<b<<endl;
            }
            else if(c>t){
                 fout<<b-1<<endl;
            }
            else{
                 c=2*e*e+(2*r-1)*e;
                 if(c==t){
                          fout<<e<<endl;
                 }
                 else{
                      fout<<b<<endl;
                 }
            }
            
    }
    
    
    
    fout.close();
    
    return 0;
}
