#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,td,n,m,i,a[100005],start,end;
	string s;
	char ans[4000];
	cin>>t;
	td=t;
	while(t--)
	{
	    cout<<"Case #"<<td-t<<": ";
	    start=end=2000;
	    cin>>s;
	    int len=s.length();
	    ans[2000]=s[0];
	    for(i=1;i<len;i++)
	    {
	        if(s[i]>=ans[start])
	        ans[--start]=s[i];
	        else
	        ans[++end]=s[i];
	    }
	    for(i=start;i<=end;i++)
	    cout<<ans[i];
	    cout<<endl;
	}
	return 0;
}
