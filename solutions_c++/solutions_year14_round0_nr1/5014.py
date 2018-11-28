#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

int A[10][10],B[10][10];
int a,b,T;


int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);    
    int cs=0;
    long long N,S;
    while(T--){
        cin>>a;
        for (int i=1;i<=4;i++) for(int j=1;j<=4;j++) cin>>A[i][j];
        cin>>b;
        for (int i=1;i<=4;i++) for(int j=1;j<=4;j++) cin>>B[i][j];

        int cnt=0,ans=0;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        if(A[a][i]==B[b][j])
        {
            cnt++;
            ans=A[a][i];
        }

        cout<<"Case #"<<++cs<<": ";
        if (cnt==1) cout<<ans<<endl;
        else if (cnt) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
} 