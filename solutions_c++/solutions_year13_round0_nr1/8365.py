#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;

int checkO(int a,int b,int c,int d)
{
     //cout<<a<<b<<c<<d<<endl;
     if(a==0 && b==0 && c==0 && d==0)
     return 1;
     if(a==0 && b==0 && c==0 && d==2)
     return 1;
     if(a==0 && b==0 && c==2 && d==0)
     return 1;
     if(a==0 && b==2 && c==0 && d==0)
     return 1;
     if(a==2 && b==0 && c==0 && d==0)
     return 1;
     return 0;
}

int checkX(int a,int b,int c,int d)
{
     if(a==1 && b==1 && c==1 && d==1)
     return 1;
     if(a==1 && b==1 && c==1 && d==2)
     return 1;
     if(a==1 && b==1 && c==2 && d==1)
     return 1;
     if(a==1 && b==2 && c==1 && d==1)
     return 1;
     if(a==2 && b==1 && c==1 && d==1)
     return 1;
     return 0;
}

int checkN(int a,int b,int c,int d)
{
     if(a==3 && b==3 && c==3 && d==3)
     return 1;
     return 0;
}


char* decisionmaking(int N,int O,int X)
{
    if(O==0 && X==1)
    return ": X won";
    if(O==1 && X==0)
    return ": O won";
    if(O==0 && X==0 && N==1)
    return ": Game has not completed";
    if(O==0 && X==0 && N==0)
    return ": Draw";
    if(O==1 && X==1)
    return ": Draw";
    }
    
int main()
{
    ifstream fin;
    fin.open("A-small-attempt1.in");
    ofstream fout;
    fout.open("A-small-output1.in");
    
    int changetoarray[500][500],i=0,h=0,pos=0,num=-1,j,miniarray[16];
    char ch;
    
    while(fin)
    {
           fin.get(ch);
           if(!fin) break;
           if(num==-1) {num=ch-48;fin.get(ch);}
           else
           {
           if(ch!='\n' | ch!=' '| ch!='\0') 
           {
                       if(ch=='.')
                       {
                       //cout<<pos<<i<<endl;
                       changetoarray[pos][i]=3;i=i+1;}
                       else if(ch=='X')
                       {changetoarray[pos][i]=1;i=i+1;}
                       else if(ch=='T')
                       {changetoarray[pos][i]=2;i=i+1;}
                       else if(ch=='O')
                       {changetoarray[pos][i]=0;i=i+1;}
                       if(i==16)  //dont change to 15
                       {
                                pos++;
                                i=0; 
                                }
                       }
           }
    }
    
    i=0;    
    //cout<<changetoarray[0][15]<<"\n\n\n";
    
    int miniplan[50]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,5,10,15,3,6,9,12,0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15},N,O,X;
    int casen=1;
    
    for(j=0;j<pos;j++)
    {
              /*cout<<endl;
              
              for(h=0;h<16;h++)
                 cout<<changetoarray[j][h];
              
              cout<<endl;*/
              
              for(h=0;h<=36;h++)  
                  if(h%4==0)
                      {
                      O=checkO(changetoarray[j][miniplan[h]],changetoarray[j][miniplan[h+1]],changetoarray[j][miniplan[h+2]],changetoarray[j][miniplan[h+3]]);
                      if(O==1) break;
                      }
              //cout<<endl<<"O="<<O;
              
              for(h=0;h<=36;h++)  
                  if(h%4==0)
                      {
                      X=checkX(changetoarray[j][miniplan[h]],changetoarray[j][miniplan[h+1]],changetoarray[j][miniplan[h+2]],changetoarray[j][miniplan[h+3]]);
                      if(X==1) break;
                      }
              //cout<<endl<<"X="<<X;
              
              for(h=0;h<=36;h++)  
                  if(h%4==0)
                      {
                      N=checkN(changetoarray[j][miniplan[h]],changetoarray[j][miniplan[h+1]],changetoarray[j][miniplan[h+2]],changetoarray[j][miniplan[h+3]]);
                      if(N==1) break;
                      }
              //cout<<endl<<"N="<<N;
              if(j==pos-1)
              {
              fout<<"Case #"<<casen<<decisionmaking(N,O,X);
                          }
              else
              fout<<"Case #"<<casen<<decisionmaking(N,O,X)<<endl;
              casen++;
    }

    fin.close();
    fout.close();
    return 0;
    }
