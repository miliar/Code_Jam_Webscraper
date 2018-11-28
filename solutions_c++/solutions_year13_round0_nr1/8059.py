#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char field [4] [4];
char T('T');
 int count(char c)
 {
     int cnt=0;
     for(int i=0; i<4; i++)
     {
         for(int y=0; y<4; y++)
         {
             if(field[i][y]==c) cnt++;
         }
     }
     return cnt;
 }
bool find_win(char c)
{
    bool won= false;
    for(int i=0; i<4; i++)
    {
        bool tmp=true;
        for(int y(0); y<4; y++)
        {
            if(field[i][y]!=c && field[i][y]!=T){
                 tmp=false;
                 break;
            }
        }
        if(tmp) won=true;
        tmp=true;
        for(int y(0); y<4; y++)
        {
            if(field[y][i]!=c && field[y][i]!=T ) {
                tmp=false;
                break;
         }
        }
        if(tmp) won=true;

}
if((field[0][0]==c || field[0][0]==T) && (field[1][1]==c || field[1][1]==T) && (field[2][2]==c || field[2][2]==T) && (field[3][3]==c||field[3][3]== T))
{
    won=true;
}
if((field[0][3]==c || field[0][3]==T) && (field[1][2]==c || field[1][2]==T)&& (field[2][1]==c || field[2][1]==T) && (field[3][0]==c || field[3][0]==T) )
{
    won=true;
    }

return won;
}


int main()
{
    ifstream fin("C:/A-small-attempt10.in.txt");
    ofstream fout("C:/response.out");

    int n;
    fin>>n;
    string input;
    for(int u(1); u<=n; u++)
    {
        for(int i=0; i<4; i++)
        {
        fin>>input;
      for(int y=0;y<input.size(); y++)
      {
          field[i][y]=input[y];
      }
    }
    int x= count('X');
    int o= count('O');

    bool valid= true;
    bool x_win=false;
    bool o_win=false;

    if(x-o==1 || x-o==0)
    {
         x_win= find_win('X');
         o_win= find_win('O');
    }
    if(x_win==true && o_win==false ) fout<<"Case #"<<u<<": X won"<<endl;
    if(o_win==true && x_win==false) fout<<"Case #"<<u<<": O won"<<endl;
    if(x==8 && (o==7 || o==8) && x_win==false && o_win==false) fout<<"Case #"<<u<<": Draw"<<endl;
    if((x<8)&&(o<7 || o<8) &&(x_win==false && o_win==false)) fout<<"Case #"<<u<<": Game has not completed"<<endl;
    }


    return 0;
}
