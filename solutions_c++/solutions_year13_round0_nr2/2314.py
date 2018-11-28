#include<iostream>
#include<cstring>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
using namespace std;
int main(){
    
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    
    int tc;
    cin>>tc;
    
    for(int caso=1;caso<=tc;caso++){
        int R,C;
        cin>>R>>C;
        
        int c[R][C];
        int maxi=-1;
        
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++){
                cin>>c[i][j];
                maxi=max(maxi,c[i][j]);
            }
        
        bool visited[R][C];
        memset(visited,0,sizeof(visited));
        
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                if(c[i][j]==maxi)
                    visited[i][j]=1;
        
        
        bool yes=0;
        
        while(true){
            
            bool fin=1;
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++)
                    if(!visited[i][j])fin=0;
            
            if(fin){
                yes=1;
                break;
            }
        
            int mini=1<<30;
            int x=-1,y=-1;
            
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++){
                    if(visited[i][j])continue;
                    if(c[i][j]<mini){
                        mini=c[i][j];
                        x=i;y=j;
                    }
                }
            
            bool columna=1;
            bool fila=1;
            
            for(int i=0;i<C;i++)
                if(c[x][i]!=mini)
                    columna=0;
            
            for(int i=0;i<R;i++)
                if(c[i][y]!=mini)
                    fila=0;
            
            
            if(columna)for(int i=0;i<C;i++)visited[x][i]=1;
            if(fila)for(int i=0;i<R;i++)visited[i][y]=1;
            if(columna==0 && fila==0)break;
            
        }
        
        
        cout<<"Case #"<<caso<<": ";        
        if(yes)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    
    return 0;
}
