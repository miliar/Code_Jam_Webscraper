#include <algorithm>

#include <cstdio>

int
main()
{
    int case_count;
    scanf("%d", &case_count);

    for (int case_index = 0; case_index < case_count; case_index++) {
        const double base_production_rate = 2.0;

        double farm_price;
        double farm_production_rate;
        double goal;
        scanf("%lf %lf %lf", &farm_price, &farm_production_rate, &goal);

        double time = 0.0;
        double production_rate = base_production_rate;
        double cookies = 0.0;

        while (cookies < goal) {

            if (cookies >= farm_price) {
                const double new_time_to_goal = (
                    (goal - (cookies - farm_price))
                        / (production_rate + farm_production_rate)
                );
                if (new_time_to_goal < (goal - cookies) / production_rate) {
                    cookies -= farm_price;
                    production_rate += farm_production_rate;
                } else {
                    time += (goal - cookies) / production_rate;
                    break;
                }
            }

            const double timedelta = std::min(
                (goal - cookies) / production_rate,
                (farm_price - cookies) / production_rate
            );
            cookies += timedelta * production_rate;
            time += timedelta;
        }

        printf("Case #%d: %.7lf\n", case_index + 1, time);
    }

    return 0;
}
