#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fin("magictrick.in");
    ofstream fout("magictrick.out");
    int t=0, a1, a2, m1[5][5], m2[5][5], count=0, temp;
    fin>>t;
    for(int i=1; i <= t; i ++){
            count=0;
            fin>>a1;
            for(int j=1;j<5;j++){
                    for(int x=1;x<5;x++){
                            fin>>m1[j][x];
                            }
                    }
            fin>>a2;
             for(int j=1;j<5;j++){
                     for(int x=1;x<5;x++){
                            fin>>m2[j][x];
                            }
                    }
             for(int y=1;y<5;y++){
                     for(int z=1;z<5;z++){
                             if(m1[a1][y] == m2[a2][z]){
                                          count++;
                                          temp = m1[a1][y];
                                          }
                             }
                     }
             if(count == 1){
                      fout<<"Case #"<<i<<": "<<temp<<endl;
                      }
             else if(count == 0){
                  fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
                  }
             else{
                  fout<<"Case #"<<i<<": "<<"Bad magician! "<<endl;
                  }
            }
    system("PAUSE");
    return EXIT_SUCCESS;
}
