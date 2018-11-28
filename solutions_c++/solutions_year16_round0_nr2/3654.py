#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int reverse(char s[],int last){
	int start,end,loop1=0,loop2=0,plus=0,i=0;
	while(s[i]=='+'){
		s[i]='-';
		loop1=1;
		i+=1;
	}
	if(loop1){
		plus+=1;
		i=0;
	}
	while(i<=last){
		if(s[i]=='+' && s[last]=='+'){
			s[i]=s[last]='-';
		}
		else if(s[i]=='-' && s[last]=='-'){
			s[i]=s[last]='+';
		}
		else if(s[i]=='+' && s[last]=='-'){
			s[i]='-';
			s[last]='+';
		}
		else{
			s[i]='+';
			s[last]='-';
		}
		i+=1;
		last-=1;
	}
	return plus+1;
}

int main(){
	//freopen("C:\\Users\\P\\Downloads\\B-large.in","r+",stdin);
	//freopen("C:\\Users\\P\\Desktop\\muk\\output_large.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int ss=0;ss<tc;ss++){
		int slen=0,plus=0,final=0;
		char s[101];
		cin>>s;
		slen=strlen(s);
		while(strlen(s)!=plus){
			if(s[slen-1]=='-'){
				final+=reverse(s,slen-1);
			}
			plus+=1;
			slen-=1;
		}
		cout<<"Case #"<<ss+1<<": "<<final<<endl;
	}
	return 0;
}
