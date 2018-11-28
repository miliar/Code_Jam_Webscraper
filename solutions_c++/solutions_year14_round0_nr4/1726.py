#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	vector<float> na,k,x,y;
	int t,n,i,j,cd,cw;
	float m;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cd=0;cw=0;
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>m;
			na.push_back(m);
		}
	     
		for(j=0;j<n;j++)
		{
			cin>>m;
			k.push_back(m);
		}
		sort(na.begin(),na.end());
		sort(k.begin(),k.end());
		x=na;
		y=k;
		int r=n;
		r--;
		while(r!=-1)
		{
		   
			for(j=0;j<=r;j++)
			if(na[0]<k[j])
				break;
		
			if(j>r)
			{
			cd++;
			j=0;
		    }
			na.erase(na.begin());
			k.erase(k.begin()+j);
			r--;
		}
		n--;
		while(n!=-1)
		{
			if(x[0]>y[n])
			{
				cw+=n+1;
				break;
			}
			
			 if(x[0]>y[0])
			{
				cw++;
				x.erase(x.begin());
				y.erase(y.begin());
				n--;
			}
			else 
			{
				x.erase(x.begin());
				y.pop_back();
				n--;
			}
			
		}
		cout<<"Case #"<<(i+1)<<": "<<cw<<" "<<cd<<"\n";
		x.clear();
		y.clear();
		na.clear();
		k.clear();
	}
	return 0;
}
