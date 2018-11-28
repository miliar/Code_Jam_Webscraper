#include<iostream>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cstdio>

using namespace std;
int longestString(string str,int begin) {
	int end=begin;
	int flag=0,i=begin;
	for(i=begin;i<str.length()-1;i++) {
		if(str[i]==str[i+1]) {
			end++;
		}
		else {
			flag=1;
			break;
		}
	}
	return end;
}
int main() {
	int t;
	scanf("%d",&t);
	char p='+',n='-';
	for(int i=1;i<=t;i++) {
		string str;
		cin>>str;
		int count=0;
		string res="";
		
		for(int j=0;j<str.length();j++) {
			j=longestString(str,j);
			char ch=str[j];
			res+=ch;
		}
		if(res.length()==1) {
			if(res[0]=='-') {
				printf("CASE #%d: 1\n",i);
				continue;
			}
			else {
				printf("CASE #%d: 0\n",i);
				continue;
			}
		}
		while(res.length()!=1) {
			//cout<<"initial"<<res<<endl;
			int j=0;
			//for(int j=0;j<res.length()-1;j++) {
				//printf("here");
				if(res.substr(j,2)=="-+"){
					//temp+=temp.substr(j+1,2);
					//printf("y\n");
					res.replace(j,1,"+");
					count+=1;
				}
				else if(res.substr(j,2)=="+-"){
					//printf("n\n");
					res.replace(j,1,"-");
					count+=1;
				}
				//cout<<"replace"<<res<<endl;
		//	}
			string temp=res;
			res="";
			//cout<<res<<" temp"<<temp;
			for(int j=0;j<temp.length();j++) {
				j=longestString(temp,j);
				char ch=temp[j];
				res+=ch;
			}
			///cout<<"shorten"<<res<<endl;
		}
		if(res=="-") {
			count++;
		}
		
		printf("CASE #%d: %d\n",i,count);
	}
	return 0;
}
