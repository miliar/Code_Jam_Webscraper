#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
    int t,x,r,c,i;
    cin>>t;
    for (i=1; i<=t; i++){
        cin>>x>>r>>c;
        cout<<"Case #"<<i<<": ";
        //if (r*c==x) cout<<"RICHARD"<<endl;
        if (x==1) cout<<"GABRIEL"<<endl;
        else if ((r*c)%x!=0) cout<<"RICHARD"<<endl;
        else if (x==4){
            if(r*c>=12) cout<<"GABRIEL"<<endl;
            else cout<<"RICHARD"<<endl;
        }
        else if (x==2) cout<<"GABRIEL"<<endl;
        else if (x==3){
            if(r*c>=6) cout<<"GABRIEL"<<endl;
            else cout<<"RICHARD"<<endl;
        }
    }
}
