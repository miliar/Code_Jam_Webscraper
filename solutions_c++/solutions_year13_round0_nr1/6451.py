#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

char verify(vector < vector<char> >);     

int main()
{
    freopen("In.txt","rt",stdin);
    freopen("Out.txt","wt",stdout);
    int i,j;
    char ans;
    vector < vector<char> > sq(4);
    int NT,TC=1;
    cin >> NT;cin.get();
    for(TC;TC<=NT;TC++)
    {
                    
                     i=0,j=0;
                     for(i=0;i<4;i++)
                     {
                                    sq[i].resize(4);
                                    for(j=0;j<4;j++)
                                    cin >> sq[i][j];
                                    cin.get();
                     }
                     cin.get();
                     ans=verify(sq);
                     cout << "Case #" << TC << ": ";
                     switch (ans)
                     {
                               case 'X': cout << "X won" << endl;break;
                               case 'O': cout << "O won" << endl;break;
                               case 'D': cout << "Draw"  << endl;break;
                               case 'N': cout << "Game has not completed" << endl;break;
                     }
    }
    return 0;
}

char verify(vector < vector <char> > sq)
{
     int i,j,cx,co,ct;
     //rows
     for(i=0;i<4;i++)
     {
                     cx=4,co=4,ct=1;
                     for(j=0;j<4;j++)
                     {
                                     cx-=(sq[i][j]=='X');
                                     co-=(sq[i][j]=='O');
                                     ct-=(sq[i][j]=='T');
                     }
                     if(cx==0 || (cx==1 && ct==0))
                     return 'X';
                     if(co==0 || (co==1 && ct==0))
                     return 'O';
     }                
     //columns
     for(j=0;j<4;j++)
     {
                     cx=4,co=4,ct=1;
                     for(i=0;i<4;i++)
                     {
                                     cx-=(sq[i][j]=='X');
                                     co-=(sq[i][j]=='O');
                                     ct-=(sq[i][j]=='T');
                     }
                     if(cx==0 || (cx==1 && ct==0))
                     return 'X';
                     if(co==0 || (co==1 && ct==0))
                     return 'O';
     }  
     
     //main diag
     i=0,j=0;
     cx=4,co=4,ct=1;
     while(i<4)
     {                     
                     cx-=(sq[i][j]=='X');
                     co-=(sq[i][j]=='O');
                     ct-=(sq[i][j]=='T');
                     i++,j++;
     }               
                     if(cx==0 || (cx==1 && ct==0))
                     return 'X';
                     if(co==0 || (co==1 && ct==0))
                     return 'O';
     
     //side diag
     i=0,j=3;
     cx=4,co=4,ct=1;     
     while(i<4)
     {
                     cx-=(sq[i][j]=='X');
                     co-=(sq[i][j]=='O');
                     ct-=(sq[i][j]=='T');
                     i++,j--;
     }
                     if(cx==0 || (cx==1 && ct==0))
                     return 'X';
                     if(co==0 || (co==1 && ct==0))
                     return 'O';
     int es=0;
     for(i=0;i<4;i++)
     for(j=0;j<4;j++)
     es+=(sq[i][j]=='.');
     if(es==0)
     return 'D';
     return 'N';
}
     
     
    
    
           
    
                    
