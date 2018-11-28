#include <iostream>
#include <string>
#include <map>
#include <utility>      

using namespace std;

pair<int,char> equivalent(pair <char,char> p)
{
	
	map<pair<char,char> , pair<char,char>> quaternions;


	
	quaternions[make_pair('1','1')]=make_pair(1,'1');
	quaternions[make_pair('1','i')]=make_pair(1,'i');
	quaternions[make_pair('1','j')]=make_pair(1,'j');
	quaternions[make_pair('1','k')]=make_pair(1,'k');
	quaternions[make_pair('i','1')]=make_pair(1,'i');
	quaternions[make_pair('i','i')]=make_pair(-1,'1');
	quaternions[make_pair('i','j')]=make_pair(1,'k');
	quaternions[make_pair('i','k')]=make_pair(-1,'j');
	quaternions[make_pair('j','1')]=make_pair(1,'j');
	quaternions[make_pair('j','i')]=make_pair(-1,'k');
	quaternions[make_pair('j','j')]=make_pair(-1,'1');
	quaternions[make_pair('j','k')]=make_pair(1,'i');
	quaternions[make_pair('k','1')]=make_pair(1,'k');
	quaternions[make_pair('k','i')]=make_pair(1,'j');
	quaternions[make_pair('k','j')]=make_pair(-1,'i');
	quaternions[make_pair('k','k')]=make_pair(-1,'1');

	return quaternions[p];
}

int main()
{
     
	freopen("C-small-attempt6.in","r",stdin);
    freopen("output.txt","w",stdout);
	
	int T; cin>>T;
	for(int j=1; j<=T; j++)
	{
	int L,X; cin>>L>>X;
	string c; cin>>c;
	string s="";
	for(int i=0; i<X; i++)
	{
		s+=c;
	}

	int succi=-1;
    int succj=-1;
	int succk=-1;
	pair<int, char> muli=make_pair(1,s[0]);

	if(muli.first==1 && muli.second=='i')
	{ succi=0;}

	pair<int, char> mulj;
	pair<int, char> mulk;
	
if(succi==-1)
{
	for(int i=1; i<s.size(); i++)
	{
		muli.first*=equivalent(make_pair(muli.second,s[i])).first;
		muli.second=equivalent(make_pair(muli.second,s[i])).second;

		if(muli.first==1 && muli.second=='i')
	        {succi=i; break;}
	}
}

if(succi!=-1 && succi<s.size()-1)
{
	pair<int, char> mulj=make_pair(1,s[succi+1]);
	if(mulj.first==1 && mulj.second=='j')
	{ succj=succi+1;}
	else
	{
    for(int i=succi+2; i<s.size(); i++)
	{
		mulj.first*=equivalent(make_pair(mulj.second,s[i])).first;
		mulj.second=equivalent(make_pair(mulj.second,s[i])).second;

		if(mulj.first==1 && mulj.second=='j')
	        {succj=i; break;}
	}
	}
}


if(succj!=-1 && succj<s.size()-1)
{
	pair<int, char> mulk=make_pair(1,s[succj+1]);
	if(mulk.first==1 && mulk.second=='k' && succj+1==s.size()-1)
	        {succk=s.size()-1;}
	else
	{
	for(int i=succj+2; i<s.size(); i++)
	{
		mulk.first*=equivalent(make_pair(mulk.second,s[i])).first;
		mulk.second=equivalent(make_pair(mulk.second,s[i])).second;

		if(mulk.first==1 && mulk.second=='k' && i==s.size()-1)
	        {succk=i;}
	}
	}
}
	if(succi!=-1 && succj!=-1 && succk!=-1)
	{
		cout<<"Case #"<<j<<": YES"<<endl;
	}
	else
	{
		cout<<"Case #"<<j<<": NO"<<endl;
	}
	}
    return 0;

}

