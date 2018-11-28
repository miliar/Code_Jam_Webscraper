#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<deque>
using namespace std;
int main()
{
	ofstream off;
    off.open("opt1.txt",ios::out|ios::app);
    ifstream iff;
    iff.open("inpt1.txt",ios::in);
    int t;
    iff>>t;
    for(int j=0;j<t;j++)
    {
    	long long n,m;
    	iff>>n>>m;
    	long long a[m];
    	for(int i=0;i<m;i++)
    	iff>>a[i];
    	sort(a,a+m);
    	int ans=0;
    	for(int i=0;i<m;i++)
    	{
    		//cout<<"N is "<<n<<endl;
    		if(n==1)
    		{
    			ans=m;
    			break;
    		}
    		if(a[i]<n)
    		n+=a[i];
    		else if(a[i]>=n)
    		{
    			int k=0;
    			//cout<<"For "<<a[i]<<" "<<n<<endl;
    			while(n<=a[i])
    			{
    				n=2*n-1;
    				k++;
    				cout<<n<<endl;
    			}
    			if(k>(m-i))
    			{
    				ans+=(m-i);
    				break;
    			}
    			else
    			{
    				ans+=k;
    				n+=a[i];
    			}
    		}
    	}
    	if(ans>m )
    	ans=m;
    	if(j==99)
    	off<<"Case #"<<j+1<<": "<<ans;
    	else
    	off<<"Case #"<<j+1<<": "<<ans<<"\n";
    	//cout<<"Case #"<<j+1<<": "<<ans<<"\n";
    }
    
}
