#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

#define MaxN 105

typedef struct
{
    bool Map_i[MaxN];
    bool Map_j[MaxN];
}Limite;
vector< vector< pair<int, int> > > vlist;
vector<int> possibility_num;
int main()
{
    int N,num=0;
    cin>>N;
    int n,m;
    Limite p[MaxN];
    while(num++<N)
    {
        cin>>n>>m;

        vlist.clear();
        for(int i = 0; i < MaxN; i ++)
        {
            vector< pair<int,int> >t;
            vlist.push_back(t);
        }
        memset(p,0,sizeof(p));
        possibility_num.clear();

        int temp;
        for(int i = 0; i <n; i ++)
            for(int j = 0; j < m; j ++)
            {
                cin>>temp;
                for(int k = 1; k <temp; k ++)
                {
                    p[k].Map_i[i] = 1;
                    p[k].Map_j[j] = 1;
                }
                vlist[temp].push_back(make_pair(i,j));
                int k = 0;
                for(k = 0; k < possibility_num.size(); k ++)
                {
                    if(possibility_num[k] == temp) break;
                }
                if(k==possibility_num.size()) possibility_num.push_back(temp);
            }
        sort(possibility_num.begin(), possibility_num.end());

        bool flag = true;
        for(int k = possibility_num.size()-2; k >=0; k --)
        {
            for(int i = 0; i < vlist[possibility_num[k]].size(); i++)
            {
                if(p[possibility_num[k]].Map_i[vlist[possibility_num[k]][i].first] == 1 && p[possibility_num[k]].Map_j[vlist[possibility_num[k]][i].second] == 1)
                {
                    flag = false;
                    break;
                }
            }
            if(flag == false)break;
        }
        if(flag)
        {
            cout<<"Case #"<<num<<": YES"<<endl;
        }
        else
        {
            cout<<"Case #"<<num<<": NO"<<endl;
        }
    }
    return 0;

}
