#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

int r, t;


long long solve()
{
	ll lr = r;
	ll lt = t;

	ll black = 0;
	while(lt>0){
		
		ll outer_r = lr + 1;
		ll inner_r = lr;

		ll paint_cost = outer_r * outer_r - inner_r * inner_r;

	//	cout<<"1.lt:"<<lt<<",lr:"<<lr<<",black:"<<black<<",cost:"<<paint_cost<<endl;
		if( lt - paint_cost < 0){
			return black;
			break;
		} else {
			black++;
			lt -= paint_cost;
			lr += 2;
		}

	}

	return black;
}

int main()
{
	long long T;

	cin>>T;

	for(long long i=0;i<T;i++){

		long long result=0 ;

		cin >> r >> t;
		
		result = solve();

		cout<<"Case "<<"#"<<i+1<<": "<<result;
		cout<<endl;

	}
	return 0;
}


