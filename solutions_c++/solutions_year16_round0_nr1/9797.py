#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t, it;
	cin>>t;
    for(it=1; it<=t; it++)
	{
	    int n, i, j=1, num;
	    cin>>n;
	    if(n==0) cout<<"Case #"<<it<<": INSOMNIA"<<endl;
	    else
	    {
	    set<int> s;
	    while(s.size()<10)
	    {
	        num=n*j;
	        while(num>0)
	        {
	          s.insert(num%10);
	          num/=10;
	        }
	        j++;
	    }
	    j--;
	    cout<<"Case #"<<it<<": "<<(n*j)<<endl;
	    }
	}
	return 0;
}
