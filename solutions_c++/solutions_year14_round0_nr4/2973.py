#include <iostream>
#include <cstdlib>
#include <deque>
#include <algorithm>

using namespace std;

deque <double> p,q,s,t;


int main()
{
	int i,j,k;
	double x,y;
	int T,S,N;
	int a,b;

	cin>>T;
	S=T;
	while(T--)
	{
		cin>>N;
		p.clear();
		q.clear();
		for(i=0;i<N;i++)
		{
			cin>>x;
			p.push_back(x);
			s.push_back(x);
		}
		for(i=0;i<N;i++)
		{
			cin>>x;
			q.push_back(x);
			t.push_back(x);
		}
		
		sort(p.begin(),p.end());
		sort(q.begin(),q.end());
		sort(s.begin(),s.end());
		sort(t.begin(),t.end());
		
		for(i=0,a=0;i<N;i++)
		{
			x=p.front();
			y=q.front();
			if(x<y)
			{
				p.pop_front();
				q.pop_back();
			}
			else
			{
				p.pop_front();
				q.pop_front();
				a++;
			}
		}
		for(i=0,b=0;i<N;i++)
		{
			x=s.front();
			y=t.back();
			if(x<y)
			{
				for(j=0;j<N;j++)
				{
					if(x<t[j])
					{
						s.pop_front();
						t.erase(t.begin()+j);
						break;
					}
				}
			}
			else
			{
				b++;
				s.pop_front();
				t.pop_front();
			}
		}
		cout<<"Case #"<<S-T<<": "<<a<<" "<<b<<endl;
		
	}


	return 0;
}
