#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("ak.in","r",stdin);
    freopen("ak2.out","w",stdout);
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	    int x,r,c,s;
	    cin>>x>>r>>c;
	    if(x==1)
	        cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
        else if(x==2)
        {
            if((r*c)%2==0)
                cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
        }
        else if(x==3)
        {
            s=r*c;
            if(s%3==0 && s>3)
                cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
        }
        else if(x==4)
        {
            s=r*c;
            if(s%4==0 && s>8)
                cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
        }
	}
	return 0;
}
