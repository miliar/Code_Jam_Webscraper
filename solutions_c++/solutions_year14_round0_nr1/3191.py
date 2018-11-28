#include <stdio.h>
#include <set>
using namespace std;

#define ROWS 4

int main()
{
    int round;
    scanf("%d", &round);
    std::set<int> seta;
    std::set<int> setb;
    std::set<int> intersect;
    int count = 1;

    while (count <= round)
    {
        int rowa, rowb;
        int elem;
        seta.clear();
        setb.clear();
        intersect.clear();
        scanf("%d", &rowa);
        for (int i=1; i<=ROWS*ROWS; i++)
        {
            scanf("%d", &elem);
            if ((i > (rowa-1)*ROWS) && (i <= (rowa)* ROWS))
            {
                //printf("%d inserted in a\n", elem);
                seta.insert(elem);
            }
            else
            {
                continue;
            }
        }


        scanf("%d", &rowb);
        for (int i=1; i<=ROWS*ROWS; i++)
        {
            scanf("%d", &elem);
            if ((i > (rowb-1)*ROWS) && (i <= rowb* ROWS))
            {
                //printf("%d inserted in b\n", elem);
                setb.insert(elem);
            }
            else
            {
                continue;
            }
        }

        set_intersection(seta.begin(),seta.end(),setb.begin(),setb.end(),
                                  std::inserter(intersect,intersect.begin()));
        int size = intersect.size();
        if (size == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", count);
        }
        else if (size > 1)
        {
            printf("Case #%d: Bad magician!\n", count);
        }
        else if (size == 1)
        {
            printf("Case #%d: %d\n", count, *intersect.begin());
        }

        count++;
    }
    return 0;
}
