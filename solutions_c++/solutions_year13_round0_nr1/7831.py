#include<iostream>
#include<stdio.h>
#include<fstream>
#include<algorithm>
using namespace std;

int n,i,j;
string s,arr[4];
//ifstream fh("Aexample.txt");
//ofstream fho("Aexampleoutput.txt");
ifstream fh("A-small-attempt0.in");
ofstream fho("A-small-output.in");

int main(){
  fh>>n;
  i=0;
  j=1;
  while(fh >> s){
    arr[i]=s;
    ++i;
    if(i==4){
      int flag=0;
      string barr[4]={arr[0],arr[1],arr[2],arr[3]};

      string X = "XXXX";
      replace(arr[0].begin(),arr[0].end(),'T','X');
      replace(arr[1].begin(),arr[1].end(),'T','X');
      replace(arr[2].begin(),arr[2].end(),'T','X');
      replace(arr[3].begin(),arr[3].end(),'T','X');
      string c1 = "";c1+=arr[0][0];c1+=arr[1][0];c1+=arr[2][0];c1+=arr[3][0];
      string c2 = "";c2+=arr[0][1];c2+=arr[1][1];c2+=arr[2][1];c2+=arr[3][1];
      string c3 = "";c3+=arr[0][2];c3+=arr[1][2];c3+=arr[2][2];c3+=arr[3][2];
      string c4 = "";c4+=arr[0][3];c4+=arr[1][3];c4+=arr[2][3];c4+=arr[3][3];
      string d1 = "";d1+=arr[0][0];d1+=arr[1][1];d1+=arr[2][2];d1+=arr[3][3];
      string d2 = "";d2+=arr[0][3];d2+=arr[1][2];d2+=arr[2][1];d2+=arr[3][0];
      if(arr[0]==X || arr[1]==X || arr[2]==X || arr[3]==X || d1==X || d2==X  || c1==X || c2==X || c3==X || c4==X)
      {
          fho<<"Case #"<<j<<": X won"<<endl;
        flag=1;
      }
      if(flag==0)
      {
        string O = "OOOO";
        replace(barr[0].begin(),barr[0].end(),'T','O');
        replace(barr[1].begin(),barr[1].end(),'T','O');
        replace(barr[2].begin(),barr[2].end(),'T','O');
        replace(barr[3].begin(),barr[3].end(),'T','O');
        string c1 = "";c1+=arr[0][0];c1+=arr[1][0];c1+=arr[2][0];c1+=arr[3][0];
        string c2 = "";c2+=arr[0][1];c2+=arr[1][1];c2+=arr[2][1];c2+=arr[3][1];
        string c3 = "";c3+=arr[0][2];c3+=arr[1][2];c3+=arr[2][2];c3+=arr[3][2];
        string c4 = "";c4+=arr[0][3];c4+=arr[1][3];c4+=arr[2][3];c4+=arr[3][3];
        string d1 = "";d1+=barr[0][0];d1+=barr[1][1];d1+=barr[2][2];d1+=barr[3][3];
        string d2 = "";d2+=barr[0][3];d2+=barr[1][2];d2+=barr[2][1];d2+=barr[3][0];      
        if(barr[0]==O || barr[1]==O || barr[2]==O || barr[3]==O || d1==O || d2==O || c1==O || c2==O || c3==O || c4==O)
        {
          fho<<"Case #"<<j<<": O won"<<endl;
          flag=1;
        }
      }
      if(flag==0)
      {
        if(arr[0].find(".") == string::npos && arr[1].find(".") == string::npos && arr[2].find(".") == string::npos && arr[3].find(".") == string::npos)
        {
          fho<<"Case #"<<j<<": Draw"<<endl;        
        }
        else{
          fho<<"Case #"<<j<<": Game has not completed"<<endl;
        }
      }
      
      i=0;
      ++j;
    }
  }
  fho<<endl;
  
  return 0;
}
