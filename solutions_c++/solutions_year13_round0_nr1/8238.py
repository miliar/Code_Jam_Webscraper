#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include<map>
#include <list>
#include <queue>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <sstream>
using namespace std;

int main(){
    //freopen("C:\\Users\\LAPTOPS\\Desktop\\bb.txt","r",stdin);
    //freopen("C:\\Users\\LAPTOPS\\Desktop\\chut.txt","w",stdout);
char a[4][4];
int t,cx,co,ct,cd,k;
cin>>t;
for(int p=1;p<=t;p++){
for(int i=0;i<=3;i++)
for(int j=0;j<=3;j++) {cin>>a[i][j];
}

cd=k=0;
for(int i=0;i<=3;i++){ co=cx=ct=0;
for(int j=0;j<=3;j++){ if(a[i][j]=='X') cx++;
else if(a[i][j]=='O') co++;
else if(a[i][j]=='T') ct=1;
else if(a[i][j]=='.') cd++;
}
if(cx+ct==4) { k=1;cout<<"Case #"<<p<<": X won\n";break;}
else if(co+ct==4) { k=1;cout<<"Case #"<<p<<": O won\n";break;}
}
if(!k){
      
for(int i=0;i<=3;i++){  co=cx=ct=0;
for(int j=0;j<=3;j++){if(a[j][i]=='X') cx++;
else if(a[j][i]=='O') co++;
else if(a[i][j]=='T') ct=1;
else if(a[i][j]=='.')cd++;
}
if(cx+ct==4) { k=1;cout<<"Case #"<<p<<": X won\n";break;}
else if(co+ct==4) { k=1;cout<<"Case #"<<p<<": O won\n";break;}

}
} 
if(!k){co=cx=ct=0;
for(int i=0;i<=3;i++){
        if(a[i][i]=='X') cx++;
else if(a[i][i]=='O') co++;
else if(a[i][i]=='T') ct=1;
else if(a[i][i]=='.')cd++;
}
if(cx+ct==4) { k=1;cout<<"Case #"<<p<<": X won\n";}
else if(co+ct==4) { k=1;cout<<"Case #"<<p<<": O won\n";}

}
if(!k){co=cx=ct=0;
for(int i=0;i<=3;i++){ //cout<<a[i][3-i];
        if(a[i][3-i]=='X') cx++;
else if(a[i][3-i]=='O') co++;
else if(a[i][3-i]=='T') ct=1;
else if(a[i][3-i]=='.')cd++;
} 
if(cx+ct==4) { k=1;cout<<"Case #"<<p<<": X won\n";}
else if(co+ct==4) { k=1;cout<<"Case #"<<p<<": O won\n";}

}
   //cout<<k;     
if(k==0 && cd>0) cout<<"Case #"<<p<<": Game has not completed\n";
else if(k==0 && cd==0) cout<<"Case #"<<p<<": Draw\n";
//cout<<p<<endl;
}
//system("pause");
}
