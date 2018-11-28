#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("inp.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;cin>>t;
    int testcaseno=1;
    while(t--)
    {
        double C,F,X;
        cin>>C>>F>>X;
        double num_cookies_in_hand=0;
        double cur_prod_rate=2;
        double total_time=0;
        while(true)
        {
            double expected_time=X/cur_prod_rate;
            double overhead_time_to_buy=C/cur_prod_rate;
            double new_prod_rate=cur_prod_rate+F;
            double new_time=(expected_time-overhead_time_to_buy);
            double production=new_time*new_prod_rate;
            if(production>X) //you should buy the building
            {
                total_time+=overhead_time_to_buy;
                cur_prod_rate=new_prod_rate;
            }
            else //continue with cur_prod_rate till you have X cookies
            {
                total_time+=expected_time;break;
            }
        }
        cout<<std::fixed<<std::setprecision(7)<<"Case #"<<testcaseno<<": "<<total_time<<endl;
        testcaseno++;
    }
    return 0;
}
