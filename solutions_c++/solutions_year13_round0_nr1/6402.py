#include <iostream>
#include <cstdio>
using namespace std;
int cnt;
char s[4][5];
void solve(){
    int  o=0,x=0,t=0,ct=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(s[i][j]=='O')o++;
            if(s[i][j]=='X')x++;
            if(s[i][j]=='T')t++;
        }
        if(o==4||(o==3&&t==1)){
            cout<<"Case #"<<++cnt<<": O won"<<endl;
            return ;
        }
        if(x==4||(x==3&&t==1)){
            cout<<"Case #"<<++cnt<<": X won"<<endl;
            return ;
        }
        o=0,x=0,t=0;
    }
    o=0,x=0,t=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(s[j][i]=='O')o++;
            if(s[j][i]=='X')x++;
            if(s[j][i]=='T')t++;
        }
        if(o==4||(o==3&&t==1)){
            cout<<"Case #"<<++cnt<<": O won"<<endl;
            return ;
        }
        if(x==4||(x==3&&t==1)){
            cout<<"Case #"<<++cnt<<": X won"<<endl;
            return ;
        }
        o=0,x=0,t=0;
    }
    o=0,x=0,t=0;
    for(int i=0;i<4;i++){
        if(s[i][i]=='O')o++;
        if(s[i][i]=='X')x++;
        if(s[i][i]=='T')t++;
    }
    if(o==4||(o==3&&t==1)){
        cout<<"Case #"<<++cnt<<": O won"<<endl;
        return ;
    }
    if(x==4||(x==3&&t==1)){
        cout<<"Case #"<<++cnt<<": X won"<<endl;
        return ;
    }
    o=0,x=0,t=0;
    for(int i=0;i<4;i++){
        if(s[i][3-i]=='O')o++;
        if(s[i][3-i]=='X')x++;
        if(s[i][3-i]=='T')t++;
    }
    if(o==4||(o==3&&t==1)){
        cout<<"Case #"<<++cnt<<": O won"<<endl;
        return ;
    }
    if(x==4||(x==3&&t==1)){
        cout<<"Case #"<<++cnt<<": X won"<<endl;
        return ;
    }
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(s[i][j]=='.')ct++;
        }
    }
    if(ct)cout<<"Case #"<<++cnt<<": Game has not completed"<<endl;
    else cout<<"Case #"<<++cnt<<": Draw"<<endl;
    return ;
}

int main() {
    int num;
    cin>>num;
    while(num--){
        for(int i=0;i<4;i++)scanf("%s\n",s[i]);
        solve();
    }    	
	return 0;
}