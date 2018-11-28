#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
ifstream fin("data.in");
ofstream fout("data.out");
#define cin fin
#define cout fout
int main()
{
    int i,n,j,k1,k2,flag,flag1,flag2,flag3,flag4,flag5,flag6,flag7;
    char board[4][5],tips[23];
    cin>>n;
    i=1;
    while(i<=n){
        flag=0;
        j=0;
        strcpy(tips,"");
        while(j<4){
            cin>>board[j++];
        }
        for(k1=0;k1<4;k1++){
            //cout<<board[k1]<<endl;
            if(strcmp(board[k1],"XXXX")==0||strcmp(board[k1],"XXXT")==0||strcmp(board[k1],"XXTX")==0||strcmp(board[k1],"XTXX")==0||strcmp(board[k1],"TXXX")==0){
                flag=1;
                strcpy(tips,"X won");
                break;
            }
            if(strcmp(board[k1],"OOOO")==0||strcmp(board[k1],"OOOT")==0||strcmp(board[k1],"OOTO")==0||strcmp(board[k1],"OTOO")==0||strcmp(board[k1],"TOOO")==0){
                flag=1;
                strcpy(tips,"O won");
                break;
            }
        }
        if(!flag){
            //strcpy(down1,"");
            //strcpy(down2,"");
            //strcpy(down3,"");
            //strcpy(down4,"");
            flag1=0;
            char down1[5]={board[0][0],board[1][0],board[2][0],board[3][0]};
            char down2[5]={board[0][1],board[1][1],board[2][1],board[3][1]};
            char down3[5]={board[0][2],board[1][2],board[2][2],board[3][2]};
            char down4[5];
            down4[0]=board[0][3];
            down4[1]=board[1][3];
            down4[2]=board[2][3];
            down4[3]=board[3][3];
            //cout<<down1<<endl;
            /*for(k1=0;k1<4;k1++){
                strcat(down1,board[k1][0]);
            }
            for(k1=0;k1<4;k1++){
                strcat(down2,board[k1][1]);
            }
            for(k1=0;k1<4;k1++){
                strcat(down3,board[k1][2]);
            }

            for(k1=0;k1<4;k1++){
                strcat(down4,board[k1][3]);
            }*/
            if(strcmp(down1,"XXXX")==0||strcmp(down1,"XXXT")==0||strcmp(down1,"XXTX")==0||strcmp(down1,"XTXX")==0||strcmp(down1,"TXXX")==0){
                flag1=1;
                strcpy(tips,"X won");
            }
            if(strcmp(down1,"OOOO")==0||strcmp(down1,"OOOT")==0||strcmp(down1,"OOTO")==0||strcmp(down1,"OTOO")==0||strcmp(down1,"TOOO")==0){
                flag1=1;
                strcpy(tips,"O won");
            }
            if(!flag1){
                flag2=0;
                if(strcmp(down2,"XXXX")==0||strcmp(down2,"XXXT")==0||strcmp(down2,"XXTX")==0||strcmp(down2,"XTXX")==0||strcmp(down2,"TXXX")==0){
                    flag2=1;
                    strcpy(tips,"X won");
                }
                if(strcmp(down2,"OOOO")==0||strcmp(down2,"OOOT")==0||strcmp(down2,"OOTO")==0||strcmp(down2,"OTOO")==0||strcmp(down2,"TOOO")==0){
                    flag2=1;
                    strcpy(tips,"O won");
                }
                if(!flag2){
                    flag3=0;
                    if(strcmp(down3,"XXXX")==0||strcmp(down3,"XXXT")==0||strcmp(down3,"XXTX")==0||strcmp(down3,"XTXX")==0||strcmp(down3,"TXXX")==0){
                        flag3=1;
                        strcpy(tips,"X won");
                    }
                    if(strcmp(down3,"OOOO")==0||strcmp(down3,"OOOT")==0||strcmp(down3,"OOTO")==0||strcmp(down3,"OTOO")==0||strcmp(down3,"TOOO")==0){
                        flag3=1;
                        strcpy(tips,"O won");
                    }
                    if(!flag3){
                        flag4=0;
                        if(strcmp(down4,"XXXX")==0||strcmp(down4,"XXXT")==0||strcmp(down4,"XXTX")==0||strcmp(down4,"XTXX")==0||strcmp(down4,"TXXX")==0){
                            flag4=1;
                            strcpy(tips,"X won");
                        }
                        if(strcmp(down4,"OOOO")==0||strcmp(down4,"OOOT")==0||strcmp(down4,"OOTO")==0||strcmp(down4,"OTOO")==0||strcmp(down4,"TOOO")==0){
                            flag4=1;
                            strcpy(tips,"O won");
                        }
                        if(!flag4){
                            flag5=0;
                            char dia1[5]={board[0][0],board[1][1],board[2][2],board[3][3]};
                            //cout<<dia1<<endl;
                            if(strcmp(dia1,"XXXX")==0||strcmp(dia1,"XXXT")==0||strcmp(dia1,"XXTX")==0||strcmp(dia1,"XTXX")==0||strcmp(dia1,"TXXX")==0){
                                flag5=1;
                                strcpy(tips,"X won");
                            }
                            if(strcmp(dia1,"OOOO")==0||strcmp(dia1,"OOOT")==0||strcmp(dia1,"OOTO")==0||strcmp(dia1,"OTOO")==0||strcmp(dia1,"TOOO")==0){
                                flag5=1;
                                strcpy(tips,"O won");
                            }
                            if(!flag5){
                                flag6=0;
                                char dia2[5]={board[0][3],board[1][2],board[2][1],board[3][0]};
                                if(strcmp(dia2,"XXXX")==0||strcmp(dia2,"XXXT")==0||strcmp(dia2,"XXTX")==0||strcmp(dia2,"XTXX")==0||strcmp(dia2,"TXXX")==0){
                                    flag6=1;
                                    strcpy(tips,"X won");
                                }
                                if(strcmp(dia2,"OOOO")==0||strcmp(dia2,"OOOT")==0||strcmp(dia2,"OOTO")==0||strcmp(dia2,"OTOO")==0||strcmp(dia2,"TOOO")==0){
                                    flag6=1;
                                    strcpy(tips,"O won");
                                }
                                if(!flag6){
                                    flag7=0;
                                    for(k2=0;k2<4;k2++){
                                        if(strchr(board[k2],'.')){
                                            flag7=1;
                                            strcpy(tips,"Game has not completed");
                                            break;
                                        }
                                    }
                                    if(!flag7){
                                        strcpy(tips,"Draw");
                                    }
                                    /*cout<<"================"<<endl;
                                    cout<<"last"<<endl;
                                    cout<<"================"<<endl;*/
                                    cout<<"Case #"<<i++<<": "<<tips<<endl;
                                }else{
                                    /*cout<<"================"<<endl;
                                    cout<<"dia2"<<endl;
                                    cout<<"================"<<endl;*/
                                    cout<<"Case #"<<i++<<": "<<tips<<endl;
                                }
                            }else{
                                /*cout<<"================"<<endl;
                                    cout<<"dia1"<<endl;
                                    cout<<"================"<<endl;*/
                                cout<<"Case #"<<i++<<": "<<tips<<endl;
                            }
                        }else{
                            /*cout<<"================"<<endl;
                                    cout<<"down4"<<endl;
                                    cout<<"================"<<endl;*/
                            cout<<"Case #"<<i++<<": "<<tips<<endl;
                        }
                    }else{
                        /*cout<<"================"<<endl;
                                    cout<<"down3"<<endl;
                                    cout<<"================"<<endl;*/
                        cout<<"Case #"<<i++<<": "<<tips<<endl;
                    }
                }else{
                    /*cout<<"================"<<endl;
                                    cout<<"down2"<<endl;
                                    cout<<"================"<<endl;*/
                    cout<<"Case #"<<i++<<": "<<tips<<endl;
                }
            }else{
                /*cout<<"================"<<endl;
                                    cout<<"down1"<<endl;
                                    cout<<"================"<<endl;*/
                cout<<"Case #"<<i++<<": "<<tips<<endl;
            }
        }else{
            /*cout<<"================"<<endl;
                                    cout<<"row"<<endl;
                                    cout<<"================"<<endl;*/
            cout<<"Case #"<<i++<<": "<<tips<<endl;
        }
    }
    return 0;
}
