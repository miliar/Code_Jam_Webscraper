#include <iostream>
using namespace std;

int main() {
	long long int t,i,len,dt,cnt;
	string s;
	cin>>t;
	dt=t;
	while(t--)
	{
	    cnt=0;
	    cin>>s;
	    len=s.length();
	    for(i=1;i<len;i++)
	    {
	        if(s[i]!=s[i-1])
	        cnt++;
	    }
	    if(s[len-1]=='-')
	    cnt++;
	    cout<<"Case #"<<dt-t<<": "<<cnt<<endl;
	}
	return 0;
}
