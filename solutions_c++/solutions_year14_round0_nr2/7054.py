#include <iostream>
#include <cstdio>
#include <string.h>


using namespace std;
//**** Declare your data ********


double cost_farm=0;
double rate_inc=0;
double max2win=0;
double winTime=0;


// **** Initialize your data
void initialize()
{
	cost_farm = rate_inc = max2win = 0;
	// emptysq = 0;

};
// *** Solver function
double run()	
{
	cin>>cost_farm;
	cin>>rate_inc;
	cin>>max2win;

	
	// cout<<"farm cost = "<<cost_farm<<endl;
	// cout<<"inc in cookie rate = "<<rate_inc<<endl;
	// cout<<"cookie to win = "<<max2win<<endl;



	int Farms=0;
	double Farms_buy_time=0;
	double Curr_cookie_rate=2.0;
	double total_time_0=0;
	double total_time_1=0;

	total_time_0 = max2win/Curr_cookie_rate + Farms_buy_time;
	while(true)
	{
		// Previous win time
		
		// win time if we buy new farm
		total_time_1 = max2win/(Curr_cookie_rate + rate_inc) + Farms_buy_time + (cost_farm/Curr_cookie_rate) ;

		// cout<<" \nFarm count = "<<Farms;
		// cout<<"\n total_time_0 = "<<total_time_0;
		// cout<<"\n total_time_1 = "<<total_time_1;
		// cout<<"\n Farms_buy_time = "<<Farms_buy_time;
		// cout<<"\n Curr_cookie_rate = "<<Curr_cookie_rate;
		// cout<<"\n new farm buy cost = "<<cost_farm/Curr_cookie_rate<<endl;

		if(total_time_0<total_time_1) 
			return total_time_0;
		Farms++;
		Farms_buy_time += cost_farm/Curr_cookie_rate;
		Curr_cookie_rate += rate_inc;
		total_time_0 = total_time_1;

	}
	
	return 0;
	
}
void solve_case(int test_case)
{
	initialize();

	// **** call solver function
	// cout<<"\n\n/*********test case------"<<test_case<<endl;
	winTime = run();
	
	// *** print output
	cout<<"Case #"<<test_case<<": "<<winTime<<endl;
	// if(card==0)
	// 	cout<<"Case #"<<test_case<<": "<<"Volunteer cheated!"<<endl;
	// else if(card>16)
	// 	cout<<"Case #"<<test_case<<": "<<"Bad magician!"<<endl;
	// else 
	// 	cout<<"Case #"<<test_case<<": "<<card<<endl;
	// 	return;


};

int main()
{
	freopen("bbb.in","r",stdin);
	freopen("b.out","w",stdout);
	initialize();
	int T; scanf("%d", &T);

	cout.setf(ios::fixed, ios::floatfield );
	cout.precision(7);
	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}
