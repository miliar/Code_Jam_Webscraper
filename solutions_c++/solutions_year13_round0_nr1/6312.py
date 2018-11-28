#include<fstream>

using namespace std;

int main(){
   int c;
   ifstream fin("A-large.in");
   ofstream fout("A-large.out");
   fin>>c;
   for(int t=1;t<=c;t++){
           bool yy=false;
           char a[4][4];
           for(int i=0;i!=4;i++)
            for(int j=0;j!=4;j++)
             fin>>a[i][j];
           for(int i=0;i!=4;i++){
            int x=0,y=0;
            for(int j=0;j!=4;j++){
                    if(a[i][j]=='X') x++;
                    if(a[i][j]=='O') y++;
                    if(a[i][j]=='T') x++,y++;
                    }     
            if(x==4){fout<<"Case #"<<t<<": "<<"X won"<<endl;yy=true;}
            if(y==4){fout<<"Case #"<<t<<": "<<"O won"<<endl;yy=true;}   
            }
           if(yy) continue;
           for(int i=0;i!=4;i++){
            int x=0,y=0;
            for(int j=0;j!=4;j++){
                    if(a[j][i]=='X') x++;
                    if(a[j][i]=='O') y++;
                    if(a[j][i]=='T') x++,y++;
                    }     
            if(x==4){fout<<"Case #"<<t<<": "<<"X won"<<endl;yy=true;}
            if(y==4){fout<<"Case #"<<t<<": "<<"O won"<<endl;yy=true;}     
            }
           if(yy) continue; 
           int x=0,y=0;
           for(int i=0;i!=4;i++){
                   if(a[i][i]=='X') x++;
                    if(a[i][i]=='O') y++;
                    if(a[i][i]=='T') x++,y++;
                   }
           if(x==4){fout<<"Case #"<<t<<": "<<"X won"<<endl;continue;}
            if(y==4){fout<<"Case #"<<t<<": "<<"O won"<<endl;continue;}      
           x=0,y=0;
           for(int i=0;i!=4;i++){
                   if(a[i][3-i]=='X') x++;
                    if(a[i][3-i]=='O') y++;
                    if(a[i][3-i]=='T') x++,y++;
                   }
           if(x==4){fout<<"Case #"<<t<<": "<<"X won"<<endl;continue;}
            if(y==4){fout<<"Case #"<<t<<": "<<"O won"<<endl;continue;} 
           
           for(int i=0;i!=4;i++){
            for(int j=0;j!=4;j++)
             if(a[i][j]=='.'){fout<<"Case #"<<t<<": "<<"Game has not completed"<<endl;yy=true;break;}
             if(yy) break;
             }
           if(yy) continue;
           
           fout<<"Case #"<<t<<": "<<"Draw"<<endl;
           }
} 
