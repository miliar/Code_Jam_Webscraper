#include <iostream>
#include <cstdio>
#include<cmath>

using namespace std;

int main()
{   freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    cin>>t;
    for(int t1=0;t1<t;t1++){
            int x,y,a[4][4],b[4][4],count1=0,ans;
            scanf("%d",&x);
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    cin>>a[i][j];
                }
            }
            scanf("%d",&y);
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    cin>>b[i][j];
                }
            }
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(a[x-1][i]==b[y-1][j]){
                        count1++;
                        ans = a[x-1][i];
                    }
                }
            }
            if(count1==0)
                cout<<"Case #"<<t1+1<<": "<<"Volunteer cheated!"<<endl;
            else if(count1>1)
                cout<<"Case #"<<t1+1<<": "<<"Bad magician!"<<endl;
            else
                cout<<"Case #"<<t1+1<<": "<<ans<<endl;
    }
    return 0;
}
