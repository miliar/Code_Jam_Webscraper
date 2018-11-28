#include <bits/stdc++.h>
using namespace std;


long long binarytodecimal(long long arr[],long long N,long long base)
{
	long long res = arr[N-1] ;
	long long var = base ;
	for (long long i = N-2; i >=0; --i)
	{
		res = res + arr[i]*var ;
		var = base*var ;
	}
return res;	
}

long long checkPrime(long long n)
{
	for(long long i=2;i<=sqrt(n)+1;++i)
  	{
      if(n%i==0)
      {
      	return i ;	  
      }
  	}
return 0 ;  	
}

bool validate(long long arr [], long long N,long long divi[])
{
	for (long long i = 2; i <= 10; ++i)
	{
		long long p =  binarytodecimal(arr,N,i);
		long long l = checkPrime(p) ;
		// cout << "L = " << l << endl ;
		if(!l)
		{
			return false ; 
		}
		else
		{
			divi[i-2] = l ;
		}
	}
return true ;	
}

void backtrack(long long arr [], long long N,long long i, vector<string>& res,long long J)
{

	if(res.size()==J) return ;
	if(i==N-1)
	{	
		long long divi[9] ;	
		if(validate(arr,N,divi))
		{
			string s = "" ;
			for (long long j = 0; j < N; ++j)
			{
				char c = arr[j] + '0' ;
				s = s + c ;
			}
			for (long long j = 0; j < 9; ++j)
			{
				// s = s + " " + to_string(divi[j]);
				stringstream ss;
				ss << divi[j];
				string str = ss.str();
				s = s + " " + str ;
			}
			res.push_back(s);
			// cout << s << endl ;	
		} 
		return ;
	}

	arr[i] = 0;
	backtrack(arr,N,i+1,res,J);
	arr[i] = 1;
	backtrack(arr,N,i+1,res,J);
}

int main()
{
	long long T ;
	cin >> T ;
	long long N,J;
	cin >> N >> J;

	// N = 16, J = 50;

	long long arr[N] ;
	fill_n(arr,N,0);
	arr[0] = 1, arr[N-1] = 1 ;

	vector<string> res;
	backtrack(arr,N,1,res,J);

	cout << "Case #1:" << endl ;
	for (long long i = 0; i < res.size(); ++i)
	{
		cout << res[i] << endl ;
	}
}	