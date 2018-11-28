#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

#define SMALL
void setInputOutputStreams()
{
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif

#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
}

long double MIN_NUMBER = 1;
long double MAX_NUMBER = 100000000000000;

long long revertLong(long long num){	
	long long r = 0;
	long long sum = 0;
	
    while(num){
         r=num%10;
         num=num/10;
         sum=sum*10+r;
    }
	return sum;
}

bool isLongPalindrom(long long number){
	return (number == revertLong(number));
}

void prepareCache(vector<int> *cache){
	long aSqrt = ceil(sqrt(MIN_NUMBER));
	long  bSqrt = floor(sqrt(MAX_NUMBER));		

	for(int i = aSqrt ; i <= bSqrt ; i++)
	{
		long long pow = i*i;
			
		if(isLongPalindrom(i) && isLongPalindrom(pow))
			(*cache).push_back(i);
	}			
}

int fairSquareNumber(vector<int> &cache , long aSqrt, long bSqrt) {
	int sum = 0;
	
	for(int i = 0 ; i< cache.size() ; i++){

		int val = cache.at(i);

		if( val >= aSqrt && val <= bSqrt){
			sum++;
		}
	}

	return sum;
}

int main(int argc, char* argv[])
{
	setInputOutputStreams();
	
	vector<int> cache;	

	int T = 0;	
	long double A = 0;
	long double B = 0;

	long aSqrt = 0;
	long bSqrt = 0;
	cin >> T;
	

	prepareCache(&cache);

	for(int t = 0 ; t < T ; t++) {
		cin >> A >> B;				
		
		aSqrt = ceil(sqrt(A));
		bSqrt = floor(sqrt(B));				

		cout<<"Case #"<<t+1<<": "<<fairSquareNumber(cache,aSqrt,bSqrt)<<endl;		
	}
	
	return 0;
}

