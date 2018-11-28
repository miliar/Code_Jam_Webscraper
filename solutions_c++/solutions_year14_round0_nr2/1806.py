#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	int T,CASES=1;
	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("B-output.out");
	input>>T;
//	cin>>T;
//	cout<<T<<endl;
	while(CASES<=T){
		double C,F,X,cur_cookies=0;
		input>>C>>F>>X;
		//cin>>C>>F>>X;
		double cur_spent_time=0, cur_rate=2;
		while( 1 ){
			if( cur_cookies - C >=0 &&
				(X - (cur_cookies - C))/(cur_rate+F) - (X - cur_cookies)/cur_rate <= 0)
			{
				cur_cookies -= C;
				cur_rate += F;
			}
			else if ( cur_cookies - C >=0 &&
				(X - (cur_cookies - C))/(cur_rate+F) - (X - cur_cookies)/cur_rate > 0)
			{
				cur_spent_time += (X-cur_cookies)/cur_rate;
				break;
			}
			else{
				cur_cookies += C;
				cur_spent_time += C/cur_rate;
			}
		}
		//cout<<cur_spent_time<<endl;
		output<<"Case #"<<CASES<<": "<< std::setprecision(10)<<cur_spent_time<<endl;
		CASES++;
	}
	return 0;
}