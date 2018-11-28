#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;

int a[5][5],b[5][5],num[5];

int main(){
    int t,num1,num2,id,ans,cas=1;
   // freopen("A-small-attempt4.in","r",stdin);
    //freopen("A-small-attempt4.txt","w",stdout);
    cin>>t;
    while(t--){
        id=0;
        cin>>num1;
        num1--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        cin>>num2;
        num2--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        memset(num,0,sizeof(num));
        for(int k=0;k<4;k++){
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(a[num1][k]==b[i][j]){
                        num[i]++;
                        if(num2==i) ans=b[i][j];
                    }
                }
            }
        }
        if(num[num2]==1) printf("Case #%d: %d\n",cas++,ans);
        else if(num[num2]==0){
            printf("Case #%d: ",cas++);
            cout<<"Volunteer cheated!"<<endl;
        }
        else {
            printf("Case #%d: ",cas++);
            cout<<"Bad magician!"<<endl;
        }
    }
}
