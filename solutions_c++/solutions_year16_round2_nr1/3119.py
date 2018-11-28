#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>

#define EQUAL_DOUBLE(a, b) ((std::fabs(((a)) - ((b))) <= 0.00000001))

char eng_names[10][6] = {"ZERO",
                         "ONE",
                         "TWO",
                         "THREE",
                         "FOUR",
                         "FIVE",
                         "SIX",
                         "SEVEN",
                         "EIGHT",
                         "NINE"};
double letter_count[26];
double count_matrix[26][10];
int solution[10];
double working_count_matrix[26][10];

int main(int argc, char **argv)
{
    for (int n = 0; n < 10; n++)
        for (char *p = &eng_names[n][0]; *p; p++)
            count_matrix[(*p) - 'A'][n]++;

    int T;
    scanf("%d", &T);
    getchar();

    for (int t = 1; t <= T; t++)
    {
        memset(letter_count, 0, sizeof(letter_count));

        char c;
        while ((c = getchar()) != '\n')
            letter_count[c - 'A']++;

        memcpy(working_count_matrix, count_matrix, sizeof(count_matrix));
        char flags_set_pivot[26] = {0};

        // for (int r = 0; r < 26; r++)
        // {
        //     for (int c = 0; c < 10; c++)
        //         printf("\t%.3lf", working_count_matrix[r][c]);
        //     printf("\t|\t%.3lf\n", letter_count[r]);
        // }
        for (int pivot_column = 0; pivot_column < 10; pivot_column++)
        {
            int pivot_row;
            for (pivot_row = 0; pivot_row < 26; pivot_row++)
                if (!flags_set_pivot[pivot_row] && !EQUAL_DOUBLE(working_count_matrix[pivot_row][pivot_column], 0.0))
                    break;

            if (pivot_row == 26)
                continue;

            flags_set_pivot[pivot_row] = 1;

            double scale = working_count_matrix[pivot_row][pivot_column];
            for (int column = pivot_column; column < 10; column++)
                working_count_matrix[pivot_row][column] /= scale;
            letter_count[pivot_row] /= scale;

            // printf("pivot (%d, %d)\n", pivot_row, pivot_column);

            for (int eliminating_row = 0; eliminating_row < 26; eliminating_row++)
            {
                if (eliminating_row == pivot_row)
                    continue;

                scale = working_count_matrix[eliminating_row][pivot_column];

                for (int column = pivot_column; column < 10; column++)
                    working_count_matrix[eliminating_row][column] -= scale * working_count_matrix[pivot_row][column];

                letter_count[eliminating_row] -= scale * letter_count[pivot_row];
            }
            // printf("============\n");
            // for (int c = 0; c < 10; c++)
            //     printf("\t%d", c);
            // printf("\n");
            // for (int r = 0; r < 26; r++)
            // {
            //     printf("# %d", r);
            //     for (int c = 0; c < 10; c++)
            //         printf("\t%.3lf", working_count_matrix[r][c]);
            //     printf("\t|\t%.3lf\n", letter_count[r]);
            // }
            // for (int r = 0; r < 26; r++)
            //     if (!EQUAL_DOUBLE(working_count_matrix[r][2] + working_count_matrix[r][4] + working_count_matrix[r][6] + working_count_matrix[r][8], letter_count[r]))
            //     {
            //         printf("wrong row %d\n", r);
            //         return 1;
            //     }

        }

        auto is_zero_row = [](double *ptr) {
            for (double *end = ptr + 10; ptr < end; ptr++)
                if (!EQUAL_DOUBLE(*ptr, 0.0))
                    return false;
            return true;
        };

        for (int row = 0; row < 26; row++)
            if (is_zero_row(&working_count_matrix[row][0]))
                assert(EQUAL_DOUBLE(letter_count[row], 0.0));

        memset(solution, 0, sizeof(solution));

        for (int row = 0; row < 26; row++)
        {
            int column;
            for (column = 0; column < 10; column++)
                if (!EQUAL_DOUBLE(working_count_matrix[row][column], 0.0))
                    break;

            if (column == 10)
                continue;

            solution[column] = (int) std::round(letter_count[row]);
            assert(EQUAL_DOUBLE(solution[column] - letter_count[row], 0.0));
        }

        printf("Case #%d: ", t);
        for (int n = 0; n < 10; n++)
            if (solution[n])
                for (int i = 0; i < solution[n]; i++)
                    printf("%d", n);
        printf("\n");
    }

    return 0;
}
