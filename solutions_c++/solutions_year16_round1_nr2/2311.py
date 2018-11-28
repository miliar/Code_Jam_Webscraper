#include<bits/stdc++.h>
using namespace std;
int main() 
{
	int t,pp=1;
	cin>>t;
	while(t--)
	{
	    int n,i,j,a;
	    cin>>n;
	    int freq[2505];
	    memset(freq,0,sizeof(freq));
	    for(i=0;i<(2*n-1);i++)
	    {
	        for(j=0;j<n;j++)
	        {
	            cin>>a;
	            freq[a]++;
	        }
	    }
	    vector<int > ans;
	    for(i=0;i<2505;i++)
	    {
	        if(freq[i]%2==1)
	        ans.push_back(i);
	    }
	    cout<<"Case #"<<pp<<": ";
	    for(i=0;i<ans.size();i++)cout<<ans[i]<<" ";
	    cout<<"\n";
	    pp++;
	}
	return 0;
}
