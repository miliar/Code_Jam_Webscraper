#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	int t,i,count,j;
	string st;
	cin>>t;
	j=1;
	while(t--)
	{
	    count=1;
	    cin>>st;
	    int k=st.length();
	    for(i=0;i<k-1;i++)
	    {
	        if(st[i]!=st[i+1])
	        count++;
	    }
	    if(st[k-1]=='+')
	    count--;
	    cout<<"Case #"<<j<<": "<<count<<"\n";
	    j++;
	}
	return 0;
}
