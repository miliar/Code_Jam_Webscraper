#include "math.h"
#include "stdio.h"

char grid[100][100];
int wd, ht;


// [
//     [. . . . .],
//     [. . . . .]
// ]
int cardinal_x[]{1,-1,0,0};
int cardinal_y[]{0,0,1,-1};
// do we hit anything after the start
bool hit(int y, int x, int cardinal) {
    int dy = cardinal_y[cardinal];
    int dx = cardinal_x[cardinal];

    // ignore start
    x += dx;
    y += dy;

    while (
        x >= 0 && y >= 0 &&
        x < wd && y < ht
    ) {
        if (grid[y][x] != '.') {
            return true;
        }

        x += dx;
        y += dy;
    }
    return false; // we hit the edge: no hit
}


int change(int y, int x) {
    int cardinal;
    switch (grid[y][x]) {
        case '.': return 0; // no change
        case '>': cardinal = 0; break;
        case '<': cardinal = 1; break;
        case 'v': cardinal = 2; break;
        case '^': cardinal = 3; break;
        default:
            printf("bad char: %c\n", grid[y][x]);
            throw "bad char: " + grid[y][x];
    }

    // we found another one: no cange
    if (hit(y,x, cardinal)) {
        return 0;
    }

    for (int c=0; c<4; ++c) {
        if (c==cardinal) {
            continue;
        }

        if (hit(y,x, c)) {
            return 1;  // we'd need to change this one
        }
    }

    return -1;  // we always hit a side: impossible
}

int main(int argc, char const *argv[])
{
    int numCases = 0;
    scanf("%d", &numCases);


    for (int caseNum=0; caseNum<numCases; ++caseNum) {
        scanf("%d %d\n", &ht, &wd);
        for (int y=0; y<ht; ++y) {
            for (int x=0; x<wd; ++x) {
                grid[y][x] = getchar();
            }
            getchar(); // '\n'
        }

        bool impossible=false;
        int numChange = 0;
        for (int y=0; y<ht && !impossible; ++y) {
            for (int x=0; x<wd; ++x) {
                int haschange = change(y,x);
                if (haschange < 0) {
                    impossible = true;
                    break;
                }
                numChange += haschange;
                //printf("%c", grid[y][x]);
            }
            // printf("\n");
        }

        if (impossible) {
            printf("Case #%d: %s\n", caseNum+1, "IMPOSSIBLE");
        }
        else {
            printf("Case #%d: %d\n", caseNum+1, numChange);
        }
    }


    return 0;
}
