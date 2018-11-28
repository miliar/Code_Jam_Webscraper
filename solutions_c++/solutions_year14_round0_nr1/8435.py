#include <fstream>
#include <iostream>

#include <set>

using namespace std; 

#define forn(i,n) for (int i =0;i<n;i++)

int main(int argc, char **argv){

    ifstream in ("entrada.in");
    ofstream out ("salida_magica.out");
    
    int t;
    
    in>>t;
    
    forn(casen,t){
        int a,b;
        in>>a;
        int c;
        set <int> s1;
        
        forn(i, 4){
            forn(j,4){
                in>>c;
                if (i == a-1){
                    s1.insert(c);
                }   
            }
        }
        
        in>>b;
        
        int found = 0;
        int who;
        
        forn(i, 4){
            forn(j,4){
                in>>c;

                if (i == b-1){              
                    if (s1.count(c)){
                        found++;
                        who =  c;
                    }
                }    
            }
        }
        

        cout<<found<<" "<<who<<endl;
        
        if (found > 0){
            if (found >1) {
                out<<"Case #"<<casen+1<<": "<<"Bad magician!\n";
            }
            else {
                out<<"Case #"<<casen+1<<": "<<who<<"\n";
    
            }
        }
        else {
            out<<"Case #"<<casen+1<<": "<<"Volunteer cheated!\n";
        }
        
    }
}
