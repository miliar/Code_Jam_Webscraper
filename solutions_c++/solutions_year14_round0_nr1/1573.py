#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807
#define INF 2000000000
#define PI acos(-1.0)
#define EPS 1e-9
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    cin >> t;
    int temp=t;
    int arr1[4][4],arr2[4][4];
    while(t--)
    {
        int x,y,sol;
        scanf("%d",&x);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&arr1[i][j]);
        scanf("%d",&y);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&arr2[i][j]);
        int counter=0;
        x--,y--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(arr1[x][i] == arr2[y][j])
                    counter++,sol=arr1[x][i];
        cout << "Case #" << temp-t << ": " ;
        if(counter==0)
            cout << "Volunteer cheated!" << endl;
        else if(counter == 1)
            cout << sol << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}

/*
struct lady
{
    int beauty,smart,rich;
};

bool sorter1(lady a,lady b)
{
    return a.beauty < b.beauty;
}

bool sorter2(lady a,lady b)
{
    return a.beauty == b.beauty && a.smart < b.smart;
}

bool sorter3(lady a,lady b)
{
    return a.beauty == b.beauty && a.smart == b.smart && a.rich < b.rich;
}

int main()
{
    int n;
    cin >> n;
    lady ladies[n];
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].beauty);
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].smart);
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].rich);
    sort(ladies,ladies+n,sorter1);
    sort(ladies,ladies+n,sorter2);
    sort(ladies,ladies+n,sorter3);
    for(int i=0;i<n;i++)
        printf("%d %d %d\n",ladies[i].beauty,ladies[i].smart,ladies[i].rich);
    return 0;
}
*/
