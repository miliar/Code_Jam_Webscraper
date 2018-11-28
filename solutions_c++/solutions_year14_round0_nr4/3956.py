#include<bits/stdc++.h>
#define SIZE 1001
using namespace std;
float naomi[SIZE], ken[SIZE];
int main()
{
    int test, t, n, i, j, deceit_war, war;
    cin>>t;
    for(test=1; test<=t; test++)
    {
        cin>>n;
        deceit_war = war = 0;
        for(i=0; i<n; i++) cin>>naomi[i];
        for(i=0; i<n; i++) cin>>ken[i];
        i = j = 0;
        sort(naomi, naomi+n);
        sort(ken, ken+n);
        for(i=0; i<n; i++)
        {
            if(naomi[i] > ken[j])
            {
                j += 1;
                deceit_war += 1;
            }
        }
        j = 0;
        vector<float> ken_v(ken, ken+n);
        vector<float>::iterator it;
        for(i=0; i<n; i++)
        {
            it = upper_bound(ken_v.begin(), ken_v.end(), naomi[i]);
            if((it-ken_v.begin()) == ken_v.size())
            {
                ken_v.erase(ken_v.begin());
                war += 1;
            }
            else ken_v.erase(ken_v.begin() + (it-ken_v.begin()));
        }
        printf("Case #%d: %d %d\n", test, deceit_war, war);
    }
    return 0;
}
