#include<iostream>
#include<algorithm>
using namespace std;
int main()
{

int t,c1,c2;
double l1[1000],l2[1000],l3[1000];

cin>>t;
for(int i=0;i<t;i++)
{cin>>c1;
for(int j=0;j<c1;j++)
	cin>>l1[j];

for(int j=0;j<c1;j++)
	cin>>l2[j];
sort(l1,l1+c1);
sort(l2,l2+c1);
int count=0;

for(int j=0;j<c1;j++)
	l3[j]=l2[j];

int count2=0;
for(int j=0;j<c1;j++)
	{for(int k=0;k<c1;k++)
		{if(l1[j]>l3[k]&& l3[k]!=-1)
			{l3[k]=-1;break;}
		}
	}

for(int j=0;j<c1;j++)
	{if(l3[j]==-1) count2++;
	}

for(int j=0;j<c1;j++)
	{for(int k=0;k<c1;k++)
		{if(l1[j]<l2[k])
			{l2[k]=-1;break;}
		}
	}

for(int j=0;j<c1;j++)
	{if(l2[j]!=-1) count++;
	}


//count2=c1-count2;
cout<<"Case #"<<i+1<<": "<<count2<<" "<<count<<endl;

}
}
