#include<iostream>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<map>
using namespace std;



bool IsPalDeQueue(unsigned long long X)
{
	
	
	deque<unsigned long long> D;


	
	while ( X > 0)
	{
		D.push_front(X%10);
		X=X/10;
	}
	
	while(D.size() > 0)
	{
		if (D.front() == D.back())
		{
			D.pop_back();
			if ( !D.empty())
			D.pop_front();
		}
		else
			return false;
	}
//	cout<<Xbar<<endl;
	return true;
}
unsigned long long ApproxSqrt(unsigned long long N)
{
	double X = 100;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	X = ((N/X) +X)/2;
	return (unsigned long long)X;
}



static vector<unsigned long long > V;
unsigned long long Preprocess()
{
		unsigned long long 	count =0;


		for (unsigned long long i = 0 ; i*i <= 100000000000000; i++)
	{

		if (  IsPalDeQueue( i) && IsPalDeQueue( i*i))
		{
			V.push_back(i*i);
		//	cout<<"Fair and Square"<<i<<" "<<i*i<<endl;
			
		}
		
	}
	return count;
}
unsigned long long Query(unsigned long long A ,unsigned long long B)
{
	unsigned long long count=0; 
	if ( V.size() > 0)
	{
		for (int i = 0; i < V.size(); i++)
		{
			if (V[i] >= A && V[i] <= B)
			{
				count++;
			}

		}
	}
	return count;
}

unsigned long long RunSmall(unsigned long long A ,unsigned long long B)
{
		unsigned long long 	count =0;

		for (unsigned long long i = ApproxSqrt( A) ; i*i <= B; i++)
	{

		if ( i*i >= A && IsPalDeQueue( i) && IsPalDeQueue( i*i))
		{
			//cout<<"Fair and Square"<<i<<" "<<i*i<<endl;
			count++;
		}
		
	}
	return count;
}



int main ()
{

	//cout<<ApproxSqrt(100);
	freopen("C-large-1.in","r",stdin);
	freopen("output_Large.txt","w",stdout);
	unsigned long long T;
	cin>>T;
	Preprocess();

	for (int i = 0; i < T; i++)
	{
		unsigned long long A=0, B=0;
		cin>>A>>B;
		
		cout<<"Case #"<<i+1<<": "<<Query(A,B)<<endl;
	}
	
}
