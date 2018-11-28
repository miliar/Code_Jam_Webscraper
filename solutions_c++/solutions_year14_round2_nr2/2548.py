#include<iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	int a,b,k,count,m,n,temp;
	for(int i=0;i<t;i++)
	{
		count=0;
		cin>>a>>b>>k;
		for(m=0;m<a;m++)
		{
			for(n=0;n<b;n++)
			{
				temp=(m&n);
				if(temp < k)
					count++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}