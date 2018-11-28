#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("ans1.txt","w",stdout);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<h<<": ";
        if(c==1){
            if(s<k)
                cout<<"IMPOSSIBLE"<<endl;
             else{
                for(int i=1;i<=k;i++)
                    cout<<i<<" ";
                cout<<endl;
             }
        }
        else{
             if(s<k/2){
                cout<<"IMPOSSIBLE"<<endl;
            }
            else{
                long long int temp=1;
                for(int i=1;i<c;i++){
                    temp*=k;
                }
                for(int i=1;i<k;i+=2)
                    cout<<i*temp+i<<" ";
                if(k%2==1)
                    cout<<k;
                cout<<endl;
            }
        }
    }
    return 0;
}
