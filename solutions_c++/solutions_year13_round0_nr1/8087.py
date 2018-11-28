#include <iostream>
#include <fstream>
#include <iomanip>
#include <locale>
#include <sstream>
#include <string.h>
using namespace std;

int main()
{
    fstream myfile;
  myfile.open ("A-small-attempt0.in");
  string line;
  if (myfile.is_open()) 
  {
                  
                            getline (myfile,line); // get number first
                   
  }
  char arr[4][4];
                 
int i,j,k,x,loop;
int cases = 0;

istringstream convert(line);

(convert >> loop) ;
     
for(x=0; x<loop; x++)
{
         int check = 0, ef=0;
         int flag = -1;
         while ( myfile.good() )
         {
               
               ++flag;
               
               getline (myfile,line);
               string a = line;
                       
               if(flag == 4 )
               {
                       flag = -1;
                       
                       int temp[7][4]={1};
                       for(i=0;i<7;i++)
                                       for(j=0;j<4;j++)
                                                       temp[i][j] = 1;

        for(i=0; i<4; i++){
         char cur = arr[0][i];
         for(j=i+1; j<4; j++){ // ->
                  char next = arr[0][j];
                  if(cur == next || next == 'T'){
                         temp[i][0]+=1; //display if 4;
                         
                         
                         if(temp[i][0] == 4 && cur != '.')
                         {
                                       cout<<"Case #"<<++cases<<": "<<cur<<" won"<<"\n";
                                       ef = 1;
                         }
                         
                         }
                         else
                             break;
                  
                  }
         
         
         for(j=1; j<4; j++) // down
         {
                  char next = arr[j][i];
                  if(cur == next || next =='T')
                  {
                         temp[i][1]+=1;//display if 4;
                         if(temp[i][1] == 4 && cur != '.')
                         {
                                       cout<<"Case #"<<++cases<<": "<<cur<<" won"<<"\n";
                                       ef = 1;
                         }
                         
                         }
                         else 
                              break;
                  }
                  
                  
         for(j=1,k=i+1; j<4,k<4; j++,k++)
         {
                          char next = arr[j][k];
                          if(cur == next || next =='T')
                          {
                                 temp[i][2]+=1;//display if 4;
                                 if(temp[i][2] == 4 && cur != '.')
                         {
                                       cout<<"Case #"<<++cases<<": "<<cur<<" won"<<"\n";
                                       ef = 1;
                         }
                                 
                                 }
                          else
                              break;
                                 
         }
         
         for(j=1,k=i-1; j<4,k>=0; j++,k--)
         {
                          char next = arr[j][k];
                          if(cur == next || next == 'T')
                          {
                                 temp[i][3]+=1;//display if 4;
                                 if(temp[i][3] == 4 && cur != '.')
                         {
                                       cout<<"Case #"<<++cases<<": "<<cur<<" won"<<"\n";
                                       ef = 1;
                         }
                                 
                                 }
                                 else
                                 break;
         }
}



int count=1;
for(i=1; i<4; i++)
{
         char cur = arr[i][0];
         
         for(j=1; j<4; j++)
         {
                  char next = arr[i][j];
                  if(cur == next || next == 'T')
                  {
                         count+= 1; //display if 4;
                         
                         if(count == 4 && cur != '.')
                         {
                                       cout<<"Case #"<<++cases<<": "<<cur<<" won"<<"\n";
                                       ef = 1;
                                       break;
                         }
                  }
                  else
                      break;
         }
         
         //cout<<"("<<i<<")-"<<count<<"\n";
         
         count = 1;
}
                       
                       // loop of while
                       
                       if(ef == 0)
                       {
                         if(check == 1)
                         {
                                  cout<<"Case #"<<++cases<<": Game has not completed"<<"\n";
                                  
                                  ef = 0;
                                  check = 0;
                                  continue;
                                  
                         }
                         cout<<"Case #"<<++cases<<": Draw"<<"\n";
                         
                         
                       }
                       ef = 0;
                       check = 0;
                       
                       
                       continue;
                       
                       
               }
               
               
               int p,q;
               
               for(p=flag; p<4; p++)
               {
                           for(q=0; q<4; q++)
                           {
                                    arr[p][q] = a[q];
                                    
                                    if(a[q] == '.')
                                      check = 1;
                                    
                           }
               }
             
         }
}



system("pause"); 
return 0;    
}
