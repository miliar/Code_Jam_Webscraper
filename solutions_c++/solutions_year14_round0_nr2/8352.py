#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>
#include <iomanip>


using namespace std;


void main()
{
	
	std::freopen("output_cookieClicker.txt", "w", stdout);
	ifstream file("B-large.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	
	
	int count;
	
	file>>count;
	
	double C, F, X;
	double rate=2;
	double time=0;
	double cookies=0;
	
	for(int i=0;i<count;i++){

		rate = 2;
		cookies = 0;
		time = 0;

		printf("Case #%d: ",i+1);

		file>>C;
		file>>F;
		file>>X;

		//cout<<setprecision(10)<<" C:"<<setprecision(10)<<C<<" F:"<<setprecision(10)<<F<<" X:"<<setprecision(10)<<X<<endl;

		while (cookies < X){			
			
			if(cookies == C){

				if( ((X-cookies)/rate) < (X/(rate+F)) ){
					time += (X-cookies)/rate;
					cookies = X;
					break;
				}
				else{
					rate += F;
					cookies -= C;
				}				
			}
			else{
				if(C<X){
					cookies += C;
					time += C / rate;
				}
				else{
					cookies = X;
					time += X/rate;
				}

			}
		}

		cout<<setprecision(10)<<time<<endl;
	
	}
}

