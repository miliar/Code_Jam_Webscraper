#include <iostream>
#include <vector>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std;


int main()
{
    
READ("A-small-attempt4.in");
WRITE("A-small-attempt4.out"); 

 vector<vector<char> >v(4,vector<char>(4));
 vector<vector<char> >v2(4,vector<char>(4));
 int t; 
 cin>>t;
 for(int k = 0; k<t; k++)
 {
        
 bool isX = false, isY = false, Notcomp = false;
 int countX = 0,  countY = 0, count2X = 0, count2Y = 0;
 
  
  for(int i = 0; i<4; i++)
 {
   for(int j = 0; j<4; j++)
   {
      cin >> v[i][j];          
   }        
 }
 
 
  
  for(int i = 0; i<4; i++)
 {
   for(int j = 0; j<4; j++)
   {
      v2[j][i] = v[i][j];          
   }        
 }
 
  for(int i = 0; i<4; i++)
 {
          countX = 0, countY = 0, count2X = 0, count2Y = 0;
   for(int j = 0; j<4; j++)
   {
      if(v[i][j] == 'X' || v[i][j] == 'T')
      {
       countX++;
      }
      if(v[i][j] =='O' || v[i][j] == 'T')
      {
        countY++;     
      }
      
      if(v2[i][j] == 'X' || v2[i][j] == 'T')
      count2X++;
      if(v2[i][j]=='O'|| v2[i][j] == 'T')
      count2Y++;
        
   }    
   
   if(countX== 4 || count2X ==4)
   isX = true;
   else if(countY==4 || count2Y ==4)
   isY = true;
       
 }
 if(isX == false && isY == false)
 {
 if((v[0][0] =='O' ||v[0][0]=='T') && (v[1][1] =='O'||v[1][1]=='T') && (v[2][2] =='O'||v[2][2]=='T') && (v[3][3]=='O'||v[0][0]=='T'))
 isY = true;
 else if((v[0][3] =='O' ||v[0][3]=='T') && (v[1][2] =='O'||v[1][2]=='T') && (v[2][1] =='O'||v[2][1]=='T') && (v[3][0]=='O'||v[3][0]=='T'))
 isY = true;
 else if ((v[0][0] =='X' ||v[0][0]=='T') && (v[1][1] =='X'||v[1][1]=='T') && (v[2][2] =='X'||v[2][2]=='T') && (v[3][3]=='X'||v[0][0]=='T'))
 isX = true;
 else if((v[0][3] =='X' ||v[0][3]=='T') && (v[1][2] =='X'||v[1][2]=='T') && (v[2][1] =='X'||v[2][1]=='T') && (v[3][0]=='X'||v[3][0]=='T'))
 isX = true;
}
  cout<<"Case #"<<k+1<<": ";
 if(isX == true)
 cout<<"X won\n";
 else if(isY == true)
 cout<<"O won\n";
  else
 {
  for(int i = 0; i<4; i++)
 {
   for(int j = 0; j<4; j++)
   {
      if(v[i][j] == '.')
      Notcomp = true;         
   }        
 }
 if(Notcomp == true)
 cout<<"Game has not completed\n";
 else
 cout<<"Draw\n";
 }
 
 
} 
 

 
 
 return 0;   
}
