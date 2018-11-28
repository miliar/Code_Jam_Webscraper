#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int t;
    cin>>t;
    for(int f=1;f<=t;f++){
        int x, c, r;
        cin>>x>>c>>r;
        cout<<"Case #"<<f<<": ";
        if(x==1)cout<<"GABRIEL";
        else if(x==2){
            if((c*r)%2==0)cout<<"GABRIEL";
            else cout<<"RICHARD";
        }else if(x==3){
            if(c>=2&&r>=2&&(c*r)%3==0)cout<<"GABRIEL";
            else cout<<"RICHARD";
        }else{
            if(c>=3&&r>=3&&(c*r)%4==0)cout<<"GABRIEL";
            else cout<<"RICHARD";
        }
        cout<<endl;
    }
    return 0;
}
