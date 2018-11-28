#include<iostream>
using namespace std;
#include<string.h>
//char s[200];
int count=0;
int flip(char s[], int b){
	char t[200];
	int v=b;
	for(int i=0;i<=b;i++)
	{	t[i]=s[v];
		if(t[i]=='+')
			t[i]='-';
		else
			t[i]='+';
		v--;
	}
	for(int i=0;i<=b;i++)
		s[i]=t[i];
	count++;
}		


int main()
{	int t,p=1,c=0,ind,frn=0;
	cin>>t;
	
	while(p<=t){
		count=0;
		char s[200];
		cin>>s;
		for(int i=0;i<strlen(s);i++)
			if(s[i]=='+')
				c++;
		if(c==strlen(s))
			{ cout<<"Case #"<<p<<": "<<"0\n";
			//cout<<"jjjjj";		
			c=0;
			p++;
			continue;}
		c=0;
	ind=strlen(s)-1;
	while(ind>=0){
		frn=0;
		//ind=strlen(s)-1;
		while(s[ind]=='+')
			ind--;
		if(ind>=0){while(s[frn]=='+')
			frn ++;
		if(frn!=0) flip(s,frn-1);
		flip(s,ind);}
								
	}
	cout<<"Case #"<<p<<": "<<count<<"\n";
	//cout<<"hhhh";
	p++; 
}


return 0;
}