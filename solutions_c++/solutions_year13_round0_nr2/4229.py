#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
using namespace std;

int yard[102][102];


bool ch(int x,int y){
    bool correctanswer=true;
    int currentxa=x,currentya=y,currentxb=x,currentyb=y;
    bool contin_in1=true,contin_in2=true;
    int h = yard[x][y];
    while (correctanswer){
        if (contin_in1) {
            currentxa--;
            if (yard[currentxa][currentya]==-1) contin_in1=false;
            else if (yard[currentxa][currentya] > h) correctanswer=false;
        }
        if (contin_in2) {
            currentxb++;
            if (yard[currentxb][currentya]==-1) contin_in2=false;
            else if (yard[currentxb][currentya] > h) correctanswer=false;
        }
        if (!contin_in1 && !contin_in2) break;

    }
    if (correctanswer) return true;
    currentxa=x;currentya=y;currentxb=x;currentyb=y;contin_in1=true;contin_in2=true;correctanswer=true;
    while (correctanswer){
        if (contin_in1) {
            currentya--;
            if (yard[currentxa][currentya]==-1) contin_in1=false;
            else if (yard[currentxa][currentya] > h) correctanswer=false;
        }
        if (contin_in2) {
            currentyb++;
            if (yard[currentxa][currentyb]==-1) contin_in2=false;
            else if (yard[currentxa][currentyb] > h) correctanswer=false;
        }
        if (!contin_in1 && !contin_in2) break;

    }
    return correctanswer;
}




int main(){
    int n,x,y,css;
    bool correctanswer;
    string msg;
    scanf("%i\n",&css);
    for (int n=0;n<css;n++){
        correctanswer = true;
        for (int i=0;i<102;i++) for (int j=0;j<102;j++) yard[i][j]=-1;
        scanf("%i %i\n",&x,&y);
        for (int i=1;i<=x;i++) for (int j=1;j<=y;j++) scanf("%i",&yard[i][j]);

        for (int i=1;i<=x;i++){
            for (int j=1;j<=y;j++){
                if (!ch(i,j)) {correctanswer=false;break;}
            }
            if (!correctanswer) break;
        }

        if (correctanswer) msg="YES";
        else msg="NO";

        printf("Case #%i: %s\n",(n+1),msg.c_str());


    }


    return 0;
}
