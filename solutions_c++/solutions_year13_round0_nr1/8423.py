#include<stdio.h>
#include<conio.h>
#include<fstream>
using namespace std;
char a[5][5];
bool cek2(char b)
{
     for(int x=1;x<=4;x++)
    { int has(0);
         for(int c=1;c<=4;c++)if(a[x][c]==b || a[x][c]=='T')has++;
         printf("%d",has);
         if(has==4)return true;
         has=0;
    }
    
     for(int x=1;x<=4;x++)
    { int has(0);
         for(int c=1;c<=4;c++)if(a[c][x]==b || a[c][x]=='T')has++;
         if(has==4)return true;
         has=0;
    }
    int o(0);
    for(int x=1;x<=4;x++)if(a[x][x]==b || a[x][x]=='T')o++;
    
         
       //  printf("%d\n",o);
         if(o==4)return true;
         o=0;
    int AB(1);
    
    for(int x=4;x>=1;x--)
    {
    // printf("%d %c %d %d\n",o,a[x][AB],x,AB);
            if(a[x][AB]==b || a[x][AB]=='T')o++;
            AB++;
    }
    
         
         if(o==4)return true;
    o=0;
    
    return false;
}
int main()
{
    ofstream myfile;
    myfile.open("output.txt");
    
    int t;
    scanf("%d",&t);
    for(int y=1;y<=t;y++)
    {
    bool haha=false;
    for(int x=1;x<=4;x++)for(int c=1;c<=4;c++){scanf("%c",&a[x][c]);if(a[x][c]=='\n'){scanf("%c",&a[x][c]);}if(a[x][c]=='.')haha=true;}
    
    bool cekx=0,ceko=0;
    cekx=cek2('X');
    ceko=cek2('O');
    printf("%d %d\n",cekx,ceko);
    myfile<<"Case #"<<y<<": ";
    printf("Case #%d: ",y);
    if(!(cekx || ceko) && !(haha)){printf("Draw");myfile<<"Draw";}
    else if(cekx){printf("X won");myfile << "X won";}
    else if(ceko){printf("O won");myfile <<"O won";}
    else {printf("Game has not completed");myfile<<"Game has not completed";}
    printf("\n");myfile<<endl;
    }
    myfile.close();
    return 0;
}
