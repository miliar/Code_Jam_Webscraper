#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void process(string a, string b);
string makeAnswer(string s, vector<int> is, vector<int> values);
bool gotNext(vector<int> v);
void print (vector<int> v){for(int i=0; i<v.size(); i++) cout<<v[i]<<" "; cout<<endl;}
void moveNext(vector<int> &v);
int getFirst(string a)
{
	string ret;
	for(int i=0; i<a.size()/2; i++)
	{
		ret+=a[i];
	}
	return stoi(ret);
}
int getSecond(string a)
{
	string ret;
	for(int i=0; i<a.size()/2; i++)
	{
		ret+=a[i+a.size()/2];
	}
	return stoi(ret);
}
int getDiff(string a)
{
	return abs(getFirst(a)- getSecond(a));
}
bool porownaj(string a, string b)
{
	//cout<<a<<" "<<b<<endl;
	if(getDiff(a)!=getDiff(b))
		return getDiff(a)<getDiff(b);
	if(getFirst(a)<getFirst(b))
		return getFirst(a)<getFirst(b);
	return getSecond(a)<getSecond(b);
}
int main()
{
	ios_base::sync_with_stdio(0);
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cout<<"Case #"<<aa+1<<": ";
		
		string a, b;
		cin>>a>>b;
		process(a, b);
		
		cout<<endl;
	}
}
void process(string a, string b)
{
	if(a=="???" && b=="???")
	{
		cout<<"000 000"<<endl;
		return;
	}
	string s=a+b;
	vector<int> questions;
	for(int i=0; i<s.size(); i++)
	{
		if(s[i]=='?')
			questions.push_back(i);
	}
	if(questions.size()==0)
	{
		cout<<a<<" "<<b;
		return;
	}
	vector<int> tmp;
	for(int i=0; i<questions.size(); i++)
	{
		tmp.push_back(0);
	}
	vector<string> tries;
	while(true)
	{
		tries.push_back(makeAnswer(s, questions, tmp));
		if(gotNext(tmp))
			moveNext(tmp);
		else break;
	}
	sort(tries.begin(), tries.end(), porownaj);
	string q, w;
	string res=tries[0];
	for(int i=0; i<res.size()/2; i++)
	{
		q+=res[i];
		w+=res[i+res.size()/2];
	}
	cout<<q<<" "<<w;
	
}
string makeAnswer(string s, vector<int> is, vector<int> values)
{
	for(int i=0; i<is.size(); i++)
	{
		s[is[i]]='0'+values[i];
	}
	return s;
}
bool gotNext(vector<int> v)
{
	for(int i=0; i<v.size(); i++)
	{
		if(v[i]!=9)
			return 1;
	}
	return 0;
}
void moveNext(vector<int> &v)
{
	v[0]++;
	int tmp=0;
	while(v[tmp]==10)
	{
		v[tmp]=0;
		v[tmp+1]++;
		tmp++;
	}
}
