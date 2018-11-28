#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int t,smax,i,people,need,counter=1;
char s[1001];
ofstream myfile;
myfile.open("output.txt");
cin>>t;
while(t--)
{
	people=need=0;
	cin>>smax;
	cin>>s;
	for(i=1;i<=smax;i++)
	{	people+=(s[i-1]-'0');
		if(people<i && (s[i]-'0')!=0){ need+=i-people;
					 people+=i-people;
					 }
					 
		if(people>=smax) break;
	
	}
	myfile<<"Case #"<<counter<<": "<<need<<endl;
	counter++;

}
myfile.close();

return 0;}
