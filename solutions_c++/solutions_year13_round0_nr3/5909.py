#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <set>

using namespace std;


int main(int argc, char* argv[])
{
    if (argc != 2)
        return 1;

    set<int> lookup;
    lookup.insert(1);
    lookup.insert(4);
    lookup.insert(9);
    lookup.insert(121);
    lookup.insert(484);

    FILE* fp = fopen(argv[1], "r");
    if (!fp)
        return 2;

    int T, A, B, t;
    fscanf(fp, "%d", &T);
    t = T;
    while (t-- > 0)
    {
        set<int> tmpset(lookup);
        fscanf(fp, "%d %d", &A, &B);
        set<int>::iterator it = tmpset.lower_bound(A);
        if (it != tmpset.begin())
            tmpset.erase(tmpset.begin(), it);
        set<int>::iterator it2 = tmpset.upper_bound(B);
        tmpset.erase(it2, tmpset.end());
        printf("Case #%d: %d", T-t, tmpset.size());
        if (t>0)
            printf("\n");
    }
     
    fclose(fp);
    return 0;
}

