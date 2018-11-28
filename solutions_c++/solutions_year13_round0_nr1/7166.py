#include <iostream>
#include <fstream>
#include<string.h>
using namespace std;

int main () {
  ifstream myfile;
  myfile.open ("A-large.in");
  ofstream fileout("fileout.txt");
  int n;
  int flag=0;
  char a[5][5];
  myfile>>n;
  //cout<<"valus of n"<<n<<"\n";
  for(int j=1;j<=n;j++)
  {
  
  for(int i=1;i<=4;i++){
  
  myfile>>a[i-1];
  //cout<<a[i-1]<<"\n";
  }
  for(int i=1;i<=4;i++)
  {
  //cout<<"check";
  if(strcmp(a[i-1],"TXXX")==0||strcmp(a[i-1],"XTXX")==0||strcmp(a[i-1],"XXTX")==0||strcmp(a[i-1],"XXXT")==0||strcmp(a[i-1],"XXXX")==0)
  {			
  fileout<<"Case #"<<j<<": X won\n";flag=1;
  break;
  }
  if(strcmp(a[i-1],"TOOO")==0||strcmp(a[i-1],"OTOO")==0||strcmp(a[i-1],"OOTO")==0||strcmp(a[i-1],"OOOT")==0||strcmp(a[i-1],"OOOO")==0)
  {
  fileout<<"Case #"<<j<<": O won\n";flag=1;
	break;
  }
  }
  if(flag==1){
  flag=0;
  continue;}
  for(int i=1;i<=4;i++)
  {
  //fileout<<"check";
  if((a[0][i-1]=='T'&&a[1][i-1]=='X'&&a[2][i-1]=='X'&&a[3][i-1]=='X')||(a[0][i-1]=='X'&&a[1][i-1]=='X'&&a[2][i-1]=='X'&&a[3][i-1]=='X')||(a[0][i-1]=='X'&&a[1][i-1]=='T'&&a[2][i-1]=='X'&&a[3][i-1]=='X')||(a[0][i-1]=='X'&&a[1][i-1]=='X'&&a[2][i-1]=='T'&&a[3][i-1]=='X')||(a[0][i-1]=='X'&&a[1][i-1]=='X'&&a[2][i-1]=='X'&&a[3][i-1]=='T'))
  {
  fileout<<"Case #"<<j<<": X won\n";flag=1;
  break;
  }
    if((a[0][i-1]=='T'&&a[1][i-1]=='O'&&a[2][i-1]=='O'&&a[3][i-1]=='O')||(a[0][i-1]=='O'&&a[1][i-1]=='O'&&a[2][i-1]=='O'&&a[3][i-1]=='O')||(a[0][i-1]=='O'&&a[1][i-1]=='T'&&a[2][i-1]=='O'&&a[3][i-1]=='O')||(a[0][i-1]=='O'&&a[1][i-1]=='O'&&a[2][i-1]=='T'&&a[3][i-1]=='O')||(a[0][i-1]=='O'&&a[1][i-1]=='O'&&a[2][i-1]=='O'&&a[3][i-1]=='T'))
  {
  fileout<<"Case #"<<j<<": O won\n";flag=1;
	break;
  }
  }
  if(flag==1){
  flag=0;
  continue;}
  if((a[0][0]=='T'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='X')||(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='X')||(a[0][0]=='X'&&a[1][1]=='T'&&a[2][2]=='X'&&a[3][3]=='X')||(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='T'&&a[3][3]=='X')||(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='T'))
  {
  fileout<<"Case #"<<j<<": X won\n";
	continue;
  }
  if((a[0][0]=='T'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='O')||(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='O')||(a[0][0]=='O'&&a[1][1]=='T'&&a[2][2]=='O'&&a[3][3]=='O')||(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='T'&&a[3][3]=='O')||(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='T'))
  {
  fileout<<"Case #"<<j<<": O won\n";
	continue;
  }
  if((a[0][3]=='T'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='O')||(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='O')||(a[0][3]=='O'&&a[1][2]=='T'&&a[2][1]=='O'&&a[3][0]=='O')||(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='T'&&a[3][0]=='O')||(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='T'))
  {
  fileout<<"Case #"<<j<<": O won\n";
	continue;
  }
   if((a[0][3]=='T'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='X')||(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='X')||(a[0][3]=='X'&&a[1][2]=='T'&&a[2][1]=='X'&&a[3][0]=='X')||(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='T'&&a[3][0]=='X')||(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='T'))
  {
  fileout<<"Case #"<<j<<": X won\n";
	continue;
  }
  for(int l=0;l<4;l++)
  for(int m=0;m<4;m++)
  if(a[l][m]=='.')
  {
  flag=1;
  break;}
  if(flag==1){
  	fileout<<"Case #"<<j<<": Game has not completed\n";
  flag=0;
  continue;}
  fileout<<"Case #"<<j<<": Draw\n";
 // myfile.seekg (1, myfile.cur);
  
  }
  
    
  myfile.close();
  fileout.close();
  return 0;

}
