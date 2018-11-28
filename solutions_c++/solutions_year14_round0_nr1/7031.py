#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    freopen("inA.txt","r",stdin);
    freopen("ouA.txt","w",stdout);
    int t,r1,r2;
    cin>>t;
    int count1 ,a[5][5],b[5][5],x;
    for(int k=1;k<=t;k++) {
        cin>>r1;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>a[i][j];
            }
        }
        cin>>r2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>b[i][j];
            }
        }
        count1=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[r1-1][i]==b[r2-1][j]){
                    count1++;
                    if(count1==1)
                        x=a[r1-1][i];
                }
            }
        }
        if(count1==1)
            cout<<"Case #"<<k<<": "<<x<<endl;
        else if(count1==0)
            cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else cout<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    return 0;
}
