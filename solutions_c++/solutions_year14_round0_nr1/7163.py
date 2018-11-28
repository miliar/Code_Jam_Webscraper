#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,x,w[10];
        vector<int> u,v;
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++){
            scanf("%d",&x);
            if(i==n) u.push_back(x);
        }
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++){
            scanf("%d",&x);
            if(i==n) v.push_back(x);
        }
        sort(u.begin(),u.end());
        sort(v.begin(),v.end());
        n=set_intersection(u.begin(),u.end(),v.begin(),v.end(),w)-w;
        printf("Case #%d: ",++no);
        if(!n){
            puts("Volunteer cheated!");
        }else if(n>1){
            puts("Bad magician!");
        }else{
            printf("%d\n",w[0]);
        }
    }
}
