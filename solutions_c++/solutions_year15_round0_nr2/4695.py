#include<bits/stdc++.h>
using namespace std;
 
typedef long long int lli;
   
#define pc(x) putchar_unlocked(x);
#define gc() getchar_unlocked();
#define F(i, n) for(i = 0;i < n; ++i)
#define M 1000003

#define MAX 210
#define MAXN 200010

lli mint(lli a,lli b)
{
	if(a<b)
	return a;
	else return b;
}
lli b,maxt,i,j;
vector<lli>vec;
void bfs(queue<vector<lli> >q,queue<lli>no)
{
while(!q.empty())
{vec=q.front();
q.pop();
b=no.front();
no.pop();
	sort(vec.begin(),vec.end());
	maxt=vec[vec.size()-1];
if(maxt==0)
{
break;}
	
	vector<lli>vec1(vec.size());
	F(i,vec.size())
	{if(vec[i]>=1)
		vec1[i]=vec[i]-1;
	}
	
		
		q.push(vec1);
		//q.push(vec);
		no.push(b+1);
		//no.push(b+1);
	for(i=1;i<=maxt/2;i++)
	{vec[vec.size()-1]=maxt-i;
		vec.push_back(i);
		q.push(vec);
		no.push(b+1);
		vec.pop_back();
		}
}
return ;
}
int main(){
lli x=1,t;
cin>>t;
while(t--)
{lli d;
cin>>d;
lli a;

queue<vector<lli> >q;
queue<lli>no;
vec.clear();
F(i,d)
{cin>>a;
vec.push_back(a);
}
q.push(vec);
no.push(0);
bfs(q,no);
cout<<"Case #"<<x<<": "<<b<<"\n";
x++;
}
    return 0;
}
