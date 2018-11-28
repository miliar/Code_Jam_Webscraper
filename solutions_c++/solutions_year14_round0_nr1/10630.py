#include <iostream>
#include<fstream>
#include<sstream>
#include<string>
using namespace std;
void search(int s1,int s2,int a[4][4],int b[4][4],int ca);
int main()
{
 ifstream in ("input.txt");
 int t,s1,s2,m,j,y;
 int a[4][4];
 int b[4][4];
 in>>t;// the number of Tests
 for(int i=0;i<t;i++)
 {
   in>>s1;//the first answer
   for(m=0;m<16;m++)
    {
    for(j=0;j<4;j++) 
    for(y=0;y<4;y++)
    in>>a[j][y];
        
    } 
    in>>s2;//the second answer
     for(m=0;m<16;m++)
    {
    for(j=0;j<4;j++) 
    for(y=0;y<4;y++)
    in>>b[j][y];
        
    } 
    
   search( s1, s2, a, b,i+1)  ;
     
     
 }
 
 

        
        
  
    
 return 0;
 }
 
 void search(int s1,int s2,int a[4][4],int b[4][4],int ca)
 {
     
  int c=0;
  int n[4];
  int m[4];
  int j,v,i;
  for( i=0;i<4;i++)
  {
   n[i]=a[s1][i] ;
   m[i]=b[s2][i];
      
      
  }
  for(i=0;i<4;i++)
  for(j=0;j<4;j++)
  if(n[i]==m[j])
  {
   c++;
   v=i;// the index of the element
      
  }
  if(c>1)
  out<<"case #"<<ca<<": "<<"Bad magician!"<<endl;
  else if(c==0)
  out<<"case #"<<ca<<": "<<"Volunteer cheated!"<<endl;
  else
 out<<"case #"<<ca<<": "<<n[v]<<endl;
  
     
     
     
 }
 

 
 
 



