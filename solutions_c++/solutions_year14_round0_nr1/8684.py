/// Allah, enlarge my knowledge, as I can enlighten your creation.
/*Minhaz Ahmed Syrus (msyrus)*/
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)

int main(){
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);
    int T, N, tmp, cnt,res;
    scanf(" %d",&T);
    for(int cas=0; cas<T; ){
        res=cnt=0;
        set <int> S;
        scanf(" %d",&N);
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                scanf(" %d",&tmp);
                if(i==N){
                    S.insert(tmp);
                }
            }
        }

        scanf(" %d",&N);
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                scanf(" %d",&tmp);
                if(i==N){
                    int x=(S.count(tmp)>0)?1:0;
                    if(cnt==0 && x==1)res=tmp;
                    cnt+=x;
                }
            }
        }
        cout<<"Case #"<<++cas<<": ";
        if(cnt==1){
            cout<<res<<"\n";
        }else if(cnt>1){
            cout<<"Bad magician!\n";
        }
        else if(cnt==0){
            cout<<"Volunteer cheated!\n";
        }
    }
    return 0;
}
