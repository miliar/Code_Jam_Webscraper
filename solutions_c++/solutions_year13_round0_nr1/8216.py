#include<conio.h>
#include<iostream.h>
#include<fstream.h>
int main()
{
    int t,i,j,k,finish,x,o,over;
    char game[5][5];
    ifstream fin("a.in");
    ofstream fout("a.OUT");
    fin>>t;
    for(k=0;k<t;k++)
    {
                    for(i=0;i<4;i++)
                      for(j=0;j<4;j++)
                      {    fin>>game[i][j];
                           game[i][4]=0;                           
                      }
                    finish=0;
                    x=o=over=0;
                    for(i=0;i<4;i++)//horizontal check
                    {
                                    for(j=0;j<4;j++)
                                       if(game[i][j]=='.')
                                         break;
                                       else if(game[i][j]!='T'&&game[i][(j+1)%4]!='T'&&game[i][j]!=game[i][(j+1)%4])
                                         break;
                                       else if(game[i][j]=='X')
                                         finish=1;
                                       else if(game[i][j]=='O')
                                         finish=2;
                                    if(j==4)
                                    {
                                            if(finish==1)
                                               x=1;
                                            else if(finish==2)
                                              o=1;
                                    }
                    }
                    for(j=0;j<4;j++)//vertical check
                    {
                                    for(i=0;i<4;i++)
                                       if(game[i][j]=='.')
                                         break;
                                       else if(game[i][j]!='T'&&game[(i+1)%4][j]!='T'&&game[i][j]!=game[(i+1)%4][j])
                                         break;
                                       else if(game[i][j]=='X')
                                         finish=1;
                                       else if(game[i][j]=='O')
                                         finish=2;
                                    if(i==4)
                                    {
                                            if(finish==1)
                                               x=1;
                                            else if(finish==2)
                                              o=1;
                                    }
                    }
                    for(i=0;i<4;i++)//main diag check
                    {
                                       if(game[i][i]=='.')
                                         break;
                                       else if(game[i][i]!='T'&&game[(i+1)%4][(i+1)%4]!='T'&&game[i][i]!=game[(i+1)%4][(i+1)%4])
                                         break;
                                       else if(game[i][i]=='X')
                                         finish=1;
                                       else if(game[i][i]=='O')
                                         finish=2;
                    }
                    if(i==4)
                    {
                                            if(finish==1)
                                               x=1;
                                            else if(finish==2)
                                              o=1;
                    }
                    
                    for(i=0;i<4;i++)//left diag check
                    {
                                       if(game[i][3-i]=='.')
                                         break;
                                       else if(game[i][3-i]!='T'&&game[(i+1)%4][(3-i-1)%4]!='T'&&game[i][3-i]!=game[(i+1)%4][(3-i-1)%4])
                                         break;
                                       else if(game[i][3-i]=='X')
                                         finish=1;
                                       else if(game[i][3-i]=='O')
                                         finish=2;
                    }
                    if(i==4)
                    {
                                            if(finish==1)
                                               x=1;
                                            else if(finish==2)
                                              o=1;
                    }
                    int tflag=0;
                    for(i=0;i<4;i++)
                    {  for(j=0;j<4;j++)
                        if(game[i][j]=='.')
                         { tflag=1;break;}
                    cout<<game[i];
                    }
                    if(!tflag)
                       over=1;
                    else over=0;
                    if(x)
                         cout<<"Case #"<<k+1<<": X won\n";
                    else if(o)
                         cout<<"Case #"<<k+1<<": O won\n";                      
                    else if(over)
                    {
                                      cout<<"Case #"<<k+1<<": Draw\n";
                    }else       cout<<"Case #"<<k+1<<": Game has not completed\n";
                    
                    if(x)
                         fout<<"Case #"<<k+1<<": X won"<<endl;
                    else if(o)
                         fout<<"Case #"<<k+1<<": O won"<<endl;                      
                    else if(over)
                    {
                                      fout<<"Case #"<<k+1<<": Draw"<<endl;
                    }else       fout<<"Case #"<<k+1<<": Game has not completed"<<endl;
                    
                    
                    
                    
                    //cout<<game[0]<<"\n"<<game[1]<<"\n"<<game[2]<<"\n"<<game[3]<<"\n\n";
    }
    getch();   
}
