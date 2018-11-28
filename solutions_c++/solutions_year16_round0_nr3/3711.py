#include<bits/stdc++.h>
#include<math.h>
using namespace std;

#define LL long long int 

int isValid(string str)
{

	vector<long long>vt;
	//cout<<str<<endl;
	for(int base=2;base<=10;base++)
	{

		long long  number = 0;
		long long  prod= 1;

		for(int i= str.size()-1;i>=0;i--)
		{

			number += ( long long ) (str[i]-'0')*prod;
			prod=prod*base;
			//cout<<"prod="<<prod;
		}
		
		long long num_sqrt=(long long)sqrt(number);
		//cout<<"base="<<base<<"number="<<number<<"root="<<num_sqrt;

		//cout<<"number="<<number<<"root="<<num_sqrt<<endl;
		int  flag=0;
		for(long long int  j=2;j<= num_sqrt ; j++)
		{
			if(number % j == 0)
			{
				vt.push_back(j);
				//cout<<"value";
				flag=1;
				break;
			}

		}
		if(flag==0)
		{
			//cout<<"came here"<<endl;
			return 0;
		}

	}

	cout<<str<<" ";
	int size1=9;
	for(int i=0;i<size1;i++)
	{
		cout<<vt[i];
		if(i!=(size1-1))
			cout<<" ";
	}
	cout<<endl;

	return 1;
}


void coinJam(int N,int J,int i, string &soln, int &count)
{
	if(count==J)
		return;
	else if(i==1)
	{
		soln.push_back('1');
		coinJam(N,J,i+1,soln,count);

	}
	else if(i== N)
	{
		soln.push_back('1');
		//cout<<soln<<endl;
		if(isValid(soln))
			{
				count=count+1;
			}	
		soln.erase(soln.size()-1);
	}

	else
	{
		soln.push_back('0');
		coinJam(N,J,i+1,soln,count);
		soln.erase(soln.size()-1);

		soln.push_back('1');
		coinJam(N,J,i+1,soln,count);
		soln.erase(soln.size()-1);

	}

}

int main()
{

	int T;
	cin>>T;

	for(int i=1;i<T+1;i++)
	{
		int N,J;
		cin>>N;
		cin>>J;

		string soln;
		int count=0;
		cout<<"Case #"<<i<<":"<<endl;
		coinJam(N,J,1,soln,count);
	}

return 0;
}







