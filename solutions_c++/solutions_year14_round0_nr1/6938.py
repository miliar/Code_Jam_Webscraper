#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, p;
    cin>>t;
    p=t;
    while(t--){
        int x, a[16]={0};
        cin>>x;
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                int q;
                cin>>q;
                if(i==x-1){
                    ++a[q-1];
                }
            }
        }
        cin>>x;
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                int q;
                cin>>q;
                if(i==x-1){
                    ++a[q-1];
                }
            }
        }
        int c=0, ans;
        for(int i=0; i<16; ++i){
            if(a[i]==2){
                ++c;
                ans=i+1;
            }
        }
        cout<<"Case #"<<p-t<<": ";
        if(c==0){
            cout<<"Volunteer cheated!\n";
        }
        if(c>1){
            cout<<"Bad magician!\n";
        }
        if(c==1){
            cout<<ans<<"\n";
        }
    }
    return 0;
}
