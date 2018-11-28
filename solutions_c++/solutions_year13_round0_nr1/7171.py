#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin ("A-large.in");
    ofstream cout ("A-large.out");
    /////
    int ctr = 1, n, x, o, tidx = -1, ms = 0;
    bool xwon = false, owon = true, owillwin = false, xwillwin = false;
    string s[5], z, ans;
    cin>>n;
    while(n--)
    {
              xwon = true;
              owon = true;
              xwillwin = false;
              owillwin = false;
              ms = 0;
              cin>>s[0]>>s[1]>>s[2]>>s[3];
              z = s[0] + s[1] + s[2] + s[3];
              for(int i = 0; i < 16; ++i)
                      if(z[i] != '.')
                              ms++;
              
              for(int i = 0; i < 4; ++i)
                      if(s[0][i] == '.' || s[0][i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[1][i] == '.' || s[1][i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[2][i] == '.' || s[2][i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[3][i] == '.' || s[3][i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              //////////////////
              for(int i = 0; i < 4; ++i)
                      if(s[i][0] == '.' || s[i][0] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][1] == '.' || s[i][1] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][2] == '.' || s[i][2] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][3] == '.' || s[i][3] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              //////////////////
              for(int i = 0; i < 4; ++i)
                      if(s[i][i] == '.' || s[i][i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
                  
              for(int i = 0; i < 4; ++i)
                      if(s[i][3-i] == '.' || s[i][3-i] == 'X')
                                 owon = false;
              if(owon)
                      owillwin = true;
              else
                  owon = true;
              ////////////////////////////
              ////////////////////////////
              ////////////////////////////
              for(int i = 0; i < 4; ++i)
                      if(s[0][i] == '.' || s[0][i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[1][i] == '.' || s[1][i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[2][i] == '.' || s[2][i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[3][i] == '.' || s[3][i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              //////////////////
              for(int i = 0; i < 4; ++i)
                      if(s[i][0] == '.' || s[i][0] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][1] == '.' || s[i][1] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][2] == '.' || s[i][2] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              
              for(int i = 0; i < 4; ++i)
                      if(s[i][3] == '.' || s[i][3] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              //////////////////
              for(int i = 0; i < 4; ++i)
                      if(s[i][i] == '.' || s[i][i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
                  
              for(int i = 0; i < 4; ++i)
                      if(s[i][3-i] == '.' || s[i][3-i] == 'O')
                                 xwon = false;
              if(xwon)
                      xwillwin = true;
              else
                  xwon = true;
              ///////////////////////
              if(!xwillwin && !owillwin)
              {
                           if(ms == 16)
                                 ans = "Draw";
                           else
                               ans = "Game has not completed"; 
                           }
              if(xwillwin)
                   ans = "X won";
              if(owillwin)
                  ans = "O won";
              cout<<"Case #"<<ctr<<": "<<ans<<endl;
              ctr++;
              }
    return 0;
    //system("PAUSE");
    //return EXIT_SUCCESS;
}
