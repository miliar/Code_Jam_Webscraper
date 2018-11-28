#include <stdio.h>

FILE* in;

double C, F, X;
double time[100000];

void work() {
    fscanf(in, "%lf %lf %lf", &C, &F, &X);
    double max_time = X / 2;
    time[0] = 0;
    int num = 0;
    for (int i=1; i<X; ++i) {
        num++;
        double speed = 2 + (i-1)*F;
        time[i] = time[i-1] + C / speed;
        if (time[i] > max_time) {
            break;
        }
    }
    double min = X / 2;
    for (int i=0; i<=num; ++i) {
        double speed = 2 + i*F;
        double total = time[i] + X / speed;
        if (total < min) {
            min = total;
        }
    }
    printf("%.07lf\n", min);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Argument wrong!\n");
        return 0;
    }

    int T;
    in = fopen(argv[1], "r");
    fscanf(in, "%d", &T);
    for (int t=0; t<T; ++t) {
        printf("Case #%d: ", t+1);
        work();
    }

    fclose(in);
    return 0;
}
