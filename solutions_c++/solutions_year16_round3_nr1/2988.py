#include <iostream>
#include <algorithm>
#include <stack>
#include <string>
#include <queue>
using namespace std;
typedef struct data
{
	char index;
	int value;
}data;
struct compare  
{  
   bool operator()(const data& l, const data& r)  
   {  
       return l.value < r.value;  
   }  
};
int main()
{
	int t,t1=1;
	cin >> t;
	while(t1<=t)
	{
		int n,size,i;
		cin >> n;
		data array[n],a,b;
		string s;
		for(i=0;i<n;i++)
		{
			cin >> array[i].value;
			array[i].index=(char)65+i;
		}
		priority_queue < data, vector <data> , compare > q;
		for(i=0;i<n;i++)
		{
			q.push(array[i]);
		}
		cout << "Case #" <<t1<<": "; 
		while(!q.empty())
		{
			size=q.size();
			if(size%2==0)
			{
				a=q.top();
				q.pop();
				if(a.value-q.top().value==2)
				{
					cout << a.index << a.index <<" ";
					a.value-=2;
					q.push(a); 
				}
				else if(a.value-q.top().value==1)
				{
					cout<< a.index <<" ";
					a.value-=1;
					q.push(a);
				}
				else
				{
					b=q.top();
					q.pop();
					cout << a.index << b.index << " ";
					a.value-=1;
					b.value-=1;
					if(a.value!=0)
					{
						q.push(a);
						q.push(b);
					}
				}
			}
			else
			{
				a=q.top();
				q.pop();
				b=q.top();
				if(a.value-b.value==2)
				{
					cout << a.index << a.index <<" ";
					a.value-=2;
					q.push(a); 
				}
				else if(a.value-b.value==1)
				{
					cout<< a.index <<" ";
					a.value-=1;
					q.push(a);
				}
				else if(a.value==1 && b.value==1)
				{
					cout<< a.index<<" ";
					a.value=0;
				}
				else
				{
					q.pop();
					if(a.value==q.top().value)
					{
						cout<< a.index << a.index<<" ";
						a.value-=2;
						if(a.value>0)
						{
							q.push(a);
						}
						q.push(b);
					}
					else
					{	
						cout << a.index << b.index << " ";
						a.value-=1;
						b.value-=1;
						if(a.value!=0)
						{
							q.push(a);
							q.push(b);
						}
					}
				}
			}
		}
		cout << "\n";
		t1++;
	}
	return 0;
}