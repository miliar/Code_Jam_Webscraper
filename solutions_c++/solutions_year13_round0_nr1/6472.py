#include<iostream>
#include<fstream>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("al.out","w",stdout);
    char a[5][5];
    int n;
    cin>>n;
    int times=0;
    while(n--){
        times++;
        int flag=0;
        int flag2=0;
        char win;
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        cin>>a[i][j];
                        if(a[i][j]=='.')
                           flag=1;
                        }
                        }
        int otimes=0,xtimes=0,ttimes=0;
        for(int k=0;k<4;k++){
                otimes=0;xtimes=0,ttimes=0;
                for(int g=0;g<4;g++){
                        if(a[k][g]=='O'){
                              otimes++;
                              }
                        else if(a[k][g]=='X'){
                              xtimes++;
                              }
                        else if(a[k][g]=='T'){
                              ttimes++;
                              }
                              }
                if(otimes==4||(otimes==3&&ttimes==1)){
                              win='O';
                              flag2=1;
                              }
                else if(xtimes==4||(xtimes==3&&ttimes==1)){
                              win='X';
                              flag2=1;
                              }
                if(flag2==1)
                     break;
                     }
        if(flag2==0){
        for(int k=0;k<4;k++){
                otimes=0;xtimes=0,ttimes=0;
                for(int g=0;g<4;g++){
                        if(a[g][k]=='O'){
                              otimes++;
                              }
                        else if(a[g][k]=='X'){
                              xtimes++;
                              }
                        else if(a[g][k]=='T'){
                              ttimes++;
                              }
                              }
                if(otimes==4||(otimes==3&&ttimes==1)){
                              win='O';
                              flag2=1;
                              }
                else if(xtimes==4||(xtimes==3&&ttimes==1)){
                              win='X';
                              flag2=1;
                              }
                if(flag2==1)
                     break;
                     }
                     }
        if(flag2==0){
               otimes=0;xtimes=0,ttimes=0;
                for(int i=0;i<4;i++){
                       if(a[i][i]=='O'){
                              otimes++;
                              }
                        else if(a[i][i]=='X'){
                              xtimes++;
                              }
                        else if(a[i][i]=='T'){
                              ttimes++;
                              }
                              }
                if(otimes==4||(otimes==3&&ttimes==1)){
                              win='O';
                              flag2=1;
                              }
                else if(xtimes==4||(xtimes==3&&ttimes==1)){
                              win='X';
                              flag2=1;
                              }
                              }
        if(flag2==0){
               otimes=0;xtimes=0,ttimes=0;
                for(int i=0;i<4;i++){
                       if(a[i][3-i]=='O'){
                              otimes++;
                              }
                        else if(a[i][3-i]=='X'){
                              xtimes++;
                              }
                        else if(a[i][3-i]=='T'){
                              ttimes++;
                              }
                              }
                if(otimes==4||(otimes==3&&ttimes==1)){
                              win='O';
                              flag2=1;
                              }
                else if(xtimes==4||(xtimes==3&&ttimes==1)){
                              win='X';
                              flag2=1;
                              }
                              }
        cout<<"Case #"<<times<<": ";
        if(flag2==1){
          cout<<win<<" won"<<endl;
          }
        else {
          if(flag==1){
            cout<<"Game has not completed"<<endl;
            }
          else if(flag==0){
            cout<<"Draw"<<endl;
            }
            }
            }
        return 0;
}
       /* for(int k=0;k<4;k++){
                for(int g=1;g<4;g++){
                         if(a[k][g]!=a[k][g-1]){
                            if((g==1&&a[k][g-1]!='T')||(g==3&&a[k][g]!='T')
                               break;
                               }
                               }
                if(g>=4){
                         break;
                         }
                         }
        if(k<4){
                win=a[k][1];
                }
        for(int i=0;i<4;i++){
                for(int j=1;j<4;j++){
                        if(a[j-1][i]!=a[j][i]){
                             if((j==1&&a[j-1][i]!='T')||j==3&&a[j][i]!='T'){
                                  break;
                                  }
                                  }
                        if(j>=4){
                            break;
                            }
                if(i<4){
                        win=a[i][1];
                        }
        for(int k=0;k<4;k++){
                if(a[k-1][k-1]!=a[k][k]){
                      times++;
                      if((k==1&&a[k-1][k-1]=='T')||(k==3&&a[k][k]=='T')){
                              break;
                              }
                              }
                              }
        if(k>=4&&times<2){
               win=a[1][1];
               }
        for(int g=1;g<4;g++){
                if(a[g-1][3-(g-1)])!=a[g][3-g]{
                       times++;
                       if((g==1&&a[g-1][3-(g-1)]=='T')||(g==3&&a[g][3-g])=='T'){
                                break;
                                }
                                }
                                }
        if(g>=4&&times<2){
                        win=a[1][3-1];
                        }*/
        
                
        
