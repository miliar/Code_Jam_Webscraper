#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<iterator>

using namespace std;

typedef vector<int> vi;
typedef vector<int>::iterator vii;

int ans[110];

int check(vi v1,vi v2)
{
	vii p;
	vii q;
	int result=0,temp;
	for(p=v1.begin();p!=v1.end();p++)
	{
		if(find(v2.begin(),v2.end(),*p) != v2.end())
		{
			result++;
			temp=*p;	
		}	
	}
	if(result==0)
	{
		return 0;
	}
	else if(result==1)
	{
		return temp;
	}
	else
	{
		return 100;
	}
}

int tc;

void show(vi v)
{
	vii p;
	for(p=v.begin();p!=v.end();p++)
		cout<<*p<<" ";
	cout<<endl;
}

int main()
{
	
	cin>>tc;
	
	for(int z=0;z<tc;z++)
	{
		int m,n,num;
		vi v1,v2;
		cin>>m;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==(m-1))
				{
					v1.insert(v1.end(),num);
				}
			}
		}
		cin>>n;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==(n-1))
				{
					v2.insert(v2.end(),num);
				}
			}
		}
		ans[z]=check(v1,v2);
	}
	
	for(int z=0;z<tc;z++)
	{
		cout<<"Case #"<<z+1<<": ";
		switch(ans[z])
		{
			case 0:
				cout<<"Volunteer cheated!";break;
			case 100:
				cout<<"Bad magician!";break;
			default:
				cout<<ans[z];
		}
		cout<<endl;
	}
	
	return 0;
}


