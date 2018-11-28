#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int Mat[100][100];
bool coordinate(int ,int,int ,int);
bool check(int,int);

int main(){
    int num;
    //freopen("in","r",stdin);
    scanf("%d",&num);
    getchar();
    
    for(int k=1;k!=num+1;k++){
        int m,n;
        scanf("%d %d",&m,&n);
        getchar();

        for(int i=0;i!=m;i++){
            
            for(int j=0;j!=n;j++)
                scanf("%d",&Mat[i][j]);
            getchar();
        }
        if(check(m,n))
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);
       
    }
}

bool coordinate(int i,int j,int m,int n){
    int  val = Mat[i][j];
    bool pi  = true,pj=true;
    
    for(int k=0;k!=m;k++)
        if(Mat[k][j]>val){
            pi = false;
            break;
        }
    
    for(int k=0;k!=n;k++)
        if(Mat[i][k]>val){
            pj = false;
            break;
        }
    return (pi || pj);
}


bool check(int m,int n){
    bool mv[100];
    bool nv[100];

    
    for(int i=0;i!=m;i++){
        for(int j=0;j!=n;j++){
            if(!coordinate(i,j,m,n))
                return false;
        }
    }
    return true;
}


            
        
    
