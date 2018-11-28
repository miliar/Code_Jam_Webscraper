#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <iomanip>

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

double C,F,X;

void printInput()
{
	printf("%f %f %f\n", C,F,X);
}

double solve()
{
	double penalty_recover_time = C/F;

	//printf("p_recover_time = %f\n", penalty_recover_time);

	double cur_time = 0.0;
	double cur_cookie;
	double cur_farm = 0.0;
	if(C < X){
		cur_time += C/2;
		cur_cookie = 2*cur_time;
		while(cur_cookie + penalty_recover_time*(2+ cur_farm*F) <= X ){
		//printf("cur_time=%f, cur_cookie =%f, cur_far= %f\n",cur_time,cur_cookie, cur_farm);
			//buy a farm
			cur_cookie -= C;
			cur_farm += 1.0;
			//move to the time you can buy a farm
			double time_to_buy_farm = C/(2+cur_farm*F);
			cur_cookie += time_to_buy_farm*2;
			cur_cookie += time_to_buy_farm*(F*cur_farm);
			cur_time += time_to_buy_farm;
		}
		double cookie_need = X - cur_cookie;
		double time_need = cookie_need / (2.0 + F*cur_farm);

		//printf("2.cur_time=%f, cur_cookie =%f, cur_far= %f\n",cur_time,cur_cookie, cur_farm);
		//printf("cookie_need =%f , time_need = %f\n",cookie_need, time_need);
		cur_time += time_need;

	}else{
		cur_time = X/2;
	}

	return cur_time;
}

int main()
{
	long long T;

	cin>>T;
	
	for(long long i=0;i<T;i++){

		double result=0 ;
		cin>>C>>F>>X;
		//printInput();
		result=solve();
		//cout<<"Case "<<"#"<<i+1<<": "<< std::setprecision( 6 )<<setfill( '0' )  << result;
		printf("Case #%lld: %.7f",i+1, result);
		cout<<endl;

	}
	return 0;
}


