#include<iostream>
using namespace std;
char ar[6][6];

int main(){
int tt;
cin>>tt;

for(int ww=0;ww<tt;ww++){
int win=0;
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
    cin>>ar[i][j];
    
    
    int x=0,o=0,t=0,flg=0;
    
    for(int i=1;i<=4;i++){
           x=0;o=0,t=0;
            for(int j=0;j<4;j++){
                    if(ar[i][j]=='X')x++;
                    else if(ar[i][j]=='O')o++;
                    else if(ar[i][j]=='T')t++;
                    else flg++;
                    }
            if(x+t==4 && t<2)win=1;
            else if(o+t==4 && t<2)win=2;
            
            
            
            }
    for(int i=0;i<4;i++){
           x=0;o=0,t=0;
            for(int j=0;j<4;j++){
                    if(ar[j][i]=='X')x++;
                    else if(ar[j][i]=='O')o++;
                    else if(ar[j][i]=='T')t++;
                    else flg++;
                    }
            if(x+t==4 && t<2)win=1;
            else if(o+t==4 && t<2)win=2;
            
            
            
            }
            
    
           x=0;o=0,t=0;
            for(int j=0;j<4;j++){
                    if(ar[j][j]=='X')x++;
                    else if(ar[j][j]=='O')o++;
                    else if(ar[j][j]=='T')t++;
                    else flg++;
                    }
            if(x+t==4 && t<2)win=1;
            else if(o+t==4 && t<2)win=2;
    
           x=0;o=0,t=0;
            for(int j=0;j<4;j++){
                    if(ar[j][3-j]=='X')x++;
                    else if(ar[j][3-j]=='O')o++;
                    else if(ar[j][3-j]=='T')t++;
                    else flg++;
                    }
            if(x+t==4 && t<2)win=1;
            else if(o+t==4 && t<2)win=2;
    
    
    if(win==1)cout<<"Case #"<<ww<<": X won\n";
    else if(win==2)cout<<"Case #"<<ww<<": O won\n";
    else if(flg!=0 && win==0)cout<<"Case #"<<ww<<": Game has not completed\n";
    else cout<<"Case #"<<ww<<": Draw\n";
    
} 
    
    }
