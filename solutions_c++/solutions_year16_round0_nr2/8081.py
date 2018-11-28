#include<iostream>
using namespace std;

void flip(int *n1,int *n2){
	reverse(n1,n2);
	while(n1<=n2){
		*n1=(*n1) * -1;
		n1++;
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	string str;
	int c,s,count;
	cin >>c;
	for(int z=1;z<=c;z++){
		count=0;
		str.clear();
		cin>>str;
		if(str.find("-",0)==string::npos)
		goto E;
		while(str.find("-",0)!=string::npos){
		if(str[0]=='+'){
		count++;
		int g=int(str.find_first_of("-",0));
		for(int i=0;i<g;i++){
			str[i]='-';
		}
		}
		//if(str.find("-",0)==string::npos)
		//goto E;
		string ss=str.substr(0,int(str.find_last_of("-",str.size()))+1);
		if(ss.size()==1 && ss[0]=='-'){
		count++;
		goto E;
		}
		for(int i=0;i<ss.size();i++){
			if(ss[i]=='-')
			ss[i]='+';
			else
			ss[i]='-';
		}
		reverse(ss.begin(),ss.end());
		count++;
		str.clear();
		str=ss;
		//cout<<str<<endl;
		}
		E:;
		cout<<"Case #"<<z<<": "<<count<<endl;
	}
	return 0;
}