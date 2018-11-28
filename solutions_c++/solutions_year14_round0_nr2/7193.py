#include <iostream>
#include <cstdlib> // for atoi
#include <iomanip>
using namespace std;
int main(){
int testCase;	
double cost;
double farm;
double xCookies;
double cookiePerTime;
double totalTime;
double farmTime;
double xCookieTimeOne;
double xCookieTimeTwo;



cin>> testCase;

for(int i = 1; i<=testCase; i++){
	cookiePerTime = 2.0;
	cin>>cost>>farm>>xCookies;

	xCookieTimeOne = xCookies/cookiePerTime;
	farmTime = cost/cookiePerTime;
	cookiePerTime=cookiePerTime+farm;
	xCookieTimeTwo = xCookies/cookiePerTime;
	totalTime=xCookieTimeTwo+farmTime;

	if(xCookieTimeOne <= totalTime){
		totalTime = xCookieTimeOne;
		cout<<"Case #"<<i<<": ";
		std::cout << std::setprecision(10) << totalTime<<endl;
	}else{
		
		while(xCookieTimeOne > totalTime){
			xCookieTimeOne = totalTime;
			
			farmTime=farmTime+(cost/cookiePerTime);
			cookiePerTime = cookiePerTime+farm;
			xCookieTimeTwo = xCookies/cookiePerTime;
			totalTime=xCookieTimeTwo+farmTime;
			

		}
		cout<<"Case #"<<i<<": ";
		std::cout << std::setprecision(13) << xCookieTimeOne<<endl;
	}
	

}

return 0;
}
