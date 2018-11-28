
#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int noofcases, i, n, j ,k, count1=0, count2=0;

    vector<float> vec1, vec2;

    float num;

    freopen("d1.in","r",stdin);
    freopen("d1.out","w",stdout);
    scanf("%d",&noofcases);

    for(i=0; i<noofcases; i++)
    {
        scanf("%d",&n);

        for(j=0; j<n; j++)
        {
            scanf("%f",&num);
            vec1.push_back(num);
        }

        std::sort(vec1.begin(), vec1.end());

        for(j=0; j<n; j++)
        {
            scanf("%f",&num);
            vec2.push_back(num);
        }

        std::sort(vec2.begin(), vec2.end());
        vector <float> vec2copy, vec1copy;
        for(j=0; j<n; j++)
        {
            vec2copy.push_back(vec2[j]);
        }

        for(j=0; j<n; j++)
        {
            vec1copy.push_back(vec1[j]);
        }


        for(j=0; j<n; j++)
        {
            for(k=0; k<n; k++)
            {

                if(vec1[j] > vec2copy[k])
                {
                    vec2copy[k] = 1;
                    vec1[j] = 0;
                    count1++;
                }
            }
        }

        for(j=0; j<n; j++)
        {
            for(k=0; k<n; k++)
            {
                if(vec1copy[j] < vec2[k])
                {
                    vec2[k] = 0;
                    vec1copy[j] = 1;
                    count2++;
                }
            }
        }

        printf("Case #%d: %d %d\n", i+1, count1, n- count2);
        count1 = count2 = 0;
        vec1.clear();
        vec2.clear();
        vec2copy.clear();

    }

return 0;
}
