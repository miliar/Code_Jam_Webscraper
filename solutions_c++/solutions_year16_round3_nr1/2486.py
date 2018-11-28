#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<algorithm>
using namespace std;

bool finished = false;

inline bool isFinsihed(vector<int>& P)
{
    for(int i=0;i<P.size();++i)
    {
        if(P[i]!=0)
            return false;
    }
    return true;
}

inline bool balanced(vector<int>& P)
{
    int sum = 0;
    int N = 0;
    for(int i=0;i<P.size();++i)
    {
        sum+=P[i];
        if(P[i]>0)
            N++;
    }

    for(int i=0;i<P.size();++i)
    {
        if(P[i]*2 > sum)
            return false;
    }
    return true;
}

void dfs(vector<int>& P, vector<string>& steps)
{
    if(finished==true)
        return;
    
    if(isFinsihed(P))
    {
        for(int i=0;i<steps.size();++i)
        {
            printf(" %s", steps[i].c_str());
        }
        printf("\n");
        finished=true;
        return;
    }

    string step;
    for(int i=0;i<P.size();++i)
    {
        if(P[i]<1)
            continue;
        for(int j=i;j<P.size();++j)
        {
            bool fillBack=false;
            step="";
            step +=(char)('A'+i);
            P[i]--;
            if(P[j]>0)
            {
                step+=(char)('A'+j);
                P[j]--;
                fillBack=true;
            }
            if(balanced(P))
            {
                steps.push_back(step);
                //printf("%s\n", step.c_str());
                dfs(P, steps);
                steps.pop_back();
            }
            
            if(fillBack)
            {
                P[j]++;
            }
            P[i]++;
        }
    }    
}

void MaxTwo(vector<int>&P, int& first, int& second)
{    
    int max = 0;
    for(int i=0;i<P.size();++i)
    {
        if(P[i] > max)
        {
            max = P[i];
            first = i;
        }        
    }

    max = 0;
    for(int i=0;i<P.size();++i)
    {
        if(i==first) continue;
        if(P[i] > max)
        {
            max = P[i];
            second = i;
        }        
    }
}

void regular(vector<int>& P)
{
    while(!isFinsihed(P))
    {
        int f=0,s=0;
        MaxTwo(P, f, s);
        P[f]--;
        P[s]--;
        if(balanced(P))
        {
            printf(" %c%c", 'A'+f, 'A'+s);
        }        
        else
        {
            P[s]++;
            P[f]--;
            if(balanced(P))
            {
                printf(" %c%c", 'A'+f, 'A'+f);
            }
            else
            {
                P[f]++;
                printf(" %c", 'A'+f);
            }
        }
    }
    printf("\n");
}

int main()
{
    int T, N, temp;
    vector<int> P;
    scanf("%d", &T);
    
    for(int i=1;i<T+1;++i)
    {
        scanf("%d", &N);
        P.clear();
        for(int j=0;j<N;++j)
        {
            scanf("%d", &temp);
            P.push_back(temp);
        }

        // for(int j=0;j<N;++j)
        //     printf(" %d", P[j]);
        // printf("\n");
        printf("Case #%d:", i);
        vector<string> steps;
        finished = false;
        //dfs(P, steps);
        regular(P);
    }
    return 0;
}

