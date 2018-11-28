/*
ID: kelovef2
LANG: C++
*/

#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    int amount;
    fin>>amount;
    
    int tmp;
    int lawn[100][100];
    bool possible[100][100];
    bool exist[100];
    bool fine=true;
    
    int n,m;
    ofstream fout("B-large.out");
    
    for(int i=0;i<100;i++)
            exist[i]=false;
    
    for(int i=0;i<amount;i++){
            
            fout<<"Case #"<<i+1<<":";
            fine=true;
            fin>>n>>m;
            
            for(int j=0;j<n;j++){
                    for(int k=0;k<m;k++){
                            fin>>tmp;
                            lawn[j][k]=tmp-1;
                            possible[j][k]=false;
                            exist[tmp-1]=true;
                    }
            }
            
            for(int x=0;x<100;x++){
                    if(exist[x]){
                                 exist[x]=false;
                                 if(fine){
                                          for(int y=0;y<n;y++){
                                                  if(!fine) break;
                                                  for(int z=0;z<m;z++){
                                                          if(!fine) break;
                                                          if(lawn[y][z]==x && !possible[y][z]){
                                                                           for(int chk=0; chk<m; chk++){
                                                                                   if(lawn[y][chk]!=x && !possible[y][chk]){
                                                                                                      fine=false;
                                                                                                      break;
                                                                                   }
                                                                                   
                                                                           }
                                                                           if(fine){
                                                                                    for(int chk=0;chk<m;chk++){
                                                                                            possible[y][chk]=true;
                                                                                    }
                                                                                    
                                                                           }
                                                                           else{
                                                                                    fine=true;
                                                                                     for(int chk=0;chk<n;chk++){
                                                                                            if(lawn[chk][z]!=x && !possible[chk][z]){
                                                                                                      fine=false;
                                                                                                      break;
                                                                                            } 
                                                                                     }
                                                                                     if(fine){
                                                                                              for(int chk=0;chk<n;chk++){
                                                                                                      possible[chk][z]=true;
                                                                                              }
                                                                                     }
                                                                           }
                                                          }
                                                  }
                                          }
                                 }
                    }
            }
            
            if(fine) fout<<" YES"<<endl;
            else fout<<" NO"<<endl;    
    }
    
    
    
    fout.close();
    
    return 0;
}
