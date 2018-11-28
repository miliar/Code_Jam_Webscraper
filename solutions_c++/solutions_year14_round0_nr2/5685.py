#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) 
{
    int i;
    int case_no = 0;
    double c, f, x;
    double tot_time, prod_rate;
    double build_cost = 0;
    ifstream fp;

    cout.precision(7);
    cout.setf( std::ios::fixed, std:: ios::floatfield );
    fp.open(argv[1]);
    if(!fp.is_open()) { cout<<"File open error!"<<endl; }
    
    fp>>case_no;
    for( i = 0 ; i < case_no ; i++ ) {

        //parsing 
        fp>>c>>f>>x;
        //cout<<"C="<<c<<" F="<<f<<" X="<<x<<endl;
        
        //initial
        tot_time = 0;
        prod_rate = 2;
        build_cost = c / prod_rate;
        
        //*************************************//
        //Algorithm
        //*************************************//
        for(;;) {
            if( ( x / prod_rate ) >= ( ( x ) / ( prod_rate + f ) + build_cost ) ) {
                tot_time += build_cost ;
                //cout<< c / prod_rate <<endl;
                prod_rate += f;   
                //cout<<"the remain x: "<<x<<endl;
                build_cost = c / prod_rate;
            } else {
                tot_time += x / prod_rate;
                //cout<<"final: "<< x / prod_rate<<endl;
                break;
            }
        }

        //*************************************//
        
        // Report Message
		cout<<"Case #"<<i+1<<": "<<tot_time<<endl;
    }
    
    fp.close();
    return 0;

}
