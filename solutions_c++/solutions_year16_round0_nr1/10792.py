#include<iostream>
#include<string>
using namespace std;
long long s,n;
bool flag[10];
int t;
void initial ()
{
	for (int y=0;y<10;y++)
	{
		flag[y]=false;
	}
}
bool check ()
{
	long long mimic;
	mimic=s;

	for (int q=0;mimic!=0;q++)
	{
		int thelper=mimic%10;
		flag[thelper]=true;
		mimic/=10;
	}
	for (int y=0;y<10;y++)
	{
		if(!flag[y])return false;
	}
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("h.txt","w",stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		initial();
		cin>>n;
		cout<<"Case #"<<i+1<<": "; 
		if (n==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{
			//n=i;
			s=n;
			check();
			for(long long j=2;true;j++)
			{
				s=n*j;
				if (check())
				{
					cout<<s<<endl;
					break;
				}
			}
		}
	}
	
	return 0;
}
