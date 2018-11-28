#include<iostream>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<set>
#include<iterator>
#include<sstream>
using namespace std;
int count(int ma,multiset<int> se)
{	
	if(ma==1||ma==2){return ma;}
	multiset<int>se2;
	multiset<int>se3(se.begin(),se.end());
	multiset<int>::iterator it2=se.begin();
	while(it2!=se.end())
	{
		int xy=*it2-1;
		se2.insert(xy);
		  it2++;
	}
multiset<int>::iterator it=se2.begin();

   it=se3.end();
	it--;
	int done=*it;
	se3.erase(it);
	int mo2;
	if(done!=9)
	{
	se3.insert(done/2);
	if(done%2==0)
		done/=2;
	else
	{done/=2; done++;}
	se3.insert(done);
	 it=se3.end();
	it--;
	 mo2=*it;
	}
	else
	{
		se3.insert(6);
		se3.insert(3);
		 it=se3.end();
	it--;
	 mo2=*it;

	}
	return min(count(ma-1,se2)+1,count(mo2,se3)+1);
}
int main()
{
	freopen("B-small-attempt0.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int s,cases,f,minutes=0;
 string x;
 cin>>cases;
 for(int i=0; i<cases; i++)
 {
	 multiset<int> ms;
	 cin>>f;
	for(int d=0; d<f; d++)
	{
		cin>>s;
		ms.insert(s);
	}
	multiset<int>::iterator it=ms.end();
	it--;
	cout<<"Case #"<<i+1<<": "<<count(*it,ms)<<endl;	 
 }
}
