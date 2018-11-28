#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool isPalindrom(unsigned long long int val)
{
	stringstream streamval;
	streamval<<val;
	string sval = streamval.str();
	size_t sz = sval.size(); 
	if (sz==1) return true;
	bool ok=true;
	size_t i = 0;
	while ((i<sz/2) && ok)
	{
		if (sval.at(i)!=sval.at(sz-i-1)) ok=false;
		i++;
	}
	return ok;


}
        int main()     
	{

		unsigned long long int precalc[48]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004};
		size_t size=48;
/*		unsigned long long int X=1,Y=1000000000000000;
	    unsigned long long int SX=(unsigned long long int)ceil(sqrt((long double)X));
		unsigned long long int SY=(unsigned long long int)floor(sqrt((long double)Y));
		
		#pragma omp parallel num_threads(4)
		for (unsigned long long int i=SX;i<=SY;i++)
		{
		    if (isPalindrom(i) && isPalindrom(i*i)) { precalc[size]=i*i; size++; cout<<i*i<<", ";}
		}
		cout<<"size = "<<size<<endl;
*/

          int T;
          cin>>T;
		  for (int m = 0;m<T;m++)
		  {
			  unsigned long long int A,B;
			  size_t count=0;
			  cin>>A;
		      cin>>B;
			  for (size_t j=0;j<size; j++)
			  {
				  if ((precalc[j]>=A) &&(precalc[j]<=B)) count++;
			  }
			  
		      cout<<"Case #"<<m+1<<": "<<count<<endl;
		  }

          return 0;
      }