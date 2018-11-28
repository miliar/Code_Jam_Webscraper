#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int main()
{
   int T;
   cin>>T;
   cin.ignore();
   vector<string> result;
   result.push_back("Draw");
   result.push_back("X won");
   result.push_back("O won");
   result.push_back("Game has not completed");
   for(int cases=1;cases<=T;cases++)
   {
      char g[4][4];
      //Get the Input!!
      for(int i=0;i<4;i++)
      {
        string s;
        cin>>s;
        for(int j=0;j<s.length();j++)
        g[i][j]=s[j];
      }
      int row[4][2]={0};
      int col[4][2]={0};
      int diag[2][2]={0};
      int not_filled=0;
      //Populate Rows Columns Stats
      for(int i=0;i<4;i++)
      {
        for(int j=0;j<4;j++) 
        {
           if( g[i][j] == 'X')
           {
                if(i==j)
                  diag[0][0]++;
                else if((i+j)==3)
                  diag[1][0]++;

                row[i][0]++;
                col[j][0]++;
           }else if(g[i][j]=='O')
           {
                if(i==j)
                  diag[0][1]++;
                else if((i+j)==3)
                  diag[1][1]++;
                row[i][1]++;
                col[j][1]++;
           } else if(g[i][j]=='T')
           {
                if(i==j) 
                {
                  diag[0][0]++;
                  diag[0][1]++;
                } else if((i+j)==3)
                {
                  diag[1][0]++;
                  diag[1][1]++;
                }
                row[i][0]++;
                col[j][0]++;
                row[i][1]++;
                col[j][1]++;
                
           }else if(g[i][j]=='.')
            not_filled=1; 
        }
      }
    int won=0;//1 means X won .... 2 means O won .... 3 means draw ... 4 means not completed.
      //Check rows and columns first :)
      for(int i=0;i<4;i++)
      {
        if(row[i][0]==4 || col[i][0]==4)
        { 
            won=1;
            break;
        }
        if(row[i][1]==4 || col[i][1]==4)
        { 
            won=2;
            break;
        }
      }
      //Now check the diagnols
      for(int i=0;i<2;i++)
      {
        if(diag[0][0]==4 || diag[1][0]==4)
        {
            won=1;
            break;
        }
        if(diag[0][1]==4 || diag[1][1]==4)
        {
            won=2;
            break;
        }
      }
      if(won==0)//Still no winner yet!
      {
        if(not_filled==0)
        won=0;
        else won=3;
      }
    cout<<"Case #"<<cases<<": "<<result[won]<<endl;
   }
    

    return 0;
}
