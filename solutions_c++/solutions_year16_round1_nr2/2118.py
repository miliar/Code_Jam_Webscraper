#include <iostream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <list>
#include <unordered_map>

using namespace std;

int main()
{
    FILE* in, *out;
    if((in=fopen("B-large.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("B-large.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        int n;
        fscanf(in, "%d", &n);

        vector<list<int> > heights(2*n-1);
        for(int i=0; i<2*n-1; ++i)
        {
            heights[i].resize(0);
            for(int j=0; j<n; ++j)
            {
                int next;
                fscanf(in, "%d", &next);
                heights[i].push_back(next);
            }
        }

        list<int> solution;
        for(int i=0; i<n; ++i)
        {
            //select first row and column
            int min1=0, min2=-1;
            for(int j=1; j<2*n-1; ++j)
            {
                if(heights[j].front()<heights[min1].front())
                {
                    min2=min1;
                    min1=j;
                }
                else if(min2==-1 || heights[j].front()<heights[min2].front())
                    min2=j;
            }

            unordered_map<int,int> occurs;

            //cout<<min1<<" "<<min2<<endl;
            //cout<<heights[min1].front()<<" "<<heights[min2].front()<<endl;

            if(heights[min1].front()==heights[min2].front())
            {
                list<int>::iterator it;
                for (it = heights[min1].begin(); it != heights[min1].end(); ++it)
                {
                    int value=*it;
                    unordered_map<int,int>::const_iterator isInside = occurs.find (value);
                    if(isInside == occurs.end())
                        occurs[value]=1;
                    else
                        ++occurs[value];
                }
                for (it = heights[min2].begin(); it != heights[min2].end(); ++it)
                {
                    int value=*it;
                    unordered_map<int,int>::const_iterator isInside = occurs.find (value);
                    if(isInside == occurs.end())
                        occurs[value]=1;
                    else
                        ++occurs[value];
                }

                for(int j=0; j<2*n-1; ++j)
                {
                    if(heights[j].front()>2500)
                        continue;

                    --occurs[heights[j].front()];
                    heights[j].pop_front();
                }

                heights[min1].push_front(2600);
                heights[min2].push_front(2600);

                unordered_map<int,int>::const_iterator iter;
                for (iter = occurs.begin(); iter != occurs.end(); ++iter )
                {
                    if(iter->second>0)
                    {
                        solution.push_back(iter->first);
                        break;
                    }
                }
            }
            else
            {
                vector<int> missing;
                missing.push_back(heights[min1].front());

                list<int>::iterator it;
                for (it = heights[min1].begin(); it != heights[min1].end(); ++it)
                {
                    int value=*it;
                    unordered_map<int,int>::const_iterator isInside = occurs.find (value);
                    if(isInside == occurs.end())
                        occurs[value]=1;
                    else
                        ++occurs[value];
                }

                for(int j=0; j<2*n-1; ++j)
                {
                    if(heights[j].front()>2500)
                        continue;

                    int value=heights[j].front();
                    unordered_map<int,int>::const_iterator isInside = occurs.find (value);

                    if(isInside == occurs.end())
                        missing.push_back(value);
                    else
                    {
                        if(occurs[value]>0)
                            --occurs[value];
                        else
                            missing.push_back(value);
                    }
                }

                sort(missing.begin(), missing.end());
                for(int j=0; j<missing.size(); ++j)
                    solution.push_back(missing[j]);

                break;
            }

        }

        fprintf(out, "Case #%d: ", t+1);
        list<int>::iterator it;
        for (it = solution.begin(); it != solution.end(); ++it)
            fprintf(out, "%d ", *it);

        fprintf(out, "\n");

    }


    fclose(in);
    fclose(out);
    return 0;
}
