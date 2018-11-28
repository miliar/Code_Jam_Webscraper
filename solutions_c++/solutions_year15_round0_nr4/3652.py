#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int l=1;l<=t;l++)
    {
        cout<<"Case #"<<l<<": ";
        int r,c,x;
        cin>>x>>r>>c;
        switch(x)
        {
            case 1:cout<<"GABRIEL\n";break;
            case 2:if((r*c)%2) cout<<"RICHARD\n";
            else cout<<"GABRIEL\n";break;
            case 3:if(min(r,c)>1 && (r*c)%3==0) cout<<"GABRIEL\n";
            else cout<<"RICHARD\n";break;
            case 4:if(r*c==12 || r*c == 16) cout<<"GABRIEL\n";
            else cout<<"RICHARD\n";break;
        }
    }
    return 0;
}