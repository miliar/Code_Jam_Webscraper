#include<list>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{	int t;
	cin>>t;
	for ( int l=1; l<=t; l++ )
	{	int t, n;
		cin>>n;
		float a[n+2], b[n+2];
		for ( int i=0; i<n; i++ )
			cin>>a[i];
		for ( int i=0; i<n; i++ )
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		list<float> l1;
		list<float> l2;
		for ( int i=0; i<n; i++ )
		{	l1.push_back(a[i]);
			l2.push_back(b[i]);
		}
		list<float> l3=l1;
		l3.reverse();
		list<float> l4=l2;
		l4.reverse();
		int count1=0, count2=0;
		for ( int i=0; i<n; i++ )
		{	//cout<<l1.front() <<" "<<l2.front()<<endl;
			if ( l1.front() > l2.front() )
			{	count2++;
				l1.pop_front();
				l2.pop_front();
			}
			else
			{	l1.pop_front();
				l2.pop_back();
			}
		}
		for ( int i=0; i<n; i++ )
		{	//cout<<l3.front() <<" "<<l4.front()<<endl;
			if ( l3.front() > l4.front() )
			{	count1++;
				l3.pop_front();
				l4.pop_back();
			}
			else
			{	l3.pop_front();
				l4.pop_front();
			}
		}
		printf("Case #%d: %d %d\n", l, count2, count1);
	}
	return 0;
}
