#include <iostream>
#include <string>
#include <fstream>
using namespace std;
 string str[4];
bool check(int i,int j)
{
     if(str[i][j] != '.'){
                     if(j+1<4 && j+2<4 && j+3<4){
                     
                     if((str[i][j+1] == str[i][j]||str[i][j+1]=='T') && (str[i][j+2] == str[i][j]||str[i][j+2]=='T') && (str[i][j+3] == str[i][j]||str[i][j+3]=='T'))
                                                return true;
                                                }
                     if(j-1>=0 && j-2>=0 && j-3>=0){
                     
                              if((str[i][j-1] == str[i][j]||str[i][j-1]=='T') && (str[i][j-2] == str[i][j]||str[i][j-2]=='T') && (str[i][j-3] == str[i][j]||str[i][j-3]=='T'))
                                                return true;
                                                }    
                     if(i+1<4 && i+2<4 && i+3<4){
                     
                     if((str[i+1][j] == str[i][j]||str[i+1][j]=='T') && (str[i+2][j] == str[i][j]||str[i+2][j]=='T') && (str[i+3][j] == str[i][j]||str[i+3][j]=='T'))
                                                return true;
                                                }
                     if(i-1>=0 && i-2>=0 && i-3>=0){
                     
                              if((str[i-1][j] == str[i][j]||str[i-1][j]=='T') && (str[i-2][j] == str[i][j]||str[i-2][j]=='T') && (str[i-3][j] == str[i][j]||str[i-3][j]=='T'))
                                                return true;
                                                 
                                                }   
                     if(i+1<4 && i+2<4 &&i+3<4 && j+1<4 && j+2<4&& j+3<4){
                     
                              if((str[i+1][j+1] == str[i][j]||str[i+1][j+1]=='T') && (str[i+2][j+2] == str[i][j]||str[i+2][j+2]=='T') && (str[i+3][j+3] == str[i][j]||str[i+3][j+3]=='T'))
                                                return true;
                                                } 
                     if(i-1>=0 && i-2>=0 &&i-3>=0 && j+1<4 && j+2<4&& j+3<4){
                     
                              if((str[i-1][j+1] == str[i][j]||str[i-1][j+1]=='T') && (str[i-2][j+2] == str[i][j]||str[i-2][j+2]=='T') && (str[i-3][j+3] == str[i][j]||str[i-3][j+3]=='T'))
                                                return true;
                                                } 
                     if(i+1<4 && i+2<4 &&i+3<4 && j-1>=0 && j-2>=0&& j-3>=0){
                     
                              if((str[i+1][j-1] == str[i][j]||str[i+1][j-1]=='T') && (str[i+2][j-2] == str[i][j]||str[i+2][j-2]=='T') && (str[i+3][j-3] == str[i][j]||str[i+3][j-3]=='T'))
                                                return true;
                                                } 
                     if(i-1>=0 && i-2>=0 &&i-3>=0 && j-1>=0 && j-2>=0&& j-3>=0){
                     
                              if((str[i-1][j-1] == str[i][j]||str[i-1][j-1]=='T') && (str[i-2][j-2] == str[i][j]||str[i-2][j-2]=='T') && (str[i-3][j-3] == str[i][j]||str[i-3][j-3]=='T'))
                                                return true;
                                                }                                                                                                                                                                                                                                                   
                     }
                     
                     return false;
     }
int main()
{
   ofstream myfile;
  myfile.open ("output.txt");
 int n;
 bool nextt =false;
 bool dot =false;
 cin >> n;
 for(int k=0;k<n;k++)
 {
 nextt =false;
 dot =false;
 for(int i=0;i<4;i++) 
 {
 cin >> str[i];
 if(str[i]=="")
 i--;
}
myfile << "Case #"<<k+1<<": ";
 for(int i=0;i<4;i++)
 {
         for(int j=0;j<4;j++)
         {
                 if(!dot)
                 {
                    if(str[i][j]=='.')
                    dot=true;    
                        }
                 if(check(i,j))
                 {
                              myfile << str[i][j] << " " << "won" <<endl;
                              nextt=true;
                               
                         }
                 if(nextt)
                 break;
                 
                 }
                  if(nextt)
                 break;
         }  
         if(!nextt)
         {
                   if(dot)
                   myfile << "Game has not completed" << endl;
                   else
                   myfile << "Draw" << endl;
                   }
         }
           myfile.close();
}
