#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int War(vector<float> Naomi, vector<float> Ken);
int Deceitful_War(vector<float> Naomi, vector<float> Ken);

int main()
{
    int T,N;
    int caseNum=1;
    int d_W,W;
    freopen("D-large.in", "r", stdin);
    freopen("PD_large.out", "w", stdout);
    scanf("%d", &T);

    while(caseNum <= T)
    {
        vector<float> Naomi;
        vector<float> Ken;
        scanf("%d", &N);
        for(int i=0; i<N; i++)
        {
            float tmp;
            scanf("%f", &tmp);
            Naomi.push_back(tmp);
        }
        sort(Naomi.begin(), Naomi.begin() + N);
        //for (vector<float>::iterator it=Naomi.begin(); it!=Naomi.end(); ++it)
        //    cout << ' ' << *it;
        for(int i=0; i<N; i++)
        {
            float tmp;
            scanf("%f", &tmp);
            Ken.push_back(tmp);
        }
        sort(Ken.begin(), Ken.begin() + N);
        //for (vector<float>::iterator it=Ken.begin(); it!=Ken.end(); ++it)
        //    cout << ' ' << *it;

        d_W = Deceitful_War(Naomi, Ken);
        W = War(Naomi, Ken);
        printf("Case #%d: %d %d\n",caseNum, d_W, W);

        caseNum++;
    }

    return 0;
}

int War(vector<float> Naomi, vector<float> Ken)
{
    int cnt = 0;
    for (vector<float>::iterator it=Naomi.begin(); it!=Naomi.end(); ++it)
    {
        int N = Ken.size();
        int eraseNum = -1;
        for(int i=0; i<N;i++)
        {
            if(Ken[i]>(*it))
            {
                eraseNum = i;
                break;
            }
        }
        if(eraseNum!=-1)
        {
            Ken.erase(Ken.begin() + eraseNum);
        }
        else
        {
            cnt = Ken.size();
        }
    }
    return cnt;
}

int Deceitful_War(vector<float> Naomi, vector<float> Ken)
{
    int cnt = 0;
    for (vector<float>::iterator it=Naomi.begin(); it!=Naomi.end(); ++it)
    {
        if((*it) < Ken[0])
        {
            Ken.pop_back();
            //Naomi.erase(Naomi.begin());
        }
        else
        {
            Ken.erase(Ken.begin());
            //Naomi.erase(Naomi.begin());
            cnt++;
        }
    }
    return cnt;
}
