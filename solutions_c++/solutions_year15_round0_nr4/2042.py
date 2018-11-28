#include <iostream>
using namespace std;

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("cj_4.txt","w",stdout);
    int t,x,r,c;
	cin>>t;
	for(int z=0;z<t;z++)
	{
	    cin>>x>>r>>c;
	    switch(x)
	    {
	    case 1:
	        cout<<"Case #"<<z+1<<": GABRIEL"<<endl;
	        break;
	   case 2:
	        if((r*c)%2==0)
	            cout<<"Case #"<<z+1<<": GABRIEL"<<endl;
	        else
	            cout<<"Case #"<<z+1<<": RICHARD"<<endl;
	        break;
	    case 3:
	        if(r*c==6||r*c==12||r*c==9)
	            cout<<"Case #"<<z+1<<": GABRIEL"<<endl;
	       else
	            cout<<"Case #"<<z+1<<": RICHARD"<<endl;
	            break;
	   case 4:
	        if(r*c==12||r*c==16)
	            cout<<"Case #"<<z+1<<": GABRIEL"<<endl;
	        else
	            cout<<"Case #"<<z+1<<": RICHARD"<<endl;
	            break;
	    }
	   
	}
	return 0;
}
