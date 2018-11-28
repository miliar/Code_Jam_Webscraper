#define LOCAL
#include<iostream>
using namespace std; 

string flipS(string str,int len){
	char tmp;
	for(int i=0;i<len/2;i++){
		tmp=(str[i]=='+')?'-':'+';
		str[i]=(str[len-i-1]=='+')?'-':'+';
		str[len-i-1]=tmp;
	}
	if(len%2==1)str[len/2]=(str[len/2]=='+')?'-':'+';
	return str;
}

int main()
{
	#ifdef LOCAL
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out","w",stdout);
	#endif

	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int len=s.length();
		int times=0;
		int bottomIndex=len-1;
		while(true){
			bool judge=true;
			for(int j=0;j<bottomIndex+1;j++){
				if(s[j]=='-') judge=false;
			}
			if(judge){
				cout<<"Case #"<<i+1<<": "<<times<<endl;	
				break;
			}
			while(s[bottomIndex]!='-')bottomIndex-=1;
			int topIndex=0;
			while(s[topIndex]!='-')topIndex+=1;
			if(topIndex!=0){
				s=flipS(s,topIndex);
				times++;
			}
			s=flipS(s,bottomIndex+1);
			times++;
		}
	}
	return 0;
}