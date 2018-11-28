#include<iostream>
#include<fstream>
using namespace std;
int main()
{
  ifstream fin; fin.open("input");
  ofstream fout;  fout.open("output");
   int nt; fin>>nt;  int k,i,j;
     for(k=1;k<=nt;k++)
      {
          char a[4][4];  string s;  int xwon=0,owon=0,notdone=0;
          int xcol[4]={0},ocol[4]={0},tcol=-1,trow=-2,xd[2]={0},od[2]={0}; 
          for(i=0;i<4;i++)
               {
                 fin>>s;// cout<<s<<"\n";
                     int tpresent=0,xcount=0,ocount=0;
                 for(j=0;j<4;j++)
                    {
                      a[i][j]=s[j]; 
                      if(s[j]=='T') {tpresent=1; tcol=j; trow=i;}
                    else  if(s[j]=='O') 
                         {
                          ocount++;ocol[j]++;
                          if(i==j)  od[0]++;
                          if(i==(3-j)) od[1]++;
                         }
                     else if(s[j]=='X') 
                         {
                            xcount++; xcol[j]++;
                              if(i==j)  xd[0]++;
                              if(i==(3-j)) xd[1]++;
                         }
                      else notdone=1;
                    }
              if((tpresent==1&&ocount==3)||(ocount==4)){ owon=1; goto last;}
         else if((tpresent==1&&xcount==3)||(xcount==4)){ xwon=1; goto last;}
               }
         for(i=0;i<4;i++) 
               {
                 if((xcol[i]==3&&tcol==i)||xcol[i]==4) {xwon=1; goto print;}
                 if((ocol[i]==3&&tcol==i)||ocol[i]==4) {owon=1; goto print;}
               }
              if((xd[0]==3&&tcol==trow)||xd[0]==4) {xwon=1; goto print;}
              if((od[0]==3&&tcol==trow)||od[0]==4) {owon=1; goto print;}
              if((xd[1]==3&&(3-tcol)==trow)||xd[1]==4) {xwon=1; goto print;}
              if((od[1]==3&&(3-tcol)==trow)||od[1]==4) {owon=1; goto print;}
         goto print;
     last: i++; for(;i<4;i++){ fin>>s;/*cout<<s<<"\n";*/}
     print: fout<<"Case #"<<k<<": " ;
             if(xwon==1) fout<<"X won\n";
              else if(owon==1) fout<<"O won\n";
              else if(notdone==1) fout<<"Game has not completed\n";
              else fout<<"Draw\n"; // cout<<"\n";  
      }
   fin.close(); fout.close();
}
