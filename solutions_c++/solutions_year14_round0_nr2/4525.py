#include <cstdio>
#include <vector>

using namespace std;

double cookies_per_sec_inc_factor;
double price_of_farm;
double cookies_to_win;

double TimeToFinish (double cookies_per_sec, double time_elapsed)
{
    return time_elapsed + (cookies_to_win / cookies_per_sec);
}

double BuyFarm (double &cookies_per_sec, double &time_elapsed)
{
    time_elapsed += (price_of_farm / cookies_per_sec);
    cookies_per_sec += cookies_per_sec_inc_factor;
    return TimeToFinish(cookies_per_sec, time_elapsed);
}

int main(int argc, char *argv[])
{
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);

    int total_cases;
    scanf("%d", &total_cases);

    for (auto i = 0; i < total_cases; ++i)
    {
        double time_elapsed = 0.0;
        double current_cookies_rate = 2;
        scanf("%lf %lf %lf", &price_of_farm, &cookies_per_sec_inc_factor, &cookies_to_win);
        
        while(1)
        {
            double time_at_current_cookies_per_sec = 
                TimeToFinish(current_cookies_rate, time_elapsed);
            
            double time_if_we_buy_a_farm = 
                BuyFarm(current_cookies_rate, time_elapsed);
 
            if( time_at_current_cookies_per_sec < time_if_we_buy_a_farm)
            {
                printf("Case #%d: %.7lf\n", i+1, time_at_current_cookies_per_sec);
                break;
            }

        }
    
    }
}
