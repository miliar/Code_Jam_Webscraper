#include <iostream>
using namespace std;

int main() {
    int t,x,c,i,n,y=0;
    string str;
	cin>>t;
	while(t--)
	{
	    y++;
	    c=0;
	    x=0;
	    cin>>n>>str;
	    for(i=0;i<=n;i++)
	    {
	        if(c<i) 
	        {
	            x+=(i-c);
	            c+=(i-c);
	        }
	        c+=str[i]-48;
	    }
	    cout<<"Case #"<<y<<": "<<x<<endl;
	}
	return 0;
}
