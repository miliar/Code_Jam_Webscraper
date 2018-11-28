#include<iostream>

using namespace std;

int main()
{
    int test,i,t,n,j,m,k,count;
    cin>>test;
    for(t=1;t<=test;t++)
    {
        cin>>n>>m>>k;
        count=0;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			if((i&j)<k)
				count=count+1;
	cout<<"Case #"<<t<<": "<<count<<endl;
    }
    return 0;
}

