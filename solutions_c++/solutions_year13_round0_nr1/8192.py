/***************************************************************************
 *
 * Copyright (c) 2013 Baidu.com, Inc. All Rights Reserved
 *
 **************************************************************************/



/**
 * @file gcj1.cpp
 * @author maoyouxiang(com@baidu.com)
 * @date 2013/04/14 00:55:53
 * @brief
 *
 **/
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

char str[10][10];
char str1[10][10];



int judge(char str[][10]) {
    char fuck;
    int j;
    for (int i=0;i<4;i++) {
      if(str[i][0]=='.')continue;
      fuck=str[i][0];
      for(j=0;j<4;j++) {
        if(str[i][j]!=fuck)break;
      }
      if(j==4) return fuck=='X'?1:2;
      if(str[0][i]=='.')continue;
      fuck=str[0][i];
      for(j=0;j<4;j++) {
        if(str[j][i]!=fuck)break;
      }
      if(j==4) return fuck=='X'?1:2;
    }
    if(str[0][0]!='.') {
        for(j=0;j<4;j++) {
            if(str[j][j]!=str[0][0])break;
        }
        if(j==4) return fuck=='X'?1:2;

    }
    if(str[0][3]!='.') {
        for(j=0;j<4;j++) {
            if(str[j][3-j]!=str[0][3])break;
        }
        if(j==4) return fuck=='X'?1:2;

    }
    return -1;













}

int main() {
    freopen("A-small-attempt3.in","r",stdin);
    freopen("data.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int t=1;t<=cas;t++) {
        for(int i=0;i<4;i++) {
            scanf("%s",str[i]);
        }
        char tmp=getchar();
        bool empty=false;
        memcpy(str1,str,sizeof(str));
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(str[i][j]=='T'){
                    str[i][j]='X';
                    str1[i][j]='O';
                } else if(str[i][j]=='.'){
                    empty=true;
                }
            }
        }
        int flag=judge(str);
        //printf("11111111---->%d\n",flag);
        printf("Case #%d: ",t);
        if(flag==1) {
          printf("X won\n");
        } else if(flag==2) {
          printf("O won\n");
        } else {
          flag=judge(str1);
          if(flag==2) {
             printf("O won\n");
          } else if(empty) {
             printf("Game has not completed\n");
          } else {
             printf("Draw\n");
          }
        }
    }
    return 0;
}






















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
