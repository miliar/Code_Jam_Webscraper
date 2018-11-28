#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string s;
    getline(cin,s);
    for(int testcase=1;testcase<=t;testcase++)
    {
       char field[4][4];
       for(int i=0;i<4;i++)
       {
          string str;
          cin>>str;
          for(int j=0;j<4;j++)
            field[i][j]=str[j]; 
       }
       // string str;
       // cin>>str;
       string answer="";
       // for(int i=0;i<4;i++)
        // for(int j=0;j<4;j++)
          // cout<<field[i][j];
       // cout<<endl;
       for(int i=0;i<4;i++)
       {
        bool right=true;
        for(int j=0;j<4;j++)
          if(!(field[i][j]=='X' || field[i][j]=='T'))
            right=false;
        if(right) answer="X won";
       }
       for(int j=0;j<4;j++)
       {
        bool right=true;
        for(int i=0;i<4;i++)
          if(!(field[i][j]=='X' || field[i][j]=='T'))
            right=false;
        if(right) answer="X won";
       }
       {
          bool right=true;
          for(int i=0;i<4;i++)
            if(!(field[i][i]=='X' || field[i][i]=='T'))
              right=false;
          if(right) answer="X won";
       }
       {
          bool right=true;
          for(int i=0;i<4;i++)
            if(!(field[i][3-i]=='X' || field[i][3-i]=='T'))
              right=false;
          if(right) answer="X won";
       }
              for(int i=0;i<4;i++)
       {
        bool right=true;
        for(int j=0;j<4;j++)
          if(!(field[i][j]=='O' || field[i][j]=='T'))
            right=false;
        if(right) answer="O won";
       }
       for(int j=0;j<4;j++)
       {
        bool right=true;
        for(int i=0;i<4;i++)
          if(!(field[i][j]=='O' || field[i][j]=='T'))
            right=false;
        if(right) answer="O won";
       }
       {
          bool right=true;
          for(int i=0;i<4;i++)
            if(!(field[i][i]=='O' || field[i][i]=='T'))
              right=false;
          if(right) answer="O won";
       }
       {
          bool right=true;
          for(int i=0;i<4;i++)
            if(!(field[i][3-i]=='O' || field[i][3-i]=='T'))
              right=false;
          if(right) answer="O won";
       }
       if(answer=="")
       {
         bool ended=true;
         for(int i=0;i<4;i++)
          for(int j=0;j<4;j++)
            if(field[i][j]=='.') ended=false;
         if(ended)
          answer = "Draw";
         else
          answer = "Game has not completed";
       }
       cout<<"Case #"<<testcase<<": "<<answer<<endl;
    }
    return 0;
}
