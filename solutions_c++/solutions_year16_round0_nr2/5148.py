#include<iostream>
#include<stack>
#include<cstring>
#include<queue>

using namespace std;
int main()
{
	
	char p[103];
	int t;
	cin>>t;
	int k =1;
	while(t--)
	{
		stack<char> s ;
	    queue<char> q ;
		int count =0;	
		cin>>p;
		
		for( int i=strlen(p)-1 ;i>=0;i--)
		{
			s.push(p[i]);
			
		}
		bool flag = true ;
		while(!s.empty())		
		{
			if(q.empty())
			{
				q.push(s.top());
				s.pop();
				continue;
			}
			if(s.top() != q.back())
			{
				while(!q.empty())
				{
					s.push((q.front()== '+')?'-':'+');
					q.pop();
					
				}
				count++;
			}
			else
			{
				//cout<<"  "<<s.top()<<"  "<<q.back()<<"ewe";
				q.push(s.top());
				s.pop();
			}

		}
		if(q.front() == '-') count++;
		cout<<"Case #"<<k++<<": "<<count<<endl;	
	}


	return 0;
}
