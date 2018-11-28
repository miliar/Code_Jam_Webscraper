#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<list>
using namespace std;
double a[1001],b[1001];
list<double> alist,blist;

int main()
{
	double s;
	int k=1,t,i,j,n;
	double temp1, temp2,temp3;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for(i=0;i<n;i++)
            cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		for(i=n-1;i>=0;i--)
		{
			alist.push_back(a[i]);
		}

		for(i=0;i<n;i++)
		{
			blist.push_back(b[i]);
		}

		int flag,real = 0;
		list<double>::iterator it = alist.begin();
		list<double>::iterator it1,it2;
		while(1)
		{
			if(it == alist.end())
                break;
            temp1 = *it;
            it = alist.erase(it);
			flag = 0;
			for(it1 = blist.begin();it1 != blist.end();it1++)
			{
				temp2 = *it1;
				if(temp2 > temp1)
				{
					flag = 1;
					it2 = blist.erase(it1);
					break;
				}
			}
			if(flag == 0)
			{
				it2 = blist.erase(blist.begin());
				real++;
			}

		}
		alist.clear();
		blist.clear();

		for(i=n-1;i>=0;i--)
		{
			alist.push_back(a[i]);
		}

		for(i=0;i<n;i++)
		{
			blist.push_back(b[i]);
		}
		list<double>::reverse_iterator irt1;
		it = alist.begin();
		int fake = 0;
		while(1)
		{
			it = alist.begin();
			temp1 = *it;
			flag = 0;
			for(it1 = blist.begin();it1 != blist.end();it1++)
			{
				temp2 = *it1;
				if(temp2 > temp1)
				{
					flag = 1;
					it2 = blist.erase(it1);
					break;
				}
			}
			if(flag == 0)
			{
				temp2 = *blist.begin();
				it2 = blist.erase(blist.begin());
				fake++;
			}

			if(flag == 1)
			{
				for(irt1=alist.rbegin();irt1 != alist.rend();irt1++)
				{
					temp3 = *irt1;
					if(temp3 < temp2)
					{
						for(it2 = alist.begin();it2 != alist.end();it2++)
						{
							if(*it2 == temp3)
							{
								it2 = alist.erase(it2);
								break;
							}
						}
						break;
					}
				}
			}
			else
			{
				for(irt1=alist.rbegin();irt1 != alist.rend();irt1++)
				{
					temp3 = *irt1;
					if(temp3 > temp2)
					{
						for(it2 = alist.begin();it2 != alist.end();it2++)
						{
							if(*it2 == temp3)
							{
								it2 = alist.erase(it2);
								break;
							}
						}
						break;
					}
				}
			}
			if(alist.empty())
                break;
		}
		printf("Case #%d: %d %d\n",k,fake,real);
		k++;
	}

	return 0;
}
