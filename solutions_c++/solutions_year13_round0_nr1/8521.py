#include<fstream>
using namespace std;
int main()
{
     ifstream cin("A-small-attempt4.in");
    ofstream cout("A-small.out");
    int n,p;
    char e[5][5];
    cin>>n;
    for (int i=1;i<=n;i++)
      {
        p=0;
           bool a=false;
        for (int x=1;x<=4;x++)
          cin>>e[x][1]>>e[x][2]>>e[x][3]>>e[x][4]; 
          for (int x=1;x<=4;x++)
          {
             
           
           for (int y=1;y<=4;y++)
            {
          
         if (e[x][y]=='.'){a=true;}
          else
          {
         if (y==4) {if (e[x][4]==e[x][3]&&e[x][4]==e[x][2]&&e[x][4]==e[x][1]){cout<<"Case #"<<i<<": "<<e[x][4]<<" won"<<endl;p=1;break;}}
         if (y==3) { if ((e[x][3]==e[x][2]&&e[x][3]==e[x][1])&&e[x][4]=='T'){cout<<"Case #"<<i<<": "<<e[x][3]<<" won"<<endl;p=1;break;}}
         if (y==2) {if ((e[x][2]==e[x][3]&&e[x][2]==e[x][4])&&e[x][1]=='T'){cout<<"Case #"<<i<<": "<<e[x][2]<<" won"<<endl;p=1;break;}}
        if (x==4) {if (e[4][y]==e[3][y]&&e[4][y]==e[2][y]&&e[4][y]==e[1][y]){cout<<"Case #"<<i<<": "<<e[4][y]<<" won"<<endl;p=1;break;}}
         if (x==3) {if ((e[3][y]==e[3][y]&&e[3][y]==e[1][y])&&e[4][y]=='T'){cout<<"Case #"<<i<<": "<<e[3][y]<<" won"<<endl;p=1;break;}}
         if (x==2) {if ((e[2][y]==e[3][y]&&e[2][y]==e[4][y])&&e[1][y]=='T'){cout<<"Case #"<<i<<": "<<e[2][y]<<" won"<<endl;p=1;break;}}
          if (x==4&&y==4) {if (e[x-1][y-1]==e[x][y]&&e[x][y]==e[x-2][y-2]&&e[x][y]==e[x-3][y-3]){cout<<"Case #"<<i<<": "<<e[x][y]<<" won"<<endl;p=1;break;}}  
          if (x==3&&y==3) {if(e[x-1][y-1]==e[x][y]&&e[x][y]==e[x-2][y-2])if (e[x+1][y+1]=='T'){cout<<"Case #"<<i<<": "<<e[x][y]<<" won"<<endl;p=1;break;}}   
          if (x==2&&y==2) {if(e[x+1][y+1]==e[x][y]&&e[x][y]==e[x+2][y+2])if (e[x-1][y-1]=='T'){cout<<"Case #"<<i<<": "<<e[x][y]<<" won"<<endl;p=1;break;}}
          if (x==1&&y==4) {if (e[x+1][y-1]==e[x][y]&&e[x][y]==e[x+2][y-2]==e[x+3][y-3]){cout<<("Case #",i,": ",e[x][y]," won")<<endl;p=1;break;}}  
          if (x==2&&y==3) {if(e[x+1][y-1]==e[x][y]&&e[x][y]==e[x+2][y-2])if (e[1][4]=='T'){cout<<"Case #"<<i<<": "<<e[x][y]<<" won"<<endl;p=1;break;}}   
            if (x==3&&y==2) {if(e[x-1][y+1]==e[x][y]&&e[x][y]==e[x-2][y+2])if (e[4][1]=='T'){cout<<"Case #"<<i<<": "<<e[x][y]<<" won"<<endl;p=1;break;}}
           }    
           }
           
            if (p==1) break;
            }
    
             if (a==true&&p==0)
            {cout<<"Case #"<<i<<": Game has not completed"<<endl;}
             if (a==false&&p==0)  
            {cout<<"Case #"<<i<<": Draw"<<endl;}
          }         
  
      
    return 0;
}
