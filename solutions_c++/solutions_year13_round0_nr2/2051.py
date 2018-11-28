#include<cstdio>
#include<vector>
#include<set>

#define DEBUG printf
using namespace std;

bool canDo(vector<vector<int> > &v){
    int r,c,i,j;
    r = v.size();
    c = v[0].size();
    vector<int> v1(c,100);
    vector<vector<int> > v2(r,v1);

        for(i=0;i<r;i++){
            int mx = v[i][0];
            for(j=1;j<c;j++){
                if(v[i][j]>mx)
                    mx = v[i][j];

            }
            for(j=0;j<c;j++)
                v2[i][j] = min(v2[i][j],mx);

        }
        for(i=0;i<c;i++){
            int mx = v[0][i];
            for(j=1;j<r;j++){
                if(v[j][i]>mx)
                    mx = v[j][i];

            }
            for(j=0;j<r;j++)
                v2[j][i] = min(v2[j][i],mx);

        }




    /*for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            if(v[i][j]!=v2[i][j]){
                DEBUG("%d %d\n",i,j);
                return false;
            }

        }

    }
    return true;
    */
    return v2==v;

}

int main(){
    int T,tc=1;
    scanf("%d\n",&T);
    while(tc <= T){
        int r,c;
        scanf("%d %d\n",&r,&c);
        vector<int> v1(c,0);
        vector<vector<int> > v2(r,v1);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                scanf("%d",&v2[i][j]);

            }
            scanf("\n");
        }
        if(canDo(v2)){
            printf("Case #%d: YES\n",tc);
        }
        else{
            printf("Case #%d: NO\n",tc);

        }
        tc++;
    }

    return 0;
}
