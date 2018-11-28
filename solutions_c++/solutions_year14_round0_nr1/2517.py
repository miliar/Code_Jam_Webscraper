#include<cstdio>
#include<vector>

using namespace std;

#define N 4
int c1[N][N];
int c2[N][N];
int t,m,n;

int main(){
    scanf("%d",&t);
    int cas=1;
    while(t--){
        scanf("%d",&m);
        int i,j;
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)scanf("%d",c1[i]+j);
        scanf("%d",&n);
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)scanf("%d",c2[i]+j);
        vector<int> ret;
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)if(c1[m-1][i]==c2[n-1][j])ret.push_back(c1[m-1][i]);
        printf("Case #%d: ",cas++);
        if(ret.size()==1)printf("%d",ret[0]);
        if(ret.size()>1)printf("Bad magician!");
        if(ret.size()==0)printf("Volunteer cheated!");
        printf("\n");
    }
    return 0;
}

