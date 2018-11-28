#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //freopen("D-small-attempt2.in.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t; cin>>t;
    for (int tt=1;tt<=t;tt++) {
        string ans; int x,r,c;
        cin>>x>>r>>c;
        if (x==1) ans="GABRIEL";
        else if (x==2) {
            if ((r==1&&c==1)||(r==1&&c==3)||(r==3&&c==1)||(r==3&&c==3)) ans="RICHARD";
            else ans="GABRIEL";
        }
        else if (x==3) {
            if ((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==4)||(r==4&&c==3)||(r==3&&c==3)) ans="GABRIEL";
            else ans="RICHARD";
        }
        else if (x==4) {
            if ((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4)) ans="GABRIEL";
            else ans="RICHARD";
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
