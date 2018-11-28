#include<iostream>
#include<string>
#include<fstream>
#include<stack>
using namespace std;
stack<char>s1;
	stack<char>s2;
	int indextobla(string S)//from start
	{
		for(int i=0;i<S.size();i++){
			if(S[i]=='-')
			return i;
		}
	}
	int indextobl(string S)//from end
	{
		for(int i=S.size();i>=0;i--){
			if(S[i]=='-')
			return i;
		}
	}
	char flip(char s)
	{
	if(s=='+')
		return '-';
	else return '+';
	
	}
	void flipandpushs(int count)
	{
		for(int i=0;i<=count;i++){
		s1.push(flip(s2.top()));
		s2.pop();
		}
	
	}
	void entertos1(string S)
{
	for(int i=S.size()-1;i>=0;i--)
	{
	s1.push(S[i]);
	}
}
	string copyfroms2(string S){
	S='\0';
	while(!s2.empty())
	{
		S+=s2.top();
		s2.pop();
	
	
	}
	return S;
	}
	
	void deletes2(){
	while(!s2.empty())
	{
		s2.pop();
	
	
	}
	
	}
	void deletes1(){
	while(!s1.empty())
	{
		s1.pop();
	
	
	}
	
	}
	string copyfroms1(){
	string S1;
	while(!s1.empty())
	{

		S1+=s1.top();
		s1.pop();
	
	
	}
	entertos1(S1);
	return S1;
	}
bool check(string S)
{
	for(int i=0;S[i]!='\0';i++){
	if(S[i]=='-')
		return false;
	}
	return true;

}

void entertos2(string S,int count)
{
	for(int i=0;i<=count;i++){
	s2.push(S[i]);
	s1.pop();
	}
}
bool countblank(string S)
{
int count=0;
for(int i=0;S[i]!='\0';i++){
	if(S[i]=='-')
		count++;

}
if(count>=(S.size()/2))
	return true;
else return false;
}
int main()
{
	
		ifstream fin("B-large.in");
		ofstream fout("output.txt");
	int tc;
	fin>>tc;
	string input;
	int count=0;
	string intermediate;
	int notoflip=0;
	int no_of_pushes=0;
	fin.ignore();
	string prev;
	for(int i=1;i<=tc;i++)
	{
		deletes1();
		deletes2();
		
		getline(fin,input);
		prev=input;
		if(i==45)
			cout<<input;
		entertos1(input);
		no_of_pushes=0;
		//	entertos1(input);
			if(!check(input)){
				entertos2(input,indextobl(input));
				flipandpushs(indextobl(input));
				 input=copyfroms1();
				 if(prev!=input)
					no_of_pushes++;
				 prev=input;
				while(!check(input))
				{
					if(indextobl(input)==0)
					{
					entertos2(input,(indextobla(input)));
					
					flipandpushs((indextobla(input)));
					input=copyfroms1();
					if(prev!=input)
					no_of_pushes++;
					prev=input;
					}
					else
					{
					entertos2(input,(indextobla(input)-1));
					
					flipandpushs((indextobla(input)-1));
					input=copyfroms1();
					if(prev!=input)
					no_of_pushes++;
					prev=input;
					}
				
					if(check(input))
						break;

					entertos2(input,(indextobl(input)));
					flipandpushs(indextobl(input));
					 input=copyfroms1();
					 if(prev!=input)
					no_of_pushes++;	
					 prev=input;
				
				}
			
			}
			fout<<"Case #"<<i<<": "<<no_of_pushes<<endl;
	}

return 0;
}