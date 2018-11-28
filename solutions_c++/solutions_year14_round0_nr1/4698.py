#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
int n,m;
int ans,t;
int a[5][5],b[5][5];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int tt=1;tt<=T;tt++){
        cin>>n;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                cin>>a[i][j];
        cin>>m;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                cin>>b[i][j];
        ans=0;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                if (a[n][i]==b[m][j]){
                    ans++;
                    t=a[n][i];
                }
        //cout<<ans<<' '<<t<<endl;
        printf("Case #%d: ",tt);
        if (ans==1) printf("%d\n",t);
        if (ans>1) printf("Bad magician!\n");
        if (ans==0) printf("Volunteer cheated!\n");
    }
}
