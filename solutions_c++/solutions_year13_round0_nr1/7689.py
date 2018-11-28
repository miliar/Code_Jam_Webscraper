#include<iostream>
#include<fstream>
using namespace std;


int main()
{
char array[4][4];
int cases,j,k,l,check,check2;
int X,O,T,D;
ifstream i;
ofstream out;
i.open("A-large.in");
out.open("O.in");
i>>cases;
for (j=1;j<=cases;j++){
check =0;check2=0;    X=0,O=0,T=0,D=0;
    for (k=0;k<4;k++){
        for (l=0;l<4;l++) {
            i>>array[k][l];
            if (array[k][l]!='.') check2++;
        }//for (l=0;<l<3;l++)
    }//for (k=0;k<3;k++)
  
 if (check == 0) {  
    for (k=0;k<4;k++){
         X=0,O=0,T=0,D=0;
        for (l=0;l<4;l++) {
            if (array[k][l]=='X')X++;
            if (array[k][l]=='O')O++;
            if (array[k][l]=='T')T++;
            if (array[k][l]=='D')D++;
        }//for (l=0;<l<3;l++)
        if ((X==4)||((X==3)&&(T==1))) {check=1;break;}
        else if ((O==4)||((O==3)&&(T==1))) {check=2;break;}
        
    }//for (k=0;k<3;k++)
}//((check == 0)&&(check2 != 16))

   if (check == 0){
     for (l=0;l<4;l++){
           X=0,O=0,T=0,D=0;
        for (k=0;k<4;k++) {
            if (array[k][l]=='X')X++;
            if (array[k][l]=='O')O++;
            if (array[k][l]=='T')T++;
            if (array[k][l]=='D')D++;
        }//for (l=0;<l<3;l++)
        if ((X==4)||((X==3)&&(T==1))) {check=1;break;}
        else if ((O==4)||((O==3)&&(T==1))) {check=2;break;}
     }//for (k=0;k<3;k++)
    }//if (check == 0)
    
     if (check == 0){
           X=0,O=0,T=0,D=0;
     for (l=0,k=0;l<4,k<4;l++,k++){
            if (array[l][k]=='X')X++;
            if (array[l][k]=='O')O++;
            if (array[l][k]=='T')T++;
            if (array[l][k]=='D')D++;
     }//for (k=0;k<3;k++)
     if ((X==4)||((X==3)&&(T==1))) {check=1;}
        else if ((O==4)||((O==3)&&(T==1))) {check=2;}
    }//if (check == 0)
  
    if (check == 0){
           X=0,O=0,T=0,D=0;
     for (l=0,k=3;l<4,k>=0;l++,k--){
            if (array[l][k]=='X')X++;
            if (array[l][k]=='O')O++;
            if (array[l][k]=='T')T++;
            if (array[l][k]=='D')D++;
     }//for (k=0;k<3;k++)
      if ((X==4)||((X==3)&&(T==1))) {check=1;}
        else if ((O==4)||((O==3)&&(T==1))) {check=2;}
    }//if (check == 0)
    
    
    if ((check == 0)&&(check2 != 16)) out<<"Case #"<<j<<": "<<"Game has not completed"<<endl;
    else if ((check == 0)&&(check2 == 16)) out<<"Case #"<<j<<": "<<"Draw"<<endl;
    else if (check == 1) out<<"Case #"<<j<<": "<<"X won"<<endl;
    else if (check == 2) out<<"Case #"<<j<<": "<<"O won"<<endl;
    X=0;O=0;T=0;D=0;
}//for (j=0;j<cases;j++)


    //system("pause");
    return 0;
}

