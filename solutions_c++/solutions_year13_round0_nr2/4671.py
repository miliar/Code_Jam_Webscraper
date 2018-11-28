#include<iostream>
#include<fstream>
#include<conio.h>
#include<string.h>
#include<iomanip>
using namespace std;

int main()
{
    int T[100][100];
    int n,i,N,M,p,q,X;
   
    
    ifstream fin;
    ofstream fout,fout2;
    fin.open("As.in",ios::in);
    fout.open("Aso.out",ios::out);
    fout2.open("Aso2.out",ios::out);
    fin>>n;
    for(i = 0; i<n ; i++)
    {
         fout2<<endl<<i+1<<"#\n"; 
        fin>>M; fin>>N;
        for(q =0;q<M;q++)
       { for(p =0;p<N;p++)
        { fin>>T[q][p];
         fout2<<T[q][p]<<" ";}
         fout2<<endl;
         }
               
   X=0;
        for(p= 0;p<M*N;p++)
        {
        
       int  min = 101;
      
       int minx=0,miny=0,j,k,flagr=0,flagc=0;
                //find min
                
                for(j = 0;j<M;j++)
                for( k =0 ; k<N;k++)
                { if(T[j][k]<min&&T[j][k]!=-1)
                {
                    min = T[j][k];  
                    minx = j; miny=k;
                                  
                        }
                        }
                        
                for(j=0;j<N;j++)
                {if(T[minx][j]!=min&&T[minx][j]!=-1)
                {flagr=1;}
                }   
                for(j=0;j<M;j++)
                {if(T[j][miny]!=min&&T[j][miny]!=-1)
                {flagc=1;}
                                }                  
                if(flagc==1&&flagr==1)
               {
                fout<<"Case #"<<i+1<<": NO"<<endl;
               X= -1; break;
                                      }
                                      
                else if(flagc==0)
                {
                     for(j = 0; j<M;j++)
                     {T[j][miny] = -1;
                     
                           }
                     
                     }      
                 else if(flagr==0)
                 { for(j = 0; j<N;j++)
                     {T[minx][j] = -1;
                     
                           }
                     
                  }  
                  //transformed 2
        for(j =0;j<M;j++)
       { for(k =0;k<N;k++)
        { 
         fout2<<T[j][k]<<" ";}
         fout2<<endl;
         }                                    
                }
          if(X!=-1)
             fout<<"Case #"<<i+1<<": YES"<<endl;
            
            }

    fin.close();
    fout.close();
    }
