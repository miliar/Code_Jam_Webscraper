#include <iostream>
#include <string>
#include <queue>
using namespace std;

#define MAX 101
typedef pair<int,int> PII;

int a[MAX][MAX],c[MAX][MAX];

int main(){
    int t,u,n,m,i,j,n1,m1,flags[101];
    string str;
    cin>>t;
    for (u=0; u<t; u++){
        priority_queue<PII,vector<PII>,greater<PII> > q;
        cout<<"Case #"<<(u+1)<<": ";
        cin>>n>>m;
        n1=n; m1=m;
        for (i=0; i<n; i++) for (j=0; j<m; j++) c[i][j]=0;
        for (i=0; i<n; i++) for (j=0; j<m; j++) cin>>a[i][j];
        for (i=0; i<n; i++){
            for (j=1; j<=100; j++) flags[j]=0;
            for (j=0; j<m; j++) flags[a[i][j]]++;
            for (j=1; j<=100; j++) if (flags[j]) q.push(make_pair(j,i+1));
        }            
        for (i=0; i<m; i++){
            for (j=1; j<=100; j++) flags[j]=0;
            for (j=0; j<n; j++) flags[a[j][i]]++;
            for (j=1; j<=100; j++) if (flags[j]) q.push(make_pair(j,-(i+1)));
        }            
        while(!q.empty()){
            PII dr=q.top(); q.pop();
            int x=dr.first, b=dr.second;
            if (b>0){
                i=b-1;
                for (j=0; j<m; j++) if (a[i][j]>x || (a[i][j]<x && c[i][j]==0)) break;
                if (j==m) for (j=0; j<m; j++) c[i][j]=1;
            }
            else{
                j=(-b)-1;
                for (i=0; i<n; i++) if (a[i][j]>x || (a[i][j]<x && c[i][j]==0)) break;
                if (i==n) for (i=0; i<n; i++) c[i][j]=1;
            }
        }
        for (i=0; i<n; i++){
            for (j=0; j<m; j++) if (c[i][j]==0) break;
            if (j<m) break;
        }
        if (i==n) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
