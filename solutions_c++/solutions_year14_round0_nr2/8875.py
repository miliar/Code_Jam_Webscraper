#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
using namespace std;

double getAns ( double price_Of_Farm, double cookie_Inc, double tot_Cookies)
{
    double bank = 0;
    double curr_Inc = 2;
    double currFastestTime = tot_Cookies / curr_Inc;
    
    while (1)
    {
        double time_test = bank + (price_Of_Farm / curr_Inc) + 
                           (tot_Cookies / (curr_Inc + cookie_Inc));
        
        if ( time_test < currFastestTime)
        {
            currFastestTime = time_test;
            bank = bank + price_Of_Farm / curr_Inc;
            curr_Inc = curr_Inc + cookie_Inc;
        }
        
        else
            break;
    }
    return currFastestTime;
}
            
int main()
{
    int cases;
    
    ifstream read("B-large.in");
    if (!read.is_open())
    {
        cout << "Error opening file" << endl;
        exit(0);
    }
    
    ofstream write("codeout_2_large.txt");
    if (!write.is_open())
    {
        cout << "Error opening file" << endl;
        exit(0);
    }
    
    read >> cases;
    
    for (int i = 0; i < cases; ++i)
    {
        double price_Of_Farm, cookie_Increase , total_Cookies , minTime;
        
        read >> price_Of_Farm;
        read >> cookie_Increase;
        read >> total_Cookies;
        
        minTime = getAns(price_Of_Farm , cookie_Increase , total_Cookies);
        
        write << "Case #" << i+1 << ": " << setprecision(9) << minTime << endl;
    }
    
    read.close();
    write.close();
    
    return 0;
}
    
    
    
    
    
    
    
    
    
    
    
    
    
