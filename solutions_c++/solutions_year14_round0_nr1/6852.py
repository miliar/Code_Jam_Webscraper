#include <iostream>

#define fo(a,b,c) for(a = (b); a < (c); a++)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))

using namespace std;

int main()
{
    int i, j, k, t, tt;
    int n = 4;
    int x, y, z;

    cin >> tt;

    for(t=1; t<=tt; t++)
    {
        int p[16] = {0};

        cin >> x;
        fi(n) fj(n) 
        {
            cin >> k;
            if(i == x-1) p[k-1]++;
        }

        cin >> y;
        fi(n) fj(n) 
        {
            cin >> k;
            if(i == y-1) p[k-1]++;
        }
        
        int c = 0;
        fi(16) if(p[i] == 2) { c++; z=i+1; }

        printf("Case #%d: ", t);
        switch(c) 
        {
            case 0 : printf("Volunteer cheated!"); break;
            case 1 : cout << z; break;
            default: printf("Bad magician!");
        }

        printf("\n");

    }

    return 0;
}
