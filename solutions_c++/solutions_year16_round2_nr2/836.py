#include<bits/stdc++.h>
using namespace std;
int ansX,ansY;
string a,b;
void dfs(int ii,int x,int y){
    if(ii==(int)a.size()){
        if(abs(x-y)<abs(ansX-ansY)){
            ansX=x;
            ansY=y;
        }else if(abs(x-y)==abs(ansX-ansY)){
            if(x<ansX || (x==ansX && y<ansY)){
                ansX=x;
                ansY=y;
            }
        }
        return;
    }
    int nx,ny;
    if(a[ii]!='?' && b[ii]!='?'){
        nx=x*10+a[ii]-48;
        ny=y*10+b[ii]-48;
        dfs(ii+1,nx,ny);
        return;
    }else if(a[ii]=='?' && b[ii]=='?'){
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                nx=x*10+i;
                ny=y*10+j;
                dfs(ii+1,nx,ny);
            }
        }
        return;
    }else if(a[ii]=='?'){
        ny=y*10+b[ii]-48;
        for(int i=0;i<10;i++){
            nx=x*10+i;
            dfs(ii+1,nx,ny);
        }
        return;
    }else{
        nx=x*10+a[ii]-48;
        for(int i=0;i<10;i++){
            ny=y*10+i;
            dfs(ii+1,nx,ny);
        }
        return;
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>a>>b;
        ansX=1<<28,ansY=-ansX;
        dfs(0,0,0);
        cout<<"Case #"<<z<<": "<<setw(a.size())<<setfill('0')<<ansX<<" "<<setw(a.size())<<setfill('0')<<ansY<<"\n";
    }
    return 0;
}
