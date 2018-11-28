#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int t,n,m;
int a[5][5],b[5][5];
int flag[10];
int main() {
   // freopen("A-small-attempt0.in", "r" , stdin);
   // freopen("output.txt" , "w" , stdout);
    while(cin>>t) {
        int tcase=0;
        while(t--) {
            memset(a,0,sizeof(a));
            memset(b,0,sizeof(b));
            cin>>n;
            for(int i=0; i<4; i++) {
                for(int j=0; j<4; j++) {
                    cin>>a[i][j];
                }
            }
            cin>>m;
            for(int i=0; i<4; i++) {
                for(int j=0; j<4; j++) {
                    cin>>b[i][j];
                }
            }
            int sum=0;
            int ans;
            for(int j=0; j<4; j++)
                for(int i=0; i<4; i++) {
                    if(b[m-1][j]==a[n-1][i]) {
                        ans=a[n-1][i];
                        sum++;
                    }
                }
            printf("Case #%d: ",++tcase);
            if(sum==1) {
                cout<<ans<<endl;
            } else if(sum>1) {
                cout<<"Bad magician!"<<endl;
            } else {
                cout<<"Volunteer cheated!"<<endl;
            }
        }
    }
    return 0;
}
