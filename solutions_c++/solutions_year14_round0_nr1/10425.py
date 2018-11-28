#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#define  TAM 4
using namespace std;

int matriz1[TAM][TAM], matriz2[TAM][TAM];
vector<int> vec1, vec2;
set<int> mySet;

void init()
{
    vec1.clear();
    vec2.clear();
}

void readOne()
{
    for(int x=0; x<TAM; x++)
        for(int y=0; y<TAM; y++)
            scanf("%d", &matriz1[x][y]);
}

void readTwo()
{
    for(int x=0; x<TAM; x++)
        for(int y=0; y<TAM; y++)
            scanf("%d", &matriz2[x][y]);
}

void getVecOne(int row)
{
    for(int x=0; x<4; x++)
        vec1.push_back(matriz1[row][x]);
}

int getAnswer()
{
    mySet.clear();
    int ans;
    for(int i=0; i<vec1.size(); i++)
        for(int j=0; j<vec2.size(); j++)
            if(vec1[i] == vec2[j])
                mySet.insert(vec1[i]);

    ans = mySet.size();
    return ans;
}

void getVecTwo(int row)
{
    for(int x=0; x<4; x++)
        vec2.push_back(matriz2[row][x]);
}

int main()
{
    int casos, ans1, ans2;

    scanf("%d", &casos);
    for(int i=1; i<=casos; i++)
    {
        init();
        scanf("%d", &ans1);
        readOne();
        getVecOne(ans1 - 1);
        scanf("%d", &ans2);
        readTwo();
        getVecTwo(ans2 - 1);

        int ans = getAnswer();
        int tmp;
        if(ans == 1)
        {
            tmp = (*mySet.begin());
            printf("Case #%d: %d\n", i, tmp);
        }
        else if(!ans)
        {
            printf("Case #%d: Volunteer cheated!\n", i);
        }
        else
            printf("Case #%d: Bad magician!\n",i);
    }
return 0;
}
