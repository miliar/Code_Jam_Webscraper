#include "iostream"

using namespace std;

 

double cost_time(double c, double f, double x){
	double time_farm = 0; 
	double cur_rate = 2;
	while( x/cur_rate > c / cur_rate + x/ (cur_rate + f))
	{
		time_farm += c/cur_rate;
		cur_rate = cur_rate + f;
	//	printf("%.7lf\n", time_farm);
	}
	time_farm += x / cur_rate;
	return time_farm;
}
void read_process(int order){
	double c,f,x, mytime = 0;
	cin>> c >> f >> x;
	mytime = cost_time(c,f,x);
	printf("Case #%d: %.7lf\n", order , mytime);
}
int main(){
	int test_num = 0;
	cin>>test_num;
	for(int i= 0 ; i< test_num; i++)
	read_process(i+1);

}