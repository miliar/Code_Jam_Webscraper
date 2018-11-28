#include<stdio.h>
#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<utility>
#include<list>
#define PB push_back
#define MP make_pair
#define LL long long int
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
using namespace std;

float a[1001],b[1001];
list<float> alist,blist;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	float s;
	int k,t,i,j,n;
	float temp1, temp2,temp3;
	sc(t);
	for(k=1;k<=t;k++)
	{
		sc(n);
		for(i=0;i<n;i++)
		scanf("%f",&a[i]);
		
		s = 0;
		for(i=0;i<n;i++)
		{
			scanf("%f",&b[i]);
			s += b[i];
		}
		
		sort(a,a+n);
		sort(b,b+n);
		
		for(i=n-1;i>=0;i--)
		{
			alist.PB(a[i]);
		}
		
		for(i=0;i<n;i++)
		{
			blist.PB(b[i]);
		}
		
		int g,naomi_real = 0;
		list<float>::iterator it = alist.begin();
		list<float>::iterator itj,itj_1;
		while(1)
		{
			if(it == alist.end())
			break;
			temp1 = *it;
			it = alist.erase(it);
			g = 0;
			for(itj = blist.begin();itj != blist.end();itj++)
			{
				temp2 = *itj;
				if(temp2 > temp1)
				{
					g = 1;
					itj_1 = blist.erase(itj);
					break;			
				}
			}
			if(g == 0)
			{
				itj_1 = blist.erase(blist.begin());
				naomi_real++;
			}
			
		}
		
		//cout<<naomi_real<<endl;
		//decitful war
		alist.clear();
		blist.clear();
		
		for(i=n-1;i>=0;i--)
		{
			alist.PB(a[i]);
		}
		
		for(i=0;i<n;i++)
		{
			blist.PB(b[i]);
		}
		list<float>::reverse_iterator it1;
		it = alist.begin();
		int naomi_fake = 0;
		while(1)
		{
			it = alist.begin();
			temp1 = *it;
			g = 0;
			for(itj = blist.begin();itj != blist.end();itj++)
			{
				temp2 = *itj;
				if(temp2 > temp1)
				{
					g = 1;
			//		cout<<*itj<<" ";
					itj_1 = blist.erase(itj);
					break;
				}
			}
			//cout<<temp1<<" "<<temp2<<endl;
			if(g == 0)
			{
			//	cout<<(*blist.begin())<<" ";
				temp2 = *blist.begin();
				itj_1 = blist.erase(blist.begin());
				naomi_fake++;
			}
			
			if(g == 1)
			{
				for(it1=alist.rbegin();it1 != alist.rend();it1++)
				{
					temp3 = *it1;
					//cout<<"here "<<temp3<<endl;
					//system("pause");
					if(temp3 < temp2)
					{
						for(itj_1 = alist.begin();itj_1 != alist.end();itj_1++)
						{
							if(*itj_1 == temp3)
							{
			//					cout<<*itj_1<<endl;
								itj_1 = alist.erase(itj_1);
								break;
							}
						}
						break;
					}	
				}
			}
			else
			{
				for(it1=alist.rbegin();it1 != alist.rend();it1++)
				{
					temp3 = *it1;
			//		cout<<"here "<<temp3<<endl;
			//		cout<<temp2<<endl;
			//		system("pause");
		
					if(temp3 > temp2)
					{
			//			cout<<"actual"<<endl;
						for(itj_1 = alist.begin();itj_1 != alist.end();itj_1++)
						{
							if(*itj_1 == temp3)
							{
			//					cout<<*itj_1<<endl;
								
								itj_1 = alist.erase(itj_1);
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
		printf("Case #%d: %d %d\n",k,naomi_fake,naomi_real);
		//cout<<naomi_fake<<endl;
	}
	
	return 0;
}

