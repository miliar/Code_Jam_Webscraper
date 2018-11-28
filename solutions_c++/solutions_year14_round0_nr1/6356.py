#include <fstream>
#include <cstdlib>
#include <iostream>
using namespace std;
int main() {
int x;
  ifstream myReadFile;
    myReadFile.open("file.text");
  ofstream out;
    out.open("sluo.text");
    myReadFile >> x;
cout<<x;
int ch1;
int ch2;
int test1[4][4];
int test2[4][4];
int nooft=1; 
for(int i=0;i<x;i++)
{
   myReadFile >> ch1;
 
   for(int j=0;j<4;j++)
       { for(int y=0;y<4;y++)
           { myReadFile >> test1[j][y];
                
             }
            }

        
   myReadFile >> ch2;
  
   for(int j=0;j<4;j++)
       {for(int y=0;y<4;y++)
          { myReadFile >> test2[j][y];
          
         }
       }
   
int sl;
int no=0;
for(int i=0;i<4;i++)
   {for(int j=0;j<4;j++)
        {
        if(test1[ch1-1][i]==test2[ch2-1][j])
          {sl=test1[ch1-1][i];
             no++;
             }}}

if(no>1)
{out<<"Case #"<<nooft;
out<<": Bad magician!\n";
nooft++;}
if(no==0)
{out<<"Case #"<<nooft;
out<<": Volunteer cheated!\n";
nooft++;}
if(no==1)
{out<<"Case #"<<nooft<<": ";
out<<sl;
out<<endl;
nooft++;}






} 
}
