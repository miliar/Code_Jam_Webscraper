#include <bits/stdc++.h>

using namespace std;
int vis[10];
bool allvis(){
    bool b=true;
    for(int i=0; i<10; i++)
        b = b&&vis[i];
    return b;
}
void go(int x){

    while(x){
        vis[x%10] = 1;
        x/=10;
    }
}
int main()
{

    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int f=1; f<=t; f++){
        memset(vis, 0, sizeof vis);
        int i=1;
        long long x;
        cin>>x;

        for(i=1;(x*i)>0; i++){
            go(x*i);
            if(allvis())break;
        }
        cout<<"Case #"<<f<<": ";
        if(x<=0)
            cout<<"INSOMNIA";
        else
            cout<<x*i;
        cout<<endl;
    }

    return 0;
}
