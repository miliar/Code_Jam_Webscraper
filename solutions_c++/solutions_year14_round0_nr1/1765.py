#include <cstdio>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int p;
        scanf("%d",&p);
        vector <int> a;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                if (i==p)
                    a.push_back(x);
            }
        scanf("%d",&p);
        vector <int> b;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                if (i==p)
                    b.push_back(x);
            }
        vector <int> c;
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        set_intersection(a.begin(),a.end(),b.begin(),b.end(),back_insert_iterator <vector <int> >(c));
        static int id=0;
        printf("Case #%d: ",++id);
        if (c.size()==1)
            printf("%d\n",c[0]);
        else if (c.empty())
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return(0);
}

