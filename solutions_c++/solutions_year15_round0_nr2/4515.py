#include<iostream>
#include<string>
#include<set>
#include<iterator>
using namespace std;
int count(int ma,multiset<int> ms)
{	
	if(ma==1||ma==2){return ma;}
	multiset<int>ms2;
	multiset<int>ms3(ms.begin(),ms.end());
	multiset<int>::iterator it2=ms.begin();
	while(it2!=ms.end())
	{
		int xy=*it2-1;
		ms2.insert(xy);
		  it2++;
	}
multiset<int>::iterator it=ms2.begin();
 
   it=ms3.end();
	it--;
	int done=*it;
	ms3.erase(it);
	int mo2;
	if(done!=9)
	{
	ms3.insert(done/2);
	if(done%2==0)
		done/=2;
	else
	{done/=2; done++;}
	ms3.insert(done);
	 it=ms3.end();
	it--;
	 mo2=*it;
	}
	else
	{
		ms3.insert(6);
		ms3.insert(3);
		 it=ms3.end();
	it--;
	 mo2=*it;
 
	}
	return min(count(ma-1,ms2)+1,count(mo2,ms3)+1);
}
int main()
{
	freopen("B-small-attempt1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int s,c,f;
 string x;
 cin>>c;
 for(int i=0; i<c; i++)
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