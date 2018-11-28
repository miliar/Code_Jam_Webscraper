#include <cstdio>
#include <cstring>

// for large problem set
const int MAX_COUNT = 10001;

// answer matrix
int mushrooms_in_plate_every_ten_seconds[MAX_COUNT];
int countWaves = 0;

// countTestCases should be less or equal to 100
int countTestCases = 0;

void init() {
    memset(mushrooms_in_plate_every_ten_seconds, 0, sizeof(int) * MAX_COUNT);
}

int solveFirstMethod() {

    int eatMushrooms = 0;

    for (int i = 1; i < countWaves; ++i) {
        if (mushrooms_in_plate_every_ten_seconds[i] < mushrooms_in_plate_every_ten_seconds[i - 1]) {
            eatMushrooms += (mushrooms_in_plate_every_ten_seconds[i - 1] - mushrooms_in_plate_every_ten_seconds[i]);
        }
    }

    return eatMushrooms;
}

int solveSecondMethod() {
    int eatMushrooms = 0;
    int eatPerTenSecond = 0;

    // determine the speed to eat mushrooms
    for (int i = 1; i < countWaves; ++i) {
        if ((mushrooms_in_plate_every_ten_seconds[i - 1] - mushrooms_in_plate_every_ten_seconds[i]) > eatPerTenSecond
        ) {
            eatPerTenSecond = (mushrooms_in_plate_every_ten_seconds[i - 1] - mushrooms_in_plate_every_ten_seconds[i]);
        }
    }

    for (int i = 1; i < countWaves; ++i) {
        if (mushrooms_in_plate_every_ten_seconds[i - 1] > eatPerTenSecond) {
            eatMushrooms += eatPerTenSecond;
        } else {
            eatMushrooms += mushrooms_in_plate_every_ten_seconds[i - 1];
        }
    }

    return eatMushrooms;
}

int main() {

    init();

    scanf("%d", &countTestCases);

    int i = 0;

    for ( ; i < countTestCases; ++i) {

        scanf("%d", &countWaves);
        for (int j = 0; j < countWaves; ++j) {
            scanf("%d", &mushrooms_in_plate_every_ten_seconds[j]);
        }

        int result = solveFirstMethod();
        int result2 = solveSecondMethod();

        printf("Case #%d: %d %d\n", i + 1, result, result2);
    }

    return 0;
}
