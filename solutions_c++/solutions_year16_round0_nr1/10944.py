#include <iostream> 
#include <string>
#include <sstream>
#include <ctime>
using namespace std;


#define MAX_N 1000000
short int mask;
const int half_max = INT_MAX/2;

string num_to_string(int a)
{
	stringstream ss;
	ss << a;
	return ss.str();
}
bool markDigit(string str)
{
	int len = str.length();
	while(len--)
	{
		//cout<<str.at(len);
		mask  = mask | 1 << str.at(len)-'0';
		//map[s] = true;
	}
	//cout<<endl;
	if (mask == 1023)
		return true;
	
	return false;
}

int process(int N)
{
	if(N == 0)
		return -1;
	int count = 1;
	
	while(N < half_max)
	{
		if( markDigit(num_to_string(count++ * N)))
			return (count-1)*N;
	}
	return -1;
}

#define __ATHOME 1

int main()
{
	#if __ATHOME
	double ctime1 = (double)clock() / CLOCKS_PER_SEC, ctime2;
	freopen("competition\\google_code_jam_16_1.txt", "r", stdin);
#endif
	int T,t;
	int N;
	cin >>T;
	for(t = 0; t<T; t++)
	{
		N  = 0;
		mask = 0;
		cin >> N;

		int ans = process(N);
		if(ans == -1)
			cout<<"Case #"<<t + 1<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<t + 1<<": "<<ans<<endl;
        
    }


#if __ATHOME
	ctime2 = (double)clock() / CLOCKS_PER_SEC;
	printf("\n time: %f\n",ctime2 - ctime1);
#endif

    return 0;
}