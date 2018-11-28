#include<cstdio>
#include<cstdlib>
using namespace std;
int arr1[4][4],arr2[4][4];
int func1(int r1,int r2){
    r1--,r2--;
    int a[17]={0};
    for(int i=0;i<4;i++)
        a[arr1[r1][i]-1]++;
    for(int i=0;i<4;i++)
        a[arr2[r2][i]-1]++;
    int cnt=0,ans=0;
    for(int i=0;i<16;i++)
        if(a[i]==2) {cnt++;ans=i+1;}
    if(cnt==1) return ans;
    if(cnt>1) return -1;
    return -2;
}
int main(){
    int t,r1,r2,x;
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&arr1[i][j]);

        scanf("%d",&r2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&arr2[i][j]);
        printf("Case #%d: ",c);
        x=func1(r1,r2);
        if(x>0) printf("%d\n",x);
        else if(x==-1) printf("%s\n","Bad magician!");
        else printf("%s\n","Volunteer cheated!");
    }
    return 0;
}
