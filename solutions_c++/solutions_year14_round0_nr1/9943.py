#include<iostream>
#include<algorithm>
#include<functional>
#include<cmath>
#include<math.h>
#include<string.h>
#include<string>
# include<fstream>
#include<map>
using namespace std;
int main ()
{     int i,j,k,p,q,n;
       ifstream fin;
       ofstream fout;
       fin.open("Input.txt");
       fout.open("Output.txt");
       fin>>n;
     //  cout<<n;
     map<int ,int>mapp;
       q=1;
       while(q<=n)
       {                fin>>p;
                        for(i=0; i<4; i++)
                           for(j=0; j<4; j++)
                           { fin>>k;
                            if(i+1==p)
                            mapp[k]=1;
                            }
                          fin>>p;  
                          int count=0,answer=0;
                          for(i=0; i<4; i++)
                           for(j=0; j<4; j++)
                           { fin>>k;
                             if(i+1==p&&mapp[k]==1)
                             {
                             answer=k;
                             count++;
                             }
                           }
                           if(count==1)
                           fout<<"Case #"<<q<<": "<<answer<<"\n"; 
                           if(count>1)
                           fout<<"Case #"<<q<<": Bad magician!\n";
                           if(count==0)
                           fout<<"Case #"<<q<<": Volunteer cheated!\n";   
                          q++;
                          mapp.clear();
         }  
       fin.close();
       fout.close();                     
                           
                           
//system("pause");
}
