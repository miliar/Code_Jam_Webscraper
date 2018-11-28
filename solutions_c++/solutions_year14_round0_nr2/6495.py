#include <iostream>
#include <iomanip>

using namespace std;

int main()
 {
    int t,tc;
    cin>>t;
    for(tc=1;tc<=t;tc++)
     {
        double c,x,f,rate,temp_t1,temp_t2,t=0,t_rate;
        cin>>c>>f>>x;
        rate=2;
        while(1)
         {
            t_rate=rate;
            temp_t1=c/rate;
            t_rate+=f;
            temp_t1+=x/t_rate;

            temp_t2=x/rate;

            if(temp_t1<temp_t2)
             {
                rate+=f;
                t+=(temp_t1-x/t_rate);
             }
            else
             {
                t+=temp_t2;
                break;
             }

         }
         cout.setf( std::ios::fixed, std:: ios::floatfield );
         cout<<"Case #"<<tc<<": "<<setprecision(7)<<t<<endl;
     }
    return 0;
 }
