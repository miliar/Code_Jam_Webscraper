#include<iostream>
using namespace std;
bool win(char **a,char x);
bool draw(char **a);
int main()
{
    int t;
    char **a = new char*[4];
    for(int i=0;i<4;i++) a[i] = new char[4];
    cin>>t;
    string s1 = "X won",s2 = "O won",
    s3 = "Draw",s4 = "Game has not completed";
    for(int T=1;T<=t;T++)
    {
     for(int i=0;i<4;i++)
     for(int j=0;j<4;j++) cin>> a[i][j];
     
     if(win(a,'X')) cout<<"Case #"<<T<<": "<<s1<<"\n";
     else if(win(a,'O')) cout<<"Case #"<<T<<": "<<s2<<"\n";
     else if(draw(a)) cout<<"Case #"<<T<<": "<<s3<<"\n";
     else cout<<"Case #"<<T<<": "<<s4<<"\n";
    }
    return 0;
}
bool win(char **a,char x)
{
     int i,j;
     for(i=0;i<4;i++){
     for(j=0;j<4;j++) if(a[i][j]==x || a[i][j]=='T');
                      else break;
                      if(j==4) return true;
                      }
     for(i=0;i<4;i++){
     for(j=0;j<4;j++) if(a[j][i]==x || a[j][i]=='T');
                      else break;
                      if(j==4) return true;
                      }
     for(i=0;i<4;i++) if(a[i][i]==x || a[i][i]=='T');
                      else break;
     if(i==4) return true;
     for(i=0;i<4;i++) if(a[i][3-i]==x || a[i][3-i]=='T');
                      else break;
     if(i==4) return true;
     
     return false;
}
bool draw(char **a)
{
    int i,j;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++) if(a[i][j]!='.');
                     else return false;
    return true;
}
