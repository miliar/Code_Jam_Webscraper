#include<iostream>
#include<string>
#include<math.h>
#include<queue>
using namespace :: std;

struct Pair
{
	string conf;
	int depth;
};
int BFS_init(string input);
int main()
{	
	int i, T, res;
	string inp;
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>inp;
		res=BFS_init(inp);
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}

int val(string num)
{
	int i, res=0;
	for (int i=0; i<num.length(); ++i){
		if(num[i]=='+')
			res+=pow(2,i);
	}
	return res;
}
string calcNew(int rot, string curr)
{
	string res="", same=curr.substr(rot, curr.length()-rot), change=curr.substr(0, rot);
	int i;
	for(i=0;i<rot;i++){
		if(change[i]=='+')
			res="-"+res;
		else
			res="+"+res;
	}
	return res+same;
}
int BFS_init(string input)
{
	queue<Pair> myqueue;
	string newconf, goal="";
	int lookup[1024], i, length, res, lv;
	struct Pair temp, newitem;
	temp.conf=input;	
	temp.depth=0;
	myqueue.push(temp);
	for(i=1;i<=input.length();i++)
		goal=goal+"+";
	for(i=0;i<(int)pow(2,input.length());i++)
		lookup[i]=0;
if(input==goal)
	return 0;

	while(!myqueue.empty()){
		temp=myqueue.front();
		myqueue.pop();
		length=temp.conf.length();
		for(i=1;i<=length;i++){
			newconf=calcNew(i, temp.conf);//new configuration
			lv=val(newconf);
			if(lookup[lv]==1)//exists
				continue;
			else
				lookup[lv]=1;
			if(newconf==goal)
				return temp.depth+1;
			newitem.conf=newconf;
			newitem.depth=temp.depth+1;
			myqueue.push(newitem);
		}
	}
	return -1;
}
