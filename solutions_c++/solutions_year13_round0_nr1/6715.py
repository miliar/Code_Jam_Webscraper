#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long sh, sv, m, i, k, t, isdraw, xwon, owon;
    char c;
    int xx[4][4];
    int oo[4][4];
    fstream infile("A-large.in");
    ofstream outfile("A-large.out");
    infile >> t;
    for (m=1; m<=t; ++m){
      isdraw=1;
      xwon=0;
      owon=0;  
      for(i=0; i<4; ++i) 
      {
          infile.get(c);
      for(k=0; k<4; ++k)
        {
          infile.get(c);
          cout <<c<<"-";
          // .=0 O=1 X=1
          if (c=='X'){xx[i][k]=1;oo[i][k]=0;}
          if (c=='O'){xx[i][k]=0;oo[i][k]=1;}
          if (c=='T'){xx[i][k]=1;oo[i][k]=1;}
          if (c=='.'){xx[i][k]=0;oo[i][k]=0;isdraw=0;}
          cout << xx[i][k]<<","<<oo[i][k]<<" ";
        }
        cout << endl;
  //      infile.get(c);
      }
      for(i=0; i<4; ++i) 
      {
               sh=0; sv=0;
      for(k=0; k<4; ++k)
        {
           sh+=xx[i][k];
           sv+=xx[k][i];
        }
        if (sh==4) xwon=1;
        if (sv==4) xwon=1;
        if ((xx[0][0]+xx[1][1]+xx[2][2]+xx[3][3])==4)xwon=1;
        if ((xx[0][3]+xx[1][2]+xx[2][1]+xx[3][0])==4)xwon=1;
      }
      
      for(i=0; i<4; ++i) 
      {
               sh=0; sv=0;
      for(k=0; k<4; ++k)
        {
           sh+=oo[i][k];
           sv+=oo[k][i];
        }
        if (sh==4) owon=1;
        if (sv==4) owon=1;
        if ((oo[0][0]+oo[1][1]+oo[2][2]+oo[3][3])==4)owon=1;
        if ((oo[0][3]+oo[1][2]+oo[2][1]+oo[3][0])==4)owon=1;
      }
      if (xwon) {
      outfile << "Case #"<<m<<": X won"<<endl;
      cout << "Case #"<<m<<": X won"<<endl; 
      }     
      else if (owon) {
      outfile << "Case #"<<m<<": O won"<<endl;
      cout << "Case #"<<m<<": O won"<<endl; 
      }
      else if (isdraw) {
      outfile << "Case #"<<m<<": Draw"<<endl;
      cout << "Case #"<<m<<": Draw"<<endl; 
      }
      else {
      outfile << "Case #"<<m<<": Game has not completed"<<endl;
      cout << "Case #"<<m<<": Game has not completed"<<endl; 
      }
      infile.get(c);
    }
    infile.close();
    outfile.close();
cin.ignore();
}
