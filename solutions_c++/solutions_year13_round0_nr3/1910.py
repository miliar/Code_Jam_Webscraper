#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;

long long pal(long long a);
long long pal(long long a, int i);
bool check(long long n);

int main()
{   
    int T;
	long long A, B;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        ostringstream ss;
        ss << i+1;
        cout<<"Case #"<<ss.str()<<": ";
        
        cin>>A>>B;
        
		long long count = 0;
		if(A == 1)
			++count;
		if(A <= 4 && 4 <=B)
			++count;
		if(A <= 9 && 9 <=B)
			++count;	
		
		for(long long j = 1; ; ++j)
		{
			long long pom = pal(j);
            pom *= pom;
			if(pom > B)
				break;
			if(pom >= A)
			  if(check(pom))
				++count;
				
			for(int k = 0; k < 10; ++k)
			{
				long long pom = pal(j, k);
				pom *= pom;
				if(pom > B)
					break;
				if(pom >= A)
					if(check(pom))
						++count;
			}
		}
        
        cout<<count<<'\n';
    }
    
    
    return 0;   
}

long long pal(long long a)
{
	long long r;
	long long ret = a;
	while(a != 0)
	{
		ret *= 10;
		ret += a%10;
		a/=10;
	}
	return ret;
}

long long pal(long long a, int i)
{
	long long r;
	long long ret = a*10 + i;
	while(a != 0)
	{
		ret *= 10;
		ret += a%10;
		a/=10;
	}
	return ret;
}

bool check(long long n)
{
	stringstream ss;
	ss<<n;
	string pom = ss.str();
	
	int n1 = pom.size();
	for(int i = 0; i < n1/2 ;++i)
		if(pom[i] != pom[n1-1-i])
			return false;
	
	return true;
}
