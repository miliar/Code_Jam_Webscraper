#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<map>
using namespace std;

void printStack(stack<bool> s)
{
	while(!s.empty()){
		cout<< s.top();
		s.pop();
	}
	cout<<endl;
}

int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
	int t;
	cin>>t;
	string s;
    for(int t_case = 1; t_case <= t; t_case++)
	{
		cin>>s;
		stack<bool> ini_s;
		map<stack<bool>, bool> m;
		for(int i = s.length() - 1 ; i >= 0; i--)
		{
			bool toAdd = s[i] == '+';
			ini_s.push(toAdd);			
		}			
		queue< pair<stack<bool>, int> > q;		
		q.push(make_pair(ini_s, 0));
		m[ini_s] = true;
		int min_cc;
		while(!q.empty())    	
		{
			pair<stack<bool> , int> c = q.front();
			q.pop();
			stack<bool> c_s = c.first;
			//cout<<"Current stack: ";
			//printStack(c_s);
			int c_c = c.second;
			//cout<<"Current count: "<<c_c<<endl;
			stack<bool> tmp = c_s;
			bool already_done = true;
			while(!tmp.empty())
			{
				if(!tmp.top())
				{				
					already_done = false;
					break;
				}
				tmp.pop();
			}
			if(already_done)
			{
				min_cc = c_c;
				break;
			}
			for(int i = 1; i <= c_s.size(); i++)
			{
				tmp = c_s;
				queue<bool> aux;
				for(int i_aux = 0; i_aux < i; i_aux++)
				{							
					aux.push(!tmp.top());			
					tmp.pop();
				}		
				while(!aux.empty())
				{		
					tmp.push(aux.front());
					aux.pop();
				}
				if(!m[tmp])
					q.push(make_pair(tmp, c_c + 1));
				m[tmp] = true;
			}
		}
		cout<<"Case #"<<t_case<<": "<<min_cc<<endl;
	}
}
