#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

#define SIZE 1001
#define WALL_LENGTH 1000
#define POS_SHIFT 250

typedef struct _attack {
    int d;
    int w;
    int e;
    int s;
} ATTACK;

typedef struct _tribe {
    int d;
    int n;
    int w;
    int e;
    int s;
    int delta_d;
    int delta_p;
    int delta_s;
    ATTACK attack;
} TRIBE;

TRIBE tribe[SIZE];
int wall[WALL_LENGTH] = {0};
int wall_mid[WALL_LENGTH] = {0};

void init(int n)
{
    int i;

    for (i = 0; i < WALL_LENGTH; ++i)
    {
        wall[i] = 0;
        wall_mid[i] = 0;
    }

    for (i = 0; i < n; ++i)
    {
        tribe[i].attack.d = tribe[i].d;
        tribe[i].attack.w = tribe[i].w;
        tribe[i].attack.e = tribe[i].e;
        tribe[i].attack.s = tribe[i].s;
    }
}

void update_wall(ATTACK attack)
{    
    int pos_w = attack.w + POS_SHIFT;
    int pos_e = attack.e + POS_SHIFT;

    for (int j = pos_w; j <= pos_e; ++j)
    {
        if (wall[j] < attack.s)
            wall[j] = attack.s;

        if (j != pos_e && wall_mid[j] < attack.s)
        {
            wall_mid[j] = attack.s;
        }
    }
}

void run(int n)
{
    int i;
    int old_day = 0;
    vector<ATTACK> vec_attack;
    int ans = 0;

    init(n);

    while (1)
    {
        int min = 10000000;
        int attack_tribe = -1;

        for (i = 0; i < n; ++i)
        {
            if (tribe[i].n && tribe[i].attack.d < min)
            {
                min = tribe[i].attack.d;
                attack_tribe = i;
            }
        }

        if (attack_tribe == -1)
            break;

        if (tribe[attack_tribe].attack.d != old_day)
        {
//            printf("Update wall. Day %d, %d\n", tribe[attack_tribe].attack.d, old_day);
            
            old_day = tribe[attack_tribe].attack.d;

            for (int i = 0; i < vec_attack.size(); ++i)
                update_wall(vec_attack[i]);

            vec_attack.clear();
        }

        int pos_w = tribe[attack_tribe].attack.w + POS_SHIFT;
        int pos_e = tribe[attack_tribe].attack.e + POS_SHIFT;

        TRIBE t = tribe[attack_tribe];
//        printf("!! %d %d %d %d\n", t.attack.d, t.attack.w, t.attack.e, t.attack.s);

        for (int j = pos_w; j <= pos_e; ++j)
            if (wall[j] < tribe[attack_tribe].attack.s ||
                (j != pos_e && wall_mid[j] < tribe[attack_tribe].attack.s))
            {
//                printf("ATTACK!\n");

                ans++;
                vec_attack.push_back(tribe[attack_tribe].attack);
                break;
            }

        // Update attack tribe
        tribe[attack_tribe].n--;

        if (tribe[attack_tribe].n)
        {
            tribe[attack_tribe].attack.d += tribe[attack_tribe].delta_d;
            tribe[attack_tribe].attack.w += tribe[attack_tribe].delta_p;
            tribe[attack_tribe].attack.e += tribe[attack_tribe].delta_p;
            tribe[attack_tribe].attack.s += tribe[attack_tribe].delta_s;
        }
    }

    for (int i = 0; i < vec_attack.size(); ++i)
        update_wall(vec_attack[i]);

    printf("%d\n", ans);
}

int main()
{
    int num_case;

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        int n;
        scanf("%d", &n);
        for (int j = 0; j < n; ++j)
            scanf("%d %d %d %d %d %d %d %d", &tribe[j].d, &tribe[j].n,
                &tribe[j].w, &tribe[j].e, &tribe[j].s, &tribe[j].delta_d,
                &tribe[j].delta_p, &tribe[j].delta_s);

        printf("Case #%d: ", i);
        run(n);
    }

    return 0;
}
