#include<iostream>
#include<algorithm>
#include<vector>
#include<iterator>
using namespace std;
vector<char> A;
int main()
{void rem();
void incr();
int T,t,count;
char a[110];
cin>>t;
for(T=1;T<=t;T++)
{	count=0;
	A.clear();
	cin>>a;
	for(int i=0;a[i]!='\0';i++)
	{
		A.push_back(a[i]);
	}
	A.push_back('\0');
	while(1){	
	if(A.size()==2&&A.at(0)=='+')
	break;
	rem();
	
	if(A.size()==2&&A[0]=='+')
	break;
		incr();
	
		count++;
	}
	cout<<"Case #"<<T<<": "<<count<<endl;
}

return 0;
}
void rem()
{	int t=A.size();
char p=A[0];
	if(A.size()==2)
	return;
	int i=1;
	for(int I=0;I<t-2;I++,i++)
	{
		if(p==A[i]){
		
		A.erase(i+A.begin());
		i--;}
		else
		p=A[i];
	}
	return;
}
void incr()
{int cy=1;
for(int i=0;A[i]!='\0';i++)
{
	if(cy==1)
	{
		if(A[i]=='-')
		{A[i]='+';
		cy=0;
		}
		else
		{
			A[i]='-';
			cy=1;
		}
	}
	if(cy==0)
	break;
}
	
}
