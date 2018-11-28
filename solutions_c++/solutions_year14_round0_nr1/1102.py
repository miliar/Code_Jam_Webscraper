#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
using namespace std;
int _used[20];
int A[4][4];
void solve(int _case){
    memset(_used,0,sizeof(_used));

    int z;
    scanf("%d",&z);
    z--;
    for(int i = 0 ; i < 4 ; ++ i){
        for(int j = 0 ; j < 4 ; ++ j ){
            scanf("%d",&A[i][j]);
            if(i==z)_used[A[i][j]]++;
        }
    }
    scanf("%d",&z);
    z--;
    int answ=0;
    int ans;
    for(int i = 0 ; i < 4 ; ++ i){
        for(int j = 0 ; j < 4 ; ++ j ){
            scanf("%d",&A[i][j]);
            if(i==z){
                _used[A[i][j]]++;
                if(_used[A[i][j]]==2){
                    answ++;
                    ans=A[i][j];
                }
            }
        }
    }
    string answer="";
    if(answ>1)printf("Case #%d: Bad magician!\n", _case);
    else if(answ==0)printf("Case #%d: Volunteer cheated!\n", _case);
    else printf("Case #%d: %d\n", _case, ans);

}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){

        solve(i);
    }
}
