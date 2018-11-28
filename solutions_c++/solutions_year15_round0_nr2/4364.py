#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int bestCase,totalppl;
void recur(int currTime,vector<int> state)
{
    sort(state.begin(),state.end());
    int limit=state.size()-1;
    if (bestCase==-1||currTime+state[limit]<bestCase)
    {
        bestCase=currTime+state[limit];
    }
if (currTime+1>=bestCase) return;
state.push_back(0);
int pp=state[limit];
for (int dd=pp-1;dd>=(pp/2)+pp%2;dd--)
{
    state[limit]=dd;
    state[limit+1]=pp-dd;
    recur(currTime+1,state);
}

}
int main()
{
    int testCases;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> testCases;
    for (int a=0; a<testCases; a++)
    {
        bestCase=-1;
        cin >> totalppl;
        vector <int> dishes (totalppl);
        for (int b=0; b<totalppl;b++)
        {
            cin >> dishes[b];
        }
        int currTime=0;
        recur(0,dishes);

        printf("Case #%d: %d\n",a+1,bestCase);

    }


}
