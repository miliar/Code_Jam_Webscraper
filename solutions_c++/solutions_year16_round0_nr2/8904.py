#include<bits/stdc++.h>
using namespace std;
string str;
void flip(string str,long long int a)
{ long long int e=0;
      while(e<a)
      {
      	swap(str[e],str[a]);
      	e++;
      	a--;
      }

}
int main()
{long long int q,t,f,i=1,k,j=0;

ifstream infile;
	ofstream outfile;
	infile.open("input.txt",ios::in);
	outfile.open("output.txt",ios::out);
	infile>>t;
	while(t--)
	{k=0;
	infile>>str;
	f=str.length();
	j=f-1;
	while(j>=0)
	{
	if(::str[j]=='-')
	{  k++;q=j;
	while(q>=0)
	{
		if(::str[q]=='-')   
		{::str[q]='+';}
		else
		{
			::str[q]='-';
		}
		q--;}
		flip(::str,j);
	
	}
	else if(::str[j]=='+'){
		j--;
	}
	}
	
		outfile<<"Case #"<<i++<<": "<<k<<endl;



	}outfile.close();
	infile.close();
return 0;}
