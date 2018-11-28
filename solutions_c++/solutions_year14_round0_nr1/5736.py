#include<iostream>

using namespace std;


int main()
{
    int t;
	cin>>t;
	int j=1;
	while(t!=0)
	{
		
		int q,p,x,b,c,d,y,z,e,f,a[16]={0};
		cin>>p;
	for(int i=1;i<=4;i++)
	{
		cin>>x>>b>>c>>d;
		if(i==p)
		{
			a[x-1]=1;
			a[b-1]=1;
			a[c-1]=1;
			a[d-1]=1;
		}
	
	}
	cin>>q;

	for(int i=1;i<=4;i++)
	{
		cin>>y>>z>>e>>f;
		if(i==q)
		{
			a[y-1]++;
			a[z-1]++;
			a[e-1]++;
			a[f-1]++;
		}

	}
	int l=0,h;
	for(int i=1;i<=16;i++)
	{
		if(a[i-1]>1)
		{
			l++;
			h=i;
		}
		
	}
	
	if(l==1)
	cout<<"Case #"<<j<<": "<<h<<endl; 
	else if(l>1)
	cout<<"Case #"<<j<<": Bad magician!"<<endl; 
	else
	cout<<"Case #"<<j<<": Volunteer cheated!"<<endl; 
	
    	j++;
		
		t--;
	}
	return 0;
} 
