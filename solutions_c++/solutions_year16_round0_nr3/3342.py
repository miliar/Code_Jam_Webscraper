#include <iostream>
#include <bits/stdc++.h>
using namespace std;
bool isprime(long long int x,int* rs)
{
	if(x%2==0)
	{
		*rs=2;
		return false;
	}
	for(int i=3;i<=sqrt(x);i+=2)
	{
		if(x%i==0)
		{
			*rs=i;
			return false;
		}
	}
	return true;
}
int main()
{
    int t;
    cin>>t;
    int cs=1;
    while(t--)
    {
        int n,j,count=0;
        cin>>n>>j;
        cout<<"Case #"<<cs<<":\n";
        for(int i=(1<<(n-1))+1;i<(1<<n);i+=2)
        {
        	//printf("%d\n",i );
        	vector<int> vec;
        	//if((i&1))
        	{
        		int arr[n];
        		int k=0,rs;
        		int temp=i;
        		while(k<n)
        		{
        			arr[k]=temp%2;
        			temp=temp/2;
        			k++;
        		}
        		if(!isprime(i,&rs))
        		{
        			//printf("%d....\n",i );
        			vec.push_back(rs);
        		}
        		else
        		{
        			continue;
        		}
        		for(int jk=3;jk<=10;jk++)
        		{
        			long long int t2=0;
        			for(int k=0;k<n;k++)
        			{
        				if(arr[k]==1)
        				{
        					t2+=pow(jk,k);
        				}
        			}
        			if(!isprime(t2,&rs))
        			{
        				vec.push_back(rs);
        			}
        			else
        			{
        				break;
        			}
        		}
        		if(vec.size()==9)
        		{
        			for(int k=0;k<n;k++)
        				cout<<arr[n-k-1];
        			cout<<" ";
        			for(int k=0;k<9;k++)
        				cout<<vec[k]<<" ";
        			cout<<endl;
        			count++;
        			if(count==j)
        				break;
        		}
        	}
        }
        cs++;
    }
    
    return 0;
}
