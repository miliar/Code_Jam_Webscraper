#include <cstdio>
using namespace std;

const int NB_SHYNESS_LVL_MAX = 1000;

int main(void)
{
    int nb_test;
    int iTest;

    scanf("%d\n", &nb_test);

    for( iTest = 0; iTest < nb_test; ++iTest ) {
        int nb_shyness_lvl;
        int iShyness;
        int nb_people[NB_SHYNESS_LVL_MAX + 1];
        int nb_people_add, nb_people_standing;

        nb_people_add = 0;
        nb_people_standing = 0;

        // Input

        scanf("%d ", &nb_shyness_lvl);

        for( iShyness = 0; iShyness <= nb_shyness_lvl; ++iShyness ) {
            char number;
            scanf("%c", &number);
            nb_people[iShyness] = number - '0';
        }

        scanf("\n");

        // Algorithm

        for( iShyness = 0; iShyness <= nb_shyness_lvl; ++iShyness ) {
            if( nb_people_standing < iShyness ) {
                nb_people_add += (iShyness - nb_people_standing);
                nb_people_standing += (iShyness - nb_people_standing);
            }
            nb_people_standing += nb_people[iShyness];
        }

        // Output

        printf("Case #%d: %d\n", iTest + 1, nb_people_add);
    }

    return 0;
} 
