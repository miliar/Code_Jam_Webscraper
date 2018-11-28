//#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream cin("1.in");
ofstream cout("1.out");

struct Cnum{
    int x,y;
    int num;
    Cnum(){}
    Cnum(int tx,int ty,int tn){
        x=tx,y=ty,num=tn;
    }
};

int tot;
int n,m;
int map[111][111];
int col[111],row[111];
Cnum v[11111];

bool Cmp(Cnum a,Cnum b){
    return a.num>b.num;
}

bool Can(){
    sort(v,v+tot,Cmp);
    for(int i=0;i!=n;i++) row[i]=0;
    for(int i=0;i!=m;i++) col[i]=0;
    for(int i=0;i!=n*m;i++){
        if (v[i].num<row[v[i].x]&&v[i].num<col[v[i].y]) return false;
        if (v[i].num>=row[v[i].x]) row[v[i].x]=v[i].num;
        if (v[i].num>=col[v[i].y]) col[v[i].y]=v[i].num;
    }
    return true;
}

int main(){
    int t;
    cin>>t;
    for(int q=1;q!=t+1;q++){
        cout<<"Case #"<<q<<": ";
        cin>>n>>m;
        tot=0;
        for(int i=0;i!=n;i++)
            for(int j=0;j!=m;j++){
                cin>>map[i][j];
                v[tot++]=Cnum(i,j,map[i][j]);
            }
        if (Can()) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}
