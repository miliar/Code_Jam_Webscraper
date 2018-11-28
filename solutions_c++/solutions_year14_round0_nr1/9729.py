
#include <iostream>
using namespace std;

short T, i, j, p, ans;
short temp;
short ans1[4];
short ans2;
short out[100];
bool in;

int main()
{
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>ans;
		for(j=1;j<ans;j++)
			for(p=0;p<4;p++)
				cin>>temp;
		for(p=0;p<4;p++)
				cin>>ans1[p];
		for(j=ans+1;j<5;j++)
			for(p=0;p<4;p++)
				cin>>temp;

		cin>>ans;
		for(j=1;j<ans;j++)
			for(p=0;p<4;p++)
				cin>>temp;
		for(p=0;p<4;p++)
		{
			cin>>ans2;
				for(j=0;j<4;j++)
					if (ans1[j]==ans2)
					{
						out[i]=ans2;
						if (in)
							out[i]=17;
						in=true;
					}
		}
		for(j=ans+1;j<5;j++)
			for(p=0;p<4;p++)
				cin>>temp;
		in=false;
	}
	for(i=0;i<T;i++)
	{
		if (out[i]==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
		else
			if(out[i]==17)
				cout<<"Case #"<<i+1<<": Bad magician!""\n";
			else
				cout<<"Case #"<<i+1<<": "<<out[i]<<"\n";
	}
	return 0;
}

