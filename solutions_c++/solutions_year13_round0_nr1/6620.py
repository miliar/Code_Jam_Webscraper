#include<iostream>
using namespace std;
char check(char a,char b,char c,char d)
{
 if(a=='X' && b=='X' && c=='X' && d=='X')
 return 'X';
 else if(a=='O' && b=='O' && c=='O' && d=='O') 
 return 'O';
 else if(a=='.' || b=='.' || c=='.' || d=='.') 
 return '0'; 
 else if(a=='T' || b=='T' || c=='T' || d=='T')
 {
  if(a=='T')
  {
   if(b=='X'&& c=='X' && d=='X')
   return check('X',b,c,d);
   else if(b=='O' && c=='O' && d=='O')
   return check('O',b,c,d);
   else
   return 'n';          
  }     
  if(b=='T')
  {
   if(a=='X'&& c=='X' && d=='X')
   return check(a,'X',c,d);
   else if(a=='O' && c=='O' && d=='O')
   return check(b,'O',c,d); 
   else
   return 'n';             
  }     
  if(c=='T')
  {
   if(b=='X'&& a=='X' && d=='X')
   return check(a,b,'X',d);
   else if(b=='O' && a=='O' && d=='O')
   return check(a,b,'O',d); 
   else
   return 'n';          
  }     
  if(d=='T')
  {
   if(b=='X'&& c=='X' && a=='X')
   return check(a,b,c,'X');
   else if(b=='O' && c=='O' && a=='O')
   return check(a,b,c,'O');
   else
   return 'n';           
  }     
 } 
 return 'n';
}
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("op1.in","w",stdout);
    int t,z=1;
    cin>>t;
    yz:
    while(t--)
    {
              char a[4][4],c;
              for(int i=0;i<4;++i)
                      for(int j=0;j<4;++j)
                              cin>>a[i][j];
             
              //row check
              for(int i=0;i<4;++i)
              {
                 c=check(a[i][0],a[i][1],a[i][2],a[i][3]);  
                 //cout<<c;
                if(c=='X' || c=='O')
                          goto xy;
              }         
              //col check
               for(int i=0;i<4;++i)
              {
                 c=check(a[0][i],a[1][i],a[2][i],a[3][i]);  
                if(c=='X' || c=='O')
                          goto xy;
              }          
              //diag1 check
                c=check(a[0][0],a[1][1],a[2][2],a[3][3]);  
               // cout<<c;
                if(c=='X' || c=='O')
                          goto xy;
                //diag2 check
                 c=check(a[0][3],a[1][2],a[2][1],a[3][0]);
                 //cout<<c;  
                if(c=='X' || c=='O')
                          goto xy;
              
                 //not finished
              for(int i=0;i<4;++i)
              {
               for(int j=0;j<4;++j)
                       if(a[i][j]=='.')
                       {
                        cout<<"Case #"<<z++<<": "<<"Game has not completed\n";
                        //break;
                        goto yz;             
                       }        
              }
                //draw
                if(c=='n')
                {cout<<"Case #"<<z++<<": "<<"Draw\n";goto yz;}
              xy:
                         cout<<"Case #"<<z++<<": "<<c<<" won\n";
                         
    }
 return 0;    
}
