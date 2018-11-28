#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

string amoxsna(char a[4][4]){
       int n=0,m=0;
       string s="";
       int mas[6][6];
       for (int i=0; i<6; i++){
           for (int j=0; j<6; j++){
               mas[i][j]=0;
           }
       }
       for (int i=0; i<4; i++){
           for (int j=0; j<4; j++){
               if (a[i][j]=='X' || a[i][j]=='T') mas[i][4]++; 
               if (a[i][j]=='O' || a[i][j]=='T') mas[i][5]++; 
               if (a[j][i]=='X' || a[j][i]=='T') mas[4][i]++; 
               if (a[j][i]=='O' || a[j][i]=='T') mas[5][i]++; 
           }
       }
       //cout<<mas[4][3]<<"  ";
       
       int sumx=mas[0][4]+mas[1][4]+mas[1][4]+mas[3][4];
       int sumo=mas[0][5]+mas[1][5]+mas[1][5]+mas[3][5];
       int r1=0, r2=0,r3=0,r4=0;
       for (int i=0; i<4; i++){
           if (a[i][i]=='X' || a[i][i]=='T') r1++;
           if (a[i][i]=='O' || a[i][i]=='T') r2++;
           if (a[i][3-i]=='X' || a[i][3-i]=='T') r3++;
           if (a[i][3-i]=='O' || a[i][3-i]=='T') r4++;
       }
       if (r1==4) s="X won";
       else {
            if (r3==4) s="X won";
            else {
                 if (r2==4) s="O won";
                 else {
                      if (r4==4) s="O won";
                      else {
                      for (int i=0; i<4; i++){
                          
           if (mas[i][4]==4) {
              s="X won";
              break;
           } 
           else {
               if (mas[i][5]==4){
                  s="O won";
                  break;                  
               }
               else {
                    if (mas[4][i]==4){
                       s="X won";
                       break;
                    }
                    else {
                         if (mas[5][i]==4){
                            s="O won";
                            break;
                         }    
                              else {          
                                    if (i==3 && (sumx+sumo-1)>14) {
                                       s="Draw";
                                       break;
                                    }
                                    else {
                                         if (i==3){
                                         s="Game has not completed";
                                         break;
                                         }
                                         
                                    }
                              }
                    }
               }
           }
           
       }
                      
                      
                      
                      
                      }
                 }
            }     
       }
       
       

       return s;
}

int main(){
    freopen("A-small-attempt5.in", "r", stdin);
    freopen("A-small-attempt5.out", "w", stdout);
    int t;
    string st[2000];
    cin>>t;
    string s="";
    char a[4][4];
    for (int i=0; i<t; i++){
        for (int j=0; j<4; j++){
            for (int k=0; k<4; k++){
                cin>>a[j][k];    
            }
        }
        s=amoxsna(a);
        st[i]=s;
    }
    for (int i=0; i<t; i++){
        cout<<"Case #"<<i+1<<": "<<st[i];
        if (i<t-1) cout<<endl;
    }
    
    //system("pause");
    return 0;
}
