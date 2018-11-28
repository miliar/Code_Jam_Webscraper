#include <cstdio>
#include <cstring>
#include <vector>

#define MAX 20

using namespace std;

int T,x,aux;
int v[MAX];
vector<int> vetor;

int main(){

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);


    scanf("%d",&T);

    for(int caso=1;caso<=T;caso++){
        printf("Case #%d: ",caso);
        vetor.clear();
        scanf("%d",&x);
        memset(v,0,sizeof v);
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&aux);
                if(i!=x) continue;
                v[aux]++;
            }
        }

        scanf("%d",&x);

        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&aux);
                if(i!=x) continue;
                v[aux]++;
            }
        }

        for(int i=1;i<=16;i++){
            if(v[i] == 2) vetor.push_back(i);
        }

        if(vetor.size() == 0) printf("Volunteer cheated!\n");
        else if(vetor.size() == 1) printf("%d\n",vetor[0]);
        else printf("Bad magician!\n");

    }

    return 0;
}
