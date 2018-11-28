#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

main()
{
    int i,j,k;

    int t;

    FILE *in = fopen("A.in","r");
    FILE *out = fopen("A.out","w");

    fscanf(in,"%d",&t);
    vector<int> S1;
    vector<int> S2;
    vector<int> v;


    for (k=1;k<=t;k++) {
        int l;

        S1.clear();
        S2.clear();
        v.resize(10);

        fscanf(in,"%d",&l);
        for (i=0;i<16;i++) {
            fscanf(in,"%d",&j);
            if (i/4+1==l)
                S1.push_back(j);
        }

        fscanf(in,"%d",&l);
        for (i=0;i<16;i++) {
            fscanf(in,"%d",&j);
            if (i/4+1==l)
                S2.push_back(j);
        }
        sort(S1.begin(),S1.end());
        sort(S2.begin(),S2.end());
        v.resize(set_intersection(S1.begin(),S1.end(),S2.begin(),S2.end(),v.begin())-v.begin());
        if (v.size()==0)
            fprintf(out,"Case #%d: Volunteer cheated!\n",k);
        if (v.size()>1)
            fprintf(out,"Case #%d: Bad magician!\n",k);
        if (v.size()==1)
            fprintf(out,"Case #%d: %d\n",k,v[0]);
    }
}
