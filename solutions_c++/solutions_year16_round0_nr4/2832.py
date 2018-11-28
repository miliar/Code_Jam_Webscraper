#include <bits/stdc++.h>
using namespace std;
int stu[101];
int ans[101][1000];

void genarate()
{
    ans[1][0]=1;
    stu[1]=1;
    ans[2][0]=2;
    stu[2]=1;
    ans[3][0]=2;
    ans[3][1]=6;
    stu[3]=2;
    for(int i=4;i<=100;i++){
        int tmp=2;
        stu[i]=ceil(i/2.0);
        for(int j=0;j<ceil(i/2.0);j++){
            ans[i][j]=tmp;
            if(tmp+(i+1)*2<=i*i) tmp+=(i+1)*2;
            else tmp+=i+1;
        }
    }
}

int main()
{
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    genarate();
    for(int cs=1;cs<=t;cs++){
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",cs);
        if(c==1&&s>=k){
            for(int i=1;i<=k;i++) printf(" %d",i);
        }
        else if(c==1&&s<k) printf(" IMPOSSIBLE",cs);
        else if(c>1&&stu[k]<=s){
            for(int i=0;i<stu[k];i++){
                printf(" %d",ans[k][i]);
            }
        }
        else printf(" IMPOSSIBLE",cs);
        cout<<"\n";
    }
    return 0;
}
