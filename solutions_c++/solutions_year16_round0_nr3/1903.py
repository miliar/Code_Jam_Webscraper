#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;


//using namespace std;


string generate_binary(int i)
{
	string s;
	while(i!=0)
	{
		s.append( to_string(i%2) );
		i=i/2;
	}
	//cout<<s.size()<<endl;
	//cout<<7-s.size()<<endl;
	int temp = 14-s.size();
	for(int j=0;j<temp;j++)
	{
		//cout<<"ok"<<endl;
		s.append("0");
	}
	reverse(s.begin(),s.end());
	//cout<<s.size()<<" "<<s<<endl;
	return s;
}

long long int calc(string x,int base)
{
	long long int ans=0;
	long long int num=1;
	for(int i=x.size()-1;i>=0;i--)
	{
		if(x[i]=='1')
			ans+=num;
		num=num*base;
	}

	return ans*base+num*base;
}

int main()
{
	vector< string> arr(501);
	vector< vector<long long int> > arr2(501,vector<long long int> () );
	for(int i=1;i<=500;i++)
	{
		string x = generate_binary(i);
		string s;
		s.append("1");
		s.append( x );
		s.append("11");
		s.append(x);
		s.append("1");

		arr[i]=s;
		arr2[i].push_back( calc(x,2)    +1  );
		arr2[i].push_back( calc(x,3)    +1  );
		arr2[i].push_back( calc(x,4)    +1  );
		arr2[i].push_back( calc(x,5)    +1  );
		arr2[i].push_back( calc(x,6)    +1  );
		arr2[i].push_back( calc(x,7)    +1  );
		arr2[i].push_back( calc(x,8)    +1  );
		arr2[i].push_back( calc(x,9)    +1  );
		arr2[i].push_back( calc(x,10)    +1 );
	}


	ofstream myfile;
 	myfile.open ("output2.txt");
  	
  	myfile<<"Case #1:"<<endl;
  	for(int i=1;i<=500;i++)
  	{
  		myfile<<arr[i]<<" ";
  		for(int j=0;j<9;j++)
  		{
  			myfile<<arr2[i][j]<<" ";
  		}myfile<<endl;
  	}

  	myfile.close();



	return 0;
}