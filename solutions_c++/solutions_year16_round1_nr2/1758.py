#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int n,x,a[2505];
        memset(a,0,sizeof(a));
        cin>>n;
        for(int i=1;i<2*n;i++){
            for(int j=1;j<=n;j++){
                cin>>x;
                a[x]++;
            }
        }

        printf("Case #%d: ",t);
        for(int i=1;i<=2500;i++){
            if(a[i]%2 == 1){
                cout<<i<<' ';
            }
        }
        cout<<endl;

    }
    return 0;
}
