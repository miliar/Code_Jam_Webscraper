#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,k,x,y,dir,res,r,c,cases,t;
    cin>>cases;
    for(t=1;t<=cases;t++){
        string s[102];
        queue< pair<int, int> > posiciones;
        bool imp,inun[102][102];
        memset(inun, 0, sizeof inun);
        cin>>r>>c;
        for(i=0;i<r;i++){
            cin>>s[i];
        }
        cout<<"Case #"<<t<<": ";
        imp=false;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(s[i][j]!='.'){
                    imp=true;
                    for(k=0;k<i;k++){
                        if(s[k][j]!='.')imp=false;
                    }
                    for(k=i+1;k<r;k++){
                        if(s[k][j]!='.')imp=false;
                    }
                    for(k=0;k<j;k++){
                        if(s[i][k]!='.')imp=false;
                    }
                    for(k=j+1;k<c;k++){
                        if(s[i][k]!='.')imp=false;
                    }
                    if(imp){
                        break;
                    }
                }
            }
            if(imp){
                break;
            }
        }
        if(imp){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            res=0;
            for(i=0;i<r;i++){
                for(j=0;j<c;j++){
                    if(s[i][j]!='.'&&!inun[i][j]){
                        x=i;
                        y=j;
                        while(true){
                            inun[x][y] = 1;
                            if(s[x][y]=='^'){
                                dir=1;
                            }
                            if(s[x][y]=='>'){
                                dir=2;
                            }
                            if(s[x][y]=='v'){
                                dir=3;
                            }
                            if(s[x][y]=='<'){
                                dir=4;
                            }
                            if(dir==1){
                                x--;
                            }
                            if(dir==2){
                                y++;
                            }
                            if(dir==3){
                                x++;
                            }
                            if(dir==4){
                                y--;
                            }
                            if(x>=r||x<0||y<0||y>=c){
                                res++;
                                break;
                            }
                            if(inun[x][y]&&s[x][y]!='.'){
                                break;
                            }
                        }
                    }
                }
            }
            cout<<res<<endl;
        }
    }
}
