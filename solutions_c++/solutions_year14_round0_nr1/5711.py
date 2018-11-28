#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#define N 17
#include<fstream>
using namespace std;
int r1[N],r2[N];

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int ans,t,flag,x1,x2,i,j,y,ics=0;
    cin>>t;
    while(t--){
        cin>>x1;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>y;
                r1[y]=i;
            }
        }
        cin>>x2;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>y;
                r2[y]=i;
            }
        }
        flag=0;
        for(i=1;i<=16;i++){
            if(r1[i]==x1&&r2[i]==x2){
                if(!flag){
                    flag=1;
                    ans=i;
                }else {
                    flag=2;
                    break;
                }
            }
        }
        printf("Case #%d: ",++ics);
        if(!flag){
            cout<<"Volunteer cheated!"<<endl;
        }else if(flag==2){
            cout<<"Bad magician!"<<endl;
        }else {
            cout<<ans<<endl;
        }
    }
    return 0;
}
