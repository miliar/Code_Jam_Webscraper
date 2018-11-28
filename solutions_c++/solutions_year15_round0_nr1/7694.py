#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	int t;
	int n,m;
	//cin>>t;
	int k=t;
	char ch;
	string line,s;
	ifstream file ("A-large.in");
	ofstream f("output.in");
  if (file.is_open())
  {
  	file>>n;
  	m=n;
  	file.get(ch);
    while ( n-- )
    {
    	int c=0,count=0;
    	 file>>t;
    	 k=1;
    	 file.get(ch);
    	 file.get(ch);
    	 count+=ch-48;
    	 
    	 while(t--)
    	 {
    	 	file.get(ch);
			if(count<(k++))
			{
				c++;
				count++;
			}
			count+=ch-48;
    	 }
    	 file.get(ch);
		 f<<"Case #"<<(m-n)<<": "<<c<<endl;
    }
    file.close();
    f.close();
  }
/*	while(t--)
	{
		int count=0,c=0;
		cin>>n;
		m=0;
		char s[n+1];
		cin>>s;
		count+=s[m]-48;
		m++;
		while(m<=n)
		{
			if(count<m)
			{
				c++;
				count++;
			}
			cout<<c<<endl;
			count+=s[m]-48;
			m++;
		}
		cout<<"Case #"<<(k-t)<<": "<<c<<endl;
	}*/
}
