#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

map<string,string> p;


bool Calc(const string& text)
{
	if(text.size()<3)
		return false;
	
	if(text.size()==3)
	{
		if(text=="ijk")
			return true;
		return false;
	}
	
	
	int next=0;
	string arr[]={"i","j","k"};
	string curr="";
	
	int i;
	for(i=0;i<text.size()&&next<3;i++)
	{
		curr+=text[i];
		bool neg=false;
		if(curr[0]=='-')
		{curr.erase(curr.begin());		neg=true;}
		curr=p[curr];
		if(neg)
		{
			if(curr[0]=='-')
				curr.erase(curr.begin());
			else
				curr.insert(0,"-");
		}
		if(curr==arr[next])
		{curr="";	++next;}
	}
	if(i==text.size())
	{
		if(next==3)
			return true;
		return false;
	}
	curr="";
	for(;i<text.size();i++)
	{
		curr+=text[i];
		bool neg=false;
		if(curr[0]=='-')
		{curr.erase(curr.begin());		neg=true;}
		curr=p[curr];
		if(neg)
		{
			if(curr[0]=='-')
				curr.erase(curr.begin());
			else
				curr.insert(0,"-");
		}
	}
	if(curr=="1")
		return true;
	return false;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Coutput.txt","w",stdout);
	int T,L,X;
	cin>>T;
	string s,text;
	
	p["1"]="1";
	p["i"]="i";
	p["j"]="j";
	p["k"]="k";
	
	p["11"]="1";
	p["1i"]="i";
	p["1j"]="j";
	p["1k"]="k";
	
	p["i1"]="i";
	p["ii"]="-1";
	p["ij"]="k";
	p["ik"]="-j";
	
	p["j1"]="j";
	p["ji"]="-k";
	p["jj"]="-1";
	p["jk"]="i";
	
	p["k1"]="k";
	p["ki"]="j";
	p["kj"]="-i";
	p["kk"]="-1";
	
	for(int i=1;i<=T;i++)
	{
		text="";
		cin>>L>>X>>s;
		for(int j=0;j<X;j++)
			text+=s;
		
		cout<<"Case #"<<i<<": ";
		
		if(Calc(text))
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}