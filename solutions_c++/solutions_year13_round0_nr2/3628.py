#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    
    
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int n;
    fin >> n;
    int sk;
    for(int i = 0; i < n; i++){
            //system("PAUSE");
            //return EXIT_SUCCESS;
            bool ats = true;        
            int x;
            int y;
            fin >> x >> y;
            cout << x << "     " << y << endl; 
            int veja[x][y];
            for(int xa = 0; xa < x; xa++){
                    for(int ya = 0; ya < y; ya++){
                            fin >> veja[xa][ya];
                            //sk++;
                            //cout << sk << endl;        
                    }
            }
            for(int a = 0; a < x; a++){
                    for(int b = 0; b < y; b++){
                            // tikrinam eilute;
                            bool eil = false;
                            for(int q = 0; q < x; q++){
                                    if(veja[q][b] > veja[a][b]){
                                                  eil = true;              
                                    }        
                            }
                            
                            //tikrinamas stulpelis
                            bool stul = false;                            
                            for(int q = 0; q < y; q++){
                                    if(veja[a][q] > veja[a][b]){
                                                  stul = true;              
                                    }        
                            }
                            if(stul && eil){
                                     ats = false;         
                            }
                                                       
                                    
                    }                                                
            }
            
            
            if(ats){
                    fout << "Case #" << i+1 << ": "<< "YES" << endl;        
            }else if(!ats){
                    fout << "Case #" << i+1 << ": "<< "NO" << endl;        
            }
    }    
}