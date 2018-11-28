#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <memory.h>
#include <ctime>
//#include <fstream>
using namespace std;
 
using namespace std;

#define INF 1000000000
#define MP make_pair
#define FILL(a,value) memset(a,value,sizeof(a))
#define MOD 1000000009
double const PI = acos(-1.0);
double const EPS=1e-7;

int u[5][5];
int n,m;

string res[5];

bool ok(int x,int y){
    if (x<0 || y<0 || x>=n || y>=m) return false;
    return true;
}

bool ook(int x,int y){
    for (int i=-1; i<=1; i++){
        for (int j=-1; j<=1; j++){
            if (ok(x+i,y+j)){
                if (u[i+x][j+y]==1) return false;
            }
        }
    }

    return true;
}

void solve(){
	n,m;
    int k;
    cin>>n>>m>>k;

    if (k==n*m-1){
        cout<<endl;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (i==0 && j==0) cout<<'c';
                else cout<<'*';
            }
            cout<<endl;
        }
        return;
    }

    for (int mask=0; mask<(1<<(n*m)); mask++){
        int cnt=0;
        int CNT=0;

        FILL(u,0);

        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (mask&(1<<cnt)) u[i][j]=1,CNT++;
                else u[i][j]=0;
                cnt++;
            }
        }

        if (CNT!=k) continue;


        int x=-1,y=-1;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (ook(i,j)){
                    x=i;
                    y=j;
                }
            }
        }

        if (x==-1){
            continue;
        }

        
        queue<pair<int,int> > q;
        q.push(MP(x,y));
        u[x][y]=2;
        
        while(!q.empty()){
            pair<int,int> A=q.front();
            q.pop();

            int x=A.first;
            int y=A.second;

            u[x][y]=2;

            if (!ook(x,y)) continue;

            for (int i=-1; i<=1; i++){
                for (int j=-1; j<=1; j++){
                    int X=x+i;
                    int Y=y+j;
                    if (!ok(X,Y)) continue;

                    if (u[X][Y]!=0) continue;

                    u[X][Y]=3;
                    q.push(MP(X,Y));
                }
            }
        }

        bool okk=true;

        for (int i=0; i<n; i++){
            res[i]="";

            for (int j=0; j<m; j++){
                if (u[i][j]==2 || u[i][j]==3) res[i]+='.';
                else if (u[i][j]==1) res[i]+='*';
                else if (u[i][j]==0){
                    okk=false;
                }
            }
        }

        if (!okk) continue;

        res[x][y]='c';

        cout<<endl;

        for (int i=0; i<n; i++){
            cout<<res[i]<<endl;
        }

        return;

    }
    cout<<endl<<"Impossible"<<endl;
    

}

int main(){

	freopen("in.txt","r",stdin);
	freopen("OUTPUT.txt","w",stdout);

	int tt;
	cin>>tt;

	//string str;
	//getline(cin,str);

	for (int t=1; t<=tt; t++){
		cout<<"Case #"<<t<<": ";
		int time=clock();
		solve();
		cerr<<"\t\tCase #"<<t<<"\t time="<<clock()-time<<endl;
	}

}