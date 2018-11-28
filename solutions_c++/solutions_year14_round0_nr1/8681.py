#include <iostream>
#include <fstream>
using namespace std;




ifstream in("input.txt");
ofstream of("output.txt");


int main()
{
 int vett[5];int vett2[5];int matrice[6][6];
 int N;
 in>>N;
 int k;
 int row;
 for(int qwerty=0;qwerty<N;qwerty++)
 {int fine=0;
         
         
         
         
         
         
  in>>row;
  for(int y=0;y<4;y++)
      for(int x=0;x<4;x++)
          in >> matrice[x][y];
  
  
  for(int i=0;i<4;i++)
       vett[i]=matrice[i][row-1];          
  
  
  in>>row;
  for(int y=0;y<4;y++)
      for(int x=0;x<4;x++)
          in >> matrice[x][y];
  
  for(int i=0;i<4;i++)
       vett2[i]=matrice[i][row-1];
  
  for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
          if(vett[i]==vett2[j])
              {if(fine==0)
               {fine=vett[i]; 
                k=i;
               }
               else
               fine=101; 
          }                      
  
  if (fine==vett[k])
      of<<"Case #"<<qwerty+1<<": "<<vett[k]<<"\n";
 if(fine==101)
   of<<"Case #"<<qwerty+1<<": Bad magician!\n";

 if(fine==0)
    of<<"Case #"<<qwerty+1<<": "<<"Volunteer cheated!\n";
    


}

}  
                 
    
 
