#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main()
{
    int x,y,z,s[100];
    int m,stand,output;
    output = stand = 0;
    int i;
   fstream in("A-small-attempt1.in");
ofstream out("outputfile.out");

in >> x; // x: testcases

for(i = 0; i< x; i++)
{
in >> y; // y: shy level (0 --> ..) 
char z[100]; 
in >> z;

stand += z[0] - 48; //initial value for standing people (with Si = 0) 

int j =1;
while (z[j] != '\0')
{
  
  m = stand - j;
  if(m>= 0) stand += z[j] - 48; 
  else 
  {
     output += j - stand;
     stand+= z[j] - 48 -m ;
  } 
j++; 
}
out << "Case #"<<i+1<<": "<<output<<endl;
stand = 0;
output = 0;   
}
 return 0;   
}
