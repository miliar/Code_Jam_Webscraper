#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int poscheck(string s1)
{
for(int i=0;i<s1.length();i++)
{
	if(s1[i]=='+')
	continue;
	else
	return 0;
}	
return 1;	
}

int negcheck(string s1)
{
for(int i=0;i<s1.length();i++)
{
	if(s1[i]=='-')
	continue;
	else
	return 0;
}
return 1;	
}
int main()
{
ifstream infile;	
infile.open("B-large.in",ios::in);
int t,i,j,k,l;
infile>>t;
int count[t]={0};
string s[t];
for(i=0;i<t;i++)
{
infile>>s[i];	
if(poscheck(s[i]))
{
count[i]=0;
}
else if(negcheck(s[i]))
{
count[i]=1;
}
else
{
int index1,index2=0;
for(j=0;j<s[i].length()-1;j++)
{
cout<<s[i]<<"\n";	
if(s[i][j]==s[i][j+1])
{
continue;
}
else
{	
index2=j;
for(k=index1,l=index2;k<l;k++,l--)
{
char temp=s[i][k];
s[i][k]=s[i][l];
s[i][l]=temp;
}	
for(k=index1;k<=index2;k++)
{
	if(s[i][k]=='+')
	s[i][k]='-';
	else if(s[i][k]=='-')
	s[i][k]='+';
}
count[i]++;
}
	
}


if(negcheck(s[i]))
{
count[i]++;
}


}

}
infile.close();
ofstream outfile;
outfile.open("pancakeoutput.txt",ios::out);
for(i=0;i<t;i++)
{
outfile<<"Case #"<<i+1<<": "<<count[i]<<"\n";	
}
outfile.close();





return 0;
}
