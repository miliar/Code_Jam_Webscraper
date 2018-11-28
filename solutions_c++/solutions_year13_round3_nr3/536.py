#include <QCoreApplication>
#include <QList>
#include <queue>
using namespace std;

struct Tribe {
    int day;
    int times;
    int west, east;
    int height;
    int deltaDay;
    int deltaEast;
    int deltaHeight;
};

int wall[1000];
bool operator <(Tribe l, Tribe r)
{
    return l.day > r.day;
}

priority_queue<Tribe> tribes;


int main(int argc, char *argv[])
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int caseNumber = 0; caseNumber < T; caseNumber++) {
        memset(wall, 0, sizeof(wall));
        int N;
        scanf("%d", &N);
        while (!tribes.empty())
            tribes.pop();
        for (int i = 0; i < N; i++) {
            Tribe t;
            scanf("%d%d%d%d%d%d%d%d", &t.day, &t.times, &t.west, &t.east, &t.height, &t.deltaDay, &t.deltaEast, &t.deltaHeight);
            tribes.push(t);
        }
        int result = 0;
        while (!tribes.empty()) {
            //printf("%d %d\n", tribes.size(), tribes.top().day);
            int today = tribes.top().day;
            QList<Tribe> todays;
            while (!tribes.empty() && tribes.top().day == today) {
                todays.append(tribes.top());
                tribes.pop();
            }
            foreach (Tribe t, todays)
                for (int i = t.west; i < t.east; i++)
                    if (wall[i + 500] < t.height) {
                        result++;
                        break;
                    }
            foreach (Tribe t, todays) {
                for (int i = t.west; i < t.east; i++)
                    wall[i + 500] = max(t.height, wall[i + 500]);
                t.times--;
                if (t.times > 0) {
                    t.day += t.deltaDay;
                    t.west += t.deltaEast;
                    t.east += t.deltaEast;
                    t.height += t.deltaHeight;
                    tribes.push(t);
                }
            }
        }
        printf("Case #%d: %d\n", caseNumber + 1, result);
    }

}
