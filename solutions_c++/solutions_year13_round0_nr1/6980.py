#include <iostream>
#include <string>
#include <fstream>

using namespace std;



bool player(char x,string a,string b,string c,string d)
{ 
     
     bool player1;                   
if(a[0] == x || a[0] == 'T')
{
        if(a[1] == x || a[1] == 'T')
        {
                if(a[2] == x || a[2] == 'T')
                {
                        if(a[3] == x || a[3] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}       

if(a[0] == x || a[0] == 'T')
{
        if(b[1] == x || b[1] == 'T')
        {
             if(c[2] == x || c[2] == 'T')                
             {
                  if(d[3] == x || d[3] == 'T')   
                     player1=true;
             }
        }
}

if(a[0] == x || a[0] == 'T')
{
        if(b[0] == x || b[0] == 'T')
        {
             if(c[0] == x || c[0] == 'T')                
             {
                  if(d[0] == x || d[0] == 'T')   
                     player1=true;
             }
        }   
}

if(a[1] == x || a[1] == 'T')
{
        if(b[1] == x || b[1] == 'T')
        {
                if(c[1] == x || c[1] == 'T')
                {
                        if(d[1] == x || d[1] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}

if(a[2] == x || a[2] == 'T')
{
        if(b[2] == x || b[2] == 'T')
        {
                if(c[2] == x || c[2] == 'T')
                {
                        if(d[2] == x || d[2] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}

if(a[3] == x || a[3] == 'T')
{
        if(b[3] == x || b[3] == 'T')
        {
                if(c[3] == x || c[3] == 'T')
                {
                        if(d[3] == x || d[3] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}

if(a[3] == x || a[3] == 'T')
{
       if(b[2] == x || b[2] == 'T')
        {
                if(c[1] == x || c[1] == 'T')
                {
                        if(d[0] == x || d[0] == 'T')
                        {
                                player1=true;
                        }
                }
        }

}


if(b[0] == x || b[0] == 'T')
{
        if(b[1] == x || b[1] == 'T')
        {
                if(b[2] == x || b[2] == 'T')
                {
                        if(b[3] == x || b[3] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}

if(c[0] == x || c[0] == 'T')
{
        if(c[1] == x || c[1] == 'T')
        {
                if(c[2] == x || c[2] == 'T')
                {
                        if(c[3] == x || c[3] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}
                     
if(d[0] == x || d[0] == 'T')
{
        if(d[1] == x || d[1] == 'T')
        {
                if(d[2] == x || d[2] == 'T')
                {
                        if(d[3] == x || d[3] == 'T')
                        {
                                player1=true;
                        }
                }
        }
}
return player1;
}



int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    
    int x,y,s=0;
    bool Player1=false,Player2=false;
    string a,b,c,d;
    fin>>x;
bool found;

if(x>=1 && x<=1000)
{    
for(int i=0;i<x;i++)
{
        s=0;
    found=false;    
    fin>>a;
    fin>>b;
    fin>>c;
    fin>>d;             

for(int m=0;m<4;m++)
{
        if(a[m]=='T' || b[m]=='T' || c[m]=='T' || d[m]=='T')
        s++;
}        

if(s>=2)
{
        goto stop;
}
for(int j=0;j<4;j++)
{
        if(a[j]=='.' || b[j]=='.' || c[j]=='.' || d[j]=='.')
        found=true;
}        
 
Player1=player('X',a,b,c,d);
Player2=player('O',a,b,c,d);

if(Player1==true)
fout<<"Case #"<<i+1<<": "<<"X won"<<endl;

else if(Player2==true)
fout<<"Case #"<<i+1<<": "<<"O won"<<endl;

else if(found == true)
{
               fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
}

else 
fout<<"Case #"<<i+1<<": "<<"Draw"<<endl; 
}

}
stop:
fin.close();
fout.close();
system("pause");
    return 0;
}
