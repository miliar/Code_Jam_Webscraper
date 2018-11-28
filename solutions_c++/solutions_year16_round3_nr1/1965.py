#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

struct p{
	char name;
	int num;
};

int t;
int n;
p a[27];

int cmp(p x,p y)
{
	return x.num>y.num;
}

int main()
{
	int i,j,k;
	int tcase=1;
	int num;
	freopen("A.in","r",stdin);
	freopen("A+","w",stdout);
	int sum;

	cin>>t;
	for(tcase=1;tcase<=t;tcase++)
	{
		sum=0;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>num;
			a[i].name=char('A'+i);
			a[i].num=num;
			sum+=num;
		}
		cout<<"Case #"<<tcase<<":";
		if(sum%2==0)
		{
			for(i=0;i<sum/2;i++)
			{
				sort(a,a+n,cmp);
				if(a[0].num==a[1].num)
				{
					cout<<" "<<a[0].name<<a[1].name;
					a[0].num--;
					a[1].num--;
				}
				else
				{
					cout<<" "<<a[0].name<<a[0].name;
					a[0].num--;
					a[0].num--;
				}
			}
		}
		else
		{
			for(i=0;i<sum/2-1;i++)
			{
				sort(a,a+n,cmp);
				if(a[0].num==a[1].num)
				{
					cout<<" "<<a[0].name<<a[1].name;
					a[0].num--;
					a[1].num--;
				}
				else
				{
					cout<<" "<<a[0].name<<a[0].name;
					a[0].num--;
					a[0].num--;
				}
			}
			sort(a,a+n,cmp);
			cout<<" "<<a[0].name;
			a[0].num--;
			sort(a,a+n,cmp);
			cout<<" "<<a[0].name<<a[1].name;
		}
		cout<<endl;
	}
//
	fclose(stdin);
	fclose(stdout);
	return 0;
}
