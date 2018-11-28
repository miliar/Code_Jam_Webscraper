#include<bits/stdc++.h>
using namespace std;




int main()
{
	int t;
	scanf("%d",&t);
	int tt=t;
	t=0;
	while(tt--)
	{
	t++;
	int n;
	priority_queue<pair<int,char> > vec;
	scanf("%d",&n);
	int x;
	long long count=0;
	for(int i=0;i<n;i++)
	{
		scanf("%d",&x);
		vec.push(make_pair(x,char(i+65)));
		count+=x;
    }
   /* for(int i=0;i<n;i++)
    {
        cout<<vec.top().first<<vec.top().second<<" ";
        vec.pop();
    }
    cout<<endl;*/
	cout<<"Case"<<" #"<<t<<":"<<" ";
	while(count!=0)
	{
	if(count!=3)
	{
	pair<int,char> p1=vec.top();
//	cout<<p1.first<<p1.second<<endl;
	vec.pop();
	p1.first--;
	vec.push(p1);
	pair<int,char> p2=vec.top();
	vec.pop();
	p2.first--;
	vec.push(p2);
	cout<<p1.second<<p2.second<<" ";
	count-=2;
    }
    else
    {
    pair<int,char> p3=vec.top();
	vec.pop();
	p3.first--;
	vec.push(p3);
	cout<<p3.second<<" ";
	count-=1;
	}
	}
	printf("\n");
	}
	return 0;
}