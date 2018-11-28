#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen ("D-small-attempt0.in","r",stdin);
    freopen ("myDsmallfile.txt","w",stdout);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1)
            cout<<"Case #"<<h<<": GABRIEL"<<endl;
        else if(x==2){
            if(r*c%2)
                cout<<"Case #"<<h<<": RICHARD"<<endl;
            else
                cout<<"Case #"<<h<<": GABRIEL"<<endl;
        }
        else if(x==3){
            if(r==1||c==1||r*c%3)
                cout<<"Case #"<<h<<": RICHARD"<<endl;
            else
                cout<<"Case #"<<h<<": GABRIEL"<<endl;
        }
        else{
            if(r*c<12)
                cout<<"Case #"<<h<<": RICHARD"<<endl;
            else
                cout<<"Case #"<<h<<": GABRIEL"<<endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
