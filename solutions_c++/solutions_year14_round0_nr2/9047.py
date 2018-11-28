#include <iostream>
#include <chrono>
#include <ctime>
#include <limits>
#include <cmath> 
#include <iomanip>
using namespace std;


bool AreDoubleSame(double dFirstVal, double dSecondVal)
{
    return std::abs(dFirstVal - dSecondVal) < std::numeric_limits<double>::epsilon();
}

int main() {

    long double C = 0;
    long double F = 0;
    long double X = 0;

    int cases = 0;
    cin >> cases;
    int d = cases;
    long double result = 0;
    //clock_t c_start = std::clock(); 
     
    while (cases) {
//	auto t_end = std::chrono::high_resolution_clock::now(); 
/*	 std::cout << "Wall clock time passed: "
              << std::chrono::duration_cast<std::chrono::seconds>(t_end - t_start).count()
              << " ms\n";
*/
	--cases;
	
	cin >> C;
	cin >> F;
	cin >> X;
	result = 0.0;
	long double cookies = 0.0;
	bool flag = true;
	bool flag_in = false;
	long double cur_rate = 2.0;
	auto  t_start = std::chrono::high_resolution_clock::now(); 
	auto  t_end1 = std::chrono::high_resolution_clock::now(); 
	
	while (cookies < X) {
	    //while(!(AreDoubleSame(cookies, C)) && (cookies < X))  {
	   // while((!(cookies <  C) && (cookies < X) ) || !(flag))  {
/*	      while(true) {
		if(flag)
		    t_start = std::chrono::high_resolution_clock::now(); 
		 flag = false;
		 t_end1 = std::chrono::high_resolution_clock::now();
	 
		cookies = cur_rate * (std::chrono::duration_cast<std::chrono::milliseconds>(t_end1 - t_start).count())/1000;
	//	cookies = cur_rate * (std::chrono::duration_cast<std::chrono::seconds>(t_end1 - t_start).count());
		if(((cookies > C) && !flag_in) ||( (cookies > X)))
		    break;
		//cookies = cur_rate * (std::chrono::duration_cast<std::chrono::seconds>(t_end1 - t_start).count());
		cout <<"here1=>"<< cookies<< " rate = " << cur_rate<<endl;
	    }
	   */
	    
	    long double time_req_C = C/cur_rate;
	    if(!flag_in){
	//	cout << "here\n";
		if( X < C){
		    cookies = X;
		}
		else 	
		    cookies = C;
	    }	
	    else{
		long double left = X - cookies;
		if( left > C) 
		    cookies += C;
		else 
		    cookies += left;
		if(cookies > X)
		    break;
	    } 
		
	     
	    //auto t_s = std::chrono::high_resolution_clock::now(); 
	    if(!(cookies < C)){
	      //if(AreDoubleSame(cookies, C)){
	//	auto t_start2 = std::chrono::high_resolution_clock::now(); 
	//	cout << "cookies == C\n";
		long double new_rate = cur_rate + F;
	        long double new_time_req = X / new_rate;
	        
		long double old_time_req = (X - cookies)/cur_rate;
		flag_in = true;
		if((old_time_req > new_time_req) && (cookies < X)){
		    result += (long double)(cookies/cur_rate);
		    cur_rate = new_rate;
		    cookies = 0.0;
		    flag_in = false;
		    //result += //(std::chrono::duration_cast<std::chrono::nanoseconds>(t_end1 - t_start).count())/1000000000;
		 //   cout << "resultinside  =" << result << endl; 
		    flag = true;

		}
	      //auto t_e = std::chrono::high_resolution_clock::now(); 
		
		//t_start = t_s
		
	    }
	    //auto t_end2 = std::chrono::high_resolution_clock::now(); 
	    //cookies = cookies + cur_rate * std::chrono::duration_cast<std::chrono::seconds>(t_end2 - t_start2).count()

	}
        //result += (std::chrono::duration_cast<std::chrono::nanoseconds>(t_end1 - t_start).count())/1000000000;
	result += (long double)(cookies/cur_rate);
	cout << "Case #"<< d - cases << ": " <<  std::setprecision(10) << result << endl;
	//cout << "Case #"<< d - cases << ": "  << result << endl;
	//auto t_end = std::chrono::high_resolution_clock::now(); 
	//cookies 
    

    }
 

}
