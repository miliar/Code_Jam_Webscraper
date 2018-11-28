#include<bits/stdc++.h>
using namespace std;
int counter=1;
void dojob()
{
	list<char>c;
	char a[1005];
	cin>>a;
	c.push_back(a[0]);
	char temp=a[0];
	int i,j,k;k=strlen(a);
	for(i=1;i<k;i++)
	{
		if(a[i]<temp)c.push_back(a[i]);
		else {c.push_front(a[i]);temp=a[i];}
	}
	cout<<"Case #"<<counter++<<": ";
	for (std::list<char>::iterator it=c.begin(); it!=c.end(); ++it)
		    std::cout << *it;
	cout<<endl;
}
int main()
{
	int t;cin>>t;
	while(t--)dojob();
	return 0;
}
