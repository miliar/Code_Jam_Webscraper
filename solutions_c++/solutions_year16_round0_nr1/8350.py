#include<iostream>
#include<stdlib.h>
#include<string>
#include<unistd.h>
#include<sstream>
#include<fstream>

using namespace std;
string process(string s,string arr)
{  
	for(int i=0;i<s.length();i++)
	{
		if(arr[s[i]-48]=='0')
		  arr[s[i]-48]='1';
	}
	return arr;
}

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("result_A_large.txt");
	string temp;
	getline(infile,temp);
	int t=atoi(temp.c_str());
	int counter=0;
	while(t--)
	{
		counter++;
		long long int n,num;
		//cin>>num;
		getline(infile,temp);
		num=atoi(temp.c_str());
		if(num==0)
		{
			outfile<<"Case #"<<counter<<": INSOMNIA"<<"\n";
			continue;
		}
		long long int k=1;
		string arr="0000000000";
		while(1)
		{ 
		    n=num*k;
		    string s;
		  	stringstream ss;
		  	ss<<n;
		  	s=ss.str();
		    arr=process(s,arr);
		    //cout<<endl<<n<<" "<<arr<<endl;
		    if(!arr.compare("1111111111"))
		    	break;
		    k++;
		  }
		 outfile<<"Case #"<<counter<<": "<<n<<"\n";
		 
	}
	return 0;
}
		    
			
