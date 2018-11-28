#include <cstdio>
#include <algorithm>

const int MAX_N = 100;
const double EPS9 = 1e-9;
const double EPS14 = 1e-14;

class Source {
public:
    double R; // rate
    double C; // temperature or X

    bool operator < (const Source &arg) const {
        return this->C < arg.C;
    }
};

int T;
int N;
double V, X;
Source sources[MAX_N];

double answer;

int main(void) {
    int t;
    int i;

    // citirea datelor
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d ", &N);
        scanf("%lf %lf", &V, &X);
        for (i = 0; i < N; ++i) {
            scanf("%lf %lf", &sources[i].R, &sources[i].C);
        }

        // calcularea solutiei
        std::sort(sources, sources + N);
        if (sources[0].C <= X && X <= sources[N - 1].C) {
            double heat = 0;
            double volume = 0;
            for (i = 0; i < N; ++i) {
                heat += sources[i].R * sources[i].C;
                volume += sources[i].R;
            }
            double time = V / volume;
            double temperature = heat / volume;
            //printf("Case #%d: time = %lf; temp = %lf\n", t, time, temperature);
            bool reversed;
            if (temperature < X) {
                std::reverse(sources, sources + N);
                reversed = true;
            } else {
                reversed = false;
            }
            double begin = time;
            double end = 1e20;
            while (end - begin > EPS9) {
                double time = (begin + end) / 2;
                double heat = 0;
                double volume = 0;
                for (i = 0; i < N && volume + time * sources[i].R < V; ++i) {
                    heat += time * sources[i].R * sources[i].C;
                    volume += time * sources[i].R;
                }
                if (i < N) {
                    heat += (V - volume) * sources[i].C;
                    volume = V;
                }
                double newTemperature = heat / volume;
                if (reversed != (newTemperature < X) ||
                        (-EPS14 < newTemperature - X && newTemperature - X < EPS14)) {
                    end = time;
                } else {
                    begin = time;
                }
            }
            answer = (begin + end) / 2;

            // afisarea solutiei
            printf("Case #%d: %.9lf\n", t, answer);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
    }
    return 0;
}
