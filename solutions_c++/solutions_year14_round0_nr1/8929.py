#include <iostream>

using namespace std;

int main() {
    int T=0;
    cin>>T;
    for(int j=1; j<=T; j++) {
        int r1, r2, c1, c2, c3, c4, t, count=0, ans=0;
        bool arr[16] = {0};
        cin>>r1;
        c1 = (r1-1)*4;
        c2 = 12 - c1;
        while(c1-->0) cin>>t;
        for(int i=0;i<4;i++) { cin>>t; arr[t-1]=true; }
        while(c2-->0) cin>>t;
        cin>>r2;
        c3 = (r2-1)*4;
        c4 = 12 - c3;
        while(c3-->0) cin>>t;
        for(int i=0;i<4;i++) {
            cin>>t;
            if(arr[t-1]) {
                ans = t;
                count++;
            }
        }
        while(c4-->0) cin>>t;
        if(count==1)
            printf("Case #%d: %d\n",j,ans);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",j);
        else
            printf("Case #%d: Bad magician!\n",j);
    }
}
