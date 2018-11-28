#include<iostream>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<stdio.h>
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
using namespace std;
int CC[30];
int NN[30];
char ch[50000];
void go(char c,int num){
    CC[c-'A']-=num;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    cin>>T;
    rep(t,1,T){
        memset(CC,0,sizeof(CC));
        memset(NN,0,sizeof(NN));
        scanf("%s",ch+1);
        printf("Case #%d: ",t);
        int l = strlen(ch+1);
        rep(i,1,l){
            CC[ch[i]-'A']++;
        }
        NN[0] = CC['Z'-'A'];
        go('Z',NN[0]);go('E',NN[0]);go('R',NN[0]);go('O',NN[0]);

        NN[2] = CC['W'-'A'];
        go('T',NN[2]);go('W',NN[2]);go('O',NN[2]);

        NN[6] = CC['X'-'A'];
        go('S',NN[6]);go('I',NN[6]);go('X',NN[6]);

        NN[8] = CC['G'-'A'];
        go('E',NN[8]);go('I',NN[8]);go('G',NN[8]);go('H',NN[8]);go('T',NN[8]);

        NN[4] = CC['U'-'A'];
        go('F',NN[4]);
        go('O',NN[4]);
        go('U',NN[4]);
        go('R',NN[4]);

        NN[5] = CC['F'-'A'];
        go('F',NN[5]);
        go('I',NN[5]);
        go('V',NN[5]);
        go('E',NN[5]);

        NN[1] = CC['O'-'A'];
        go('O',NN[1]);
        go('N',NN[1]);
        go('E',NN[1]);

        NN[3] = CC['T'-'A'];
        go('T',NN[3]);
        go('H',NN[3]);
        go('R',NN[3]);
        go('E',NN[3]);
        go('E',NN[3]);

        NN[7] = CC['S'-'A'];
        go('S',NN[7]);
        go('E',NN[7]);
        go('V',NN[7]);
        go('E',NN[7]);
        go('N',NN[7]);

        NN[9] = CC['I'-'A'];
        go('N',NN[9]);
        go('I',NN[9]);
        go('N',NN[9]);
        go('E',NN[9]);

        rep(i,0,9){
            rep(j,1,NN[i])
                printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
