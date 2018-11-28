#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int main ()
{
    int numberOfTestCases;
    scanf("%d", &numberOfTestCases);

    for (int testCase = 0; testCase < numberOfTestCases; testCase++)
    {
        int firstRow, secondRow;
        set <int> firstSet, secondSet;

        scanf("%d",&firstRow);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                int x;
                scanf("%d", &x);
                if(i+1 == firstRow)
                {
                    firstSet.insert(x);
                }
            }
        }

        scanf("%d",&secondRow);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                int x;
                scanf("%d", &x);
                if(i+1 == secondRow)
                {
                    secondSet.insert(x);
                }
            }
        }
        int count = 0, element;

        for (auto el : firstSet)
        {
            int x = secondSet.count(el);
            if (x) element = el;
            count += secondSet.count(el);
        }

        printf ("Case #%d: ", testCase + 1);
        if (count > 1)
        {
            printf ("Bad magician!\n");
        }
        else if (count == 1)
        {
            printf ("%d\n", element);
        }
        else
        {
            printf ("Volunteer cheated!\n");
        }
    }
}
