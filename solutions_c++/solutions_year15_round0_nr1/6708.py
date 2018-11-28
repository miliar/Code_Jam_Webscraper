#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string prepath = "..\\2015-A\\";
//string test = "test";
//string test = "A-small-attempt0";
string test = "A-large";

struct Item {
    unsigned short price;
    unsigned short index;
    static bool less(const Item &l, const Item &r) {
        return l.price < r.price;
    }
};

int main()
{
    string path = prepath + test + "_out.in";
    FILE *fout = fopen(path.c_str(), "w");
    if (fout == NULL) {
        printf("can not open out\n");
        exit(0);
    }
    fflush(fout);

    path = prepath + test + ".in";
    FILE *fin = fopen(path.c_str(), "r");
    if (fin == NULL) {
        printf("can not open in\n");
        exit(0);
    }

    int problemc;
    int ret = fscanf(fin, "%d", &problemc);
    if (ret != 1) {
        printf("problemc\n");
        exit(0);
    }
    printf("problemc %d\n", problemc);

    for (int n = 0; n < problemc; ++n) {
        int maxlevel;
        ret = fscanf(fin, "%d ", &maxlevel);
        if (ret != 1) {
            printf("maxlevel");
            exit(0);
        }
        printf("maxlevel %d\n", maxlevel);

        //read space
        //fgetc(fin);

        unsigned alreadyStanding = 0;
        unsigned guests = 0;
        for (int i = 0; i <= maxlevel; i++) {
            const char c = fgetc(fin);
            const int num = c -'0';
            if (num < 0 || num > 9) {
                printf("c %d %c\n", num, c);
                char buf[1024];
                fscanf(fin, "%s", buf);
                printf("buf %s\n", buf);
            }
            int needeGuests = i - alreadyStanding;
            if (needeGuests > 0) {
                guests += needeGuests;
                alreadyStanding += needeGuests;
            }
            alreadyStanding += num;
        }

        fprintf(fout, "Case #%d: %u\n", n+1, guests);
    }

    return 0;
}

