#include<iostream>
#include<fstream>
using namespace std;

char findStatus(char [][4]);
int main(){
    int T, i, j, k;
    char B[4][4], stat='\0';
    string status;
    string str;
    ifstream file;
    ofstream file1;
    ofstream ofile;
    
    file.open("A-small-attempt0.in");
    ofile.open("output.out");
    file >> T;
    
    for(i=0;i<T;i++)
    {
        for(j=0;j<4;j++)
        {
            file>>B[j][0]>>B[j][1]>>B[j][2]>>B[j][3];
        }
        for(j=0;j<4;j++)
        {
            cout<<B[j][0]<<B[j][1]<<B[j][2]<<B[j][3]<<endl;
        }
         
    stat=findStatus(B);
       
    if(stat=='X') status="X won";
    else if(stat=='O') status="O won";
    else if(stat=='.') status="Game has not completed";
    else if(stat=='N') status="Game has not completed";
    else if(stat=='D') status="Draw";
    ofile<<"Case #"<<i+1<<": "<<status<<endl;
    file1 << endl;
    cout << endl;
    //getline(file, str);
    }
}
    
char findStatus(char V[][4])
{
     int i, j, flag=0;
     for(i=0;i<4;i++)//vertical checking
     {
         if(V[0][i]==V[1][i])
         {
              if(V[1][i]==V[2][i]){if(V[2][i]==V[3][i] || V[3][i]=='T') return V[0][i];}
              else if((V[2][i]=='T') && (V[1][i]==V[3][i])) {if(V[0][i]!='.') return V[0][i];}
              //else if((V[i+3][0]=='T') && (V[i+2][0]==V[i+1][0])) return V[i][0];
         }
         else if(V[0][i]=='T')
              {if(V[1][i]==V[2][i] && V[2][i]==V[3][i]) {if(V[1][i]!='.') return V[1][i];}}
         else if(V[1][i]=='T')
              {if(V[2][i]==V[0][i] && V[2][i]==V[3][i]) {if(V[0][i]!='.') return V[0][i];}}
     }
     
     for(i=0;i<4;i++)//horizontal checking
     {
         if(V[i][0]==V[i][1])
         {
              if(V[i][1]==V[i][2]){if(V[i][2]==V[i][3] || V[i][3]=='T'){if(V[i][0]!='.') return V[i][0];}}
              else if((V[i][2]=='T') && (V[i][0]==V[i][3])) {if(V[i][0]!='.') return V[i][0];}
              //else if((V[0][i+3]=='T') && (V[0][i+2]==V[0][i+1])) return V[0][i];
         }
         else if(V[i][0]=='T')
              {if(V[i][1]==V[i][2] && V[i][2]==V[i][3]) {if(V[i][1]!='.') return V[i][1];}}
         else if(V[i][1]=='T')
              {if(V[i][0]==V[i][2] && V[i][2]==V[i][3]) {if(V[i][0]!='.') return V[i][0];}}
     }
     
     //diagonal checking1
         if(V[0][0]==V[1][1])
         {
              if(V[1][1]==V[2][2]){if(V[2][2]==V[3][3] || V[3][3]=='T') return V[0][0];}
              else if((V[2][2]=='T') && (V[3][3]==V[1][1])) {if(V[0][0]!='.') return V[0][0];}
              //else if((V[3][3]=='T') && (V[2][2]==V[1][1])) return V[0][0];
         }
         else if(V[0][0]=='T')
              {if(V[1][1]==V[2][2] && V[2][2]==V[3][3]) {if(V[1][1]!='.') return V[1][1];}}
         else if(V[1][1]=='T')
              {if(V[0][0]==V[2][2] && V[2][2]==V[3][3]) {if(V[0][0]!='.') return V[0][0];}}
     
     
     //diagonal checking2
         if(V[0][3]==V[1][2])
         {
              if(V[1][2]==V[2][1]){if(V[2][1]==V[0][3] || V[0][3]=='T') return V[0][3];}
              else if((V[2][1]=='T') && (V[1][2]==V[3][0])) {if(V[0][3]!='.') return V[0][3];}
              //else if((V[3][0]=='T') && (V[1][2]==V[2][1])) return V[0][3];
         }
         else if(V[0][3]=='T')
              {if(V[1][2]==V[2][1] && V[2][1]==V[3][0]) {if(V[1][2]!='.') return V[1][2];}}
         else if(V[1][2]=='T')
              {if(V[0][3]==V[2][1] && V[2][1]==V[3][0]) {if(V[0][3]!='.') return V[0][3];}}
              
         for(i=0;i<4;i++)
         {
              for(j=0;j<4;j++)
              {
                  if(V[i][j]=='.') flag=1;
              }
              cout<<"hello"<<"  "<<flag<<endl;
              if(flag==1) break;
         }
         if(flag==1) return 'N';
         
         return 'D';
}
