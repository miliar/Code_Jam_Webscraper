#include <iostream>
#include <fstream>

using namespace std;
int T;
char a[4][4];
void referee(char ra[4][4]);
ifstream fin("A-small-attempt0.in");
ofstream fout("output.txt");
int main()
{
    fin>>T;
    for(int h=0;h<T;h++){
    fout<<"Case "<<"#"<<h+1<<": ";

    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
      fin>>a[i][j];
        }
    }
     referee(a);
    }
    return 0;
    system("pause");
}


void referee(char ra[4][4])
{
    char x='X',o='O',t='T',dot='.';
    int f1=0,f2=0,f3=0,f4=0,f5=0;

    for(int u=0;u<4;u++){

      if( ((ra[u][0]==x)||(ra[u][0]==t)) && ((ra[u][1]==x)||(ra[u][1]==t)) && ((ra[u][2]==x)||(ra[u][2]==t)) && ((ra[u][3]==x)||(ra[u][3]==t)) ){
       fout<<"X won"<<endl;f1+=1;break;  }

      if( ((ra[u][0]==o)||(ra[u][0]==t)) && ((ra[u][1]==o)||(ra[u][1]==t)) && ((ra[u][2]==o)||(ra[u][2]==t)) && ((ra[u][3]==o)||(ra[u][3]==t)) ){
       fout<<"O won"<<endl;f1+=1;break;  }
       }
if(f1==0){
 for(int v=0;v<4;v++){

 if( ((ra[0][v]==x)||(ra[0][v]==t)) && ((ra[1][v]==x)||(ra[1][v]==t)) && ((ra[2][v]==x)||(ra[2][v]==t)) && ((ra[3][v]==x)||(ra[3][v]==t)) ){
       fout<<"X won"<<endl;f2+=1;break;  }

      if( ((ra[0][v]==o)||(ra[0][v]==t)) && ((ra[1][v]==o)||(ra[1][v]==t)) && ((ra[2][v]==o)||(ra[2][v]==t)) && ((ra[3][v]==o)||(ra[3][v]==t)) ){
       fout<<"O won"<<endl;f2+=1;break;  }    }

}
if(f2==0){

      if( ((ra[0][0]==x)||(ra[0][0]==t)) && ((ra[1][1]==x)||(ra[1][1]==t)) && ((ra[2][2]==x)||(ra[2][2]==t)) && ((ra[3][3]==x)||(ra[3][3]==t)) ){
       fout<<"X won"<<endl;f3+=1;}

      else if( ((ra[0][0]==o)||(ra[0][0]==t)) && ((ra[1][1]==o)||(ra[1][1]==t)) && ((ra[2][2]==o)||(ra[2][2]==t)) && ((ra[3][3]==o)||(ra[3][3]==t)) ){
       fout<<"O won"<<endl;f3+=1;}


}
if(f3==0){
       if( ((ra[0][3]==x)||(ra[0][3]==t)) && ((ra[1][2]==x)||(ra[1][2]==t)) && ((ra[2][1]==x)||(ra[2][1]==t)) && ((ra[3][0]==x)||(ra[3][0]==t)) ){
       fout<<"X won"<<endl;f4+=1;}

       else if( ((ra[0][3]==o)||(ra[0][3]==t)) && ((ra[1][2]==o)||(ra[1][2]==t)) && ((ra[2][1]==o)||(ra[2][1]==t)) && ((ra[3][0]==o)||(ra[3][0]==t)) ){
       fout<<"O won"<<endl;f4+=1;}

}

if(f1==0&&f2==0&&f3==0&&f4==0){

for(int a=0;a<4;a++){
    for(int b=0;b<4;b++){
    if( ra[a][b]==dot){
    fout<<"Game has not completed"<<endl;
    f5+=1;break;
                                }

                            }
    if(f5>0)break;
                    }
if(f5==0)fout<<"Draw"<<endl;
}
}
