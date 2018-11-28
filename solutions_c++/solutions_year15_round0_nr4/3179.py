#include<iostream>
#include<stdio.h>
using namespace std;
char tab[2][10]={"GABRIEL","RICHARD"};
void wys(char c,int i){
if(c=='g')printf("Case #%d: %s\n",i,tab[0]);
else printf("Case #%d: %s\n",i,tab[1]);

}
int main(){
    int t,x,r,c,tmp;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>x>>r>>c;
        if(r>c){tmp=c;c=r;r=tmp;}//r<c r jest mniejszy
        if((r*c)%x!=0){wys('r',i);continue;}
        if(r==3&&c==4){wys('g',i);continue;}
        if(r==4&&c==4&&x==3){wys('r',i);continue;}
        if(r==2&&c==4&&(x==3||x==4)){wys('r',i);continue;}
        if(r==3&&c==3&&(x==2||x==4)){wys('r',i);continue;}
        if(r==2&&c==3&&x==4){wys('r',i);continue;}
        if(r==2&&c==2&&(x==3||x==4)){wys('r',i);continue;}
        if(r==1&&c==2&&(x==3||x==4)){wys('r',i);continue;}
        if(r==1&&c==3&&(x!=1)){wys('r',i);continue;}
        if(r==3&&c==3&&(x==2||x==4)){wys('r',i);continue;}
        if(r==1&&c==4&&(x==4||x==3)){wys('r',i);continue;}
        if(r==4&&c==4&&(x==3)){wys('r',i);continue;}
        wys('g',i);


    }

}

