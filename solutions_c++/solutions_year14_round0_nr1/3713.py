#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int a[5][5],b[5][5];
int ans;
int solve(int A,int B)
{
    vector<int> row1,row2;
    int i,j;
    for(i=1;i<=4;i++)
        row1.push_back(a[A][i]);
    for(i=1;i<=4;i++)
        row2.push_back(b[B][i]);
    int num = 0;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(row1[i]==row2[j]){
                ans = row1[i];
                num++;
            }
        }
    }
    return num;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ans1.txt","w",stdout);
    int T,ncase,i,j,A,B;
    cin>>T;
    ncase = 0;
    while(T--){
        ncase++;
        cin>>A;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                scanf("%d",&a[i][j]);
            }
        }
        cin>>B;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                scanf("%d",&b[i][j]);
            }
        }
        int num = solve(A,B);
        printf("Case #%d: ",ncase);
        if(num==0) cout<<"Volunteer cheated!"<<endl;
        else if(num==1) cout<<ans<<endl;
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}
