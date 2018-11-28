#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

int main(void)
{
    int total_dataset_number = 0;

    scanf("%d ", &total_dataset_number);

    int dataset_index = 0;

    while(total_dataset_number--)
    {
        unsigned long long start_radius = 0;
        unsigned long long paint_volume = 0;

        scanf("%llu %llu", &start_radius, &paint_volume);

        unsigned long long required_volume = 0;

        bool not_enough = false;
        unsigned long long drawed_circle = 0;

        unsigned long long i = start_radius;

        unsigned long long limit = paint_volume / 2;

        while(1)
        {

            if (i > paint_volume)
                break;

            required_volume += 2 * i + 1;

            if (required_volume > paint_volume)
            {
                not_enough = true;
                break;
            }

            drawed_circle++;
            i += 2;
        }

        printf("Case #%d: %llu\n", ++dataset_index, drawed_circle);

    }
    return 0;
}
