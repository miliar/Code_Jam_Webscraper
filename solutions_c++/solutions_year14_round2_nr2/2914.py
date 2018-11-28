# include <iostream>

using namespace std;

int main()
{
	int t,a,b,k,i=0;
	cin>>t;
	for(i=0;i<t;i++)
	{
		int count=0;
		cin>>a>>b>>k;
		int v_j,v_k;
		for(v_j=a-1;v_j>=0;v_j--)
		{
			for(v_k=b-1;v_k>=0;v_k--)
			{
				if((v_j&v_k)<=k-1)
					count++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}