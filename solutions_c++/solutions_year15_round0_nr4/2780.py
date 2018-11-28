#include<bits/stdc++.h>

using namespace std;

int main()
{
    int casos;
    scanf("%d",&casos);
    vector < set <pair<int,int> > > arr(4);
    arr[0].insert(make_pair(1,1));
    arr[0].insert(make_pair(1,2));
    arr[0].insert(make_pair(1,3));
    arr[0].insert(make_pair(1,4));
    arr[0].insert(make_pair(2,2));
    arr[0].insert(make_pair(2,3));
    arr[0].insert(make_pair(2,4));
    arr[0].insert(make_pair(3,3));
    arr[0].insert(make_pair(3,4));
    arr[0].insert(make_pair(4,4));
    arr[1].insert(make_pair(1,2));
    arr[1].insert(make_pair(1,4));
    arr[1].insert(make_pair(2,2));
    arr[1].insert(make_pair(2,3));
    arr[1].insert(make_pair(2,4));
    arr[1].insert(make_pair(3,4));
    arr[1].insert(make_pair(4,4));
    arr[2].insert(make_pair(2,3));
    arr[2].insert(make_pair(3,3));
    arr[2].insert(make_pair(3,4));
    arr[3].insert(make_pair(4,3));
    arr[3].insert(make_pair(4,4));


    for(int i = 0 ; i < casos ; i++)
    {
        int X,R,C;
        scanf("%d%d%d",&X,&R,&C);
        if(arr[X-1].find(make_pair(R,C))!=arr[X-1].end()||arr[X-1].find(make_pair(C,R))!=arr[X-1].end())
            printf("Case #%d: GABRIEL\n",i+1);
        else
            printf("Case #%d: RICHARD\n",i+1);
    }

    return 0;
}
