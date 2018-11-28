#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

int a[120][120],b[120][120];
int R,C;
bool flag;
bool change=true;
void solveH(int x){
    set<int> st; st.insert(100);
    for(int i=0; i<C; i++)
        st.insert(a[x][i]);
    if(st.size()==1){}
    else if(st.size()==2){
        change = true;
        int t = *st.begin();
        for(int i=0; i<C; i++){
            if(a[x][i]==100 && b[x][i]>t){
                flag = false;
            }
            a[x][i]=100;
        }
    }
}

void solveV(int x){
    set<int> st; st.insert(100);
    for(int i=0; i<R; i++)
        st.insert(a[i][x]);
    if(st.size()==1){}
    else if(st.size()==2){
        change=true;
        int t = *st.begin();
        for(int i=0; i<R; i++){
            if(a[i][x]==100 && b[i][x]>t){
                flag = false;
            }
            a[i][x]=100;
        }
    }
}
bool check(){
    for(int i=0; i<R; i++)
    for(int j=0; j<C; j++){
        if(a[i][j]!=100) return false;
    }
    return true;
}
void solve(int test){
    printf("Case #%d: ",test+1);
    flag=true;
    change=true;
    while(change){
        change=false;
        for(int i=0; i<R; i++) solveH(i);
        /*for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                printf("%d ",a[i][j]);
            }
            printf("\n");
        }
        printf("\n");*/
        for(int i=0; i<C; i++) solveV(i);
        /*for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                printf("%d ",a[i][j]);
            }
            printf("\n");
        }
        printf("\n");*/
    }

    if(flag && check()){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
}
int ntest;
int main(){
    freopen("B-small-attempt3.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&ntest);
    for(int t=0; t<ntest; t++){
        scanf("%d %d",&R,&C);
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                scanf("%d",&a[i][j]);
                b[i][j]=a[i][j];
            }
        }
        solve(t);
    }
    return 0;
}
