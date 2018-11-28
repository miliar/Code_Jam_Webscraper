#include<iostream>
#include<cstdio>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<algorithm>
#include<list>
#define ll long long
#define MAX_R 5
using namespace std;

int T, ans1, ans2, more_than_once=0, it;
int wyst[17]={0};
//int A[MAX_R][MAX_R];

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> T;
    for(int lzd=1; lzd<=T; ++lzd)
    {
        cin >> ans1;
        for(int i=1; i<=MAX_R-1; ++i)
        {
            for(int j=1; j<=MAX_R-1; ++j)
            {
                int temp; cin >> temp;
                if(i==ans1) wyst[temp]++;
            }
        }
        cin >> ans2;
        for(int i=1; i<=MAX_R-1; ++i)
        {
            for(int j=1; j<=MAX_R-1; ++j)
            {
                int temp; cin >> temp;
                if(i==ans2) wyst[temp]++;
            }
        }
        more_than_once=0; it=0;
        for(int i=1; i<=16; ++i)
            if(wyst[i]>1) {more_than_once++; it=i;}
        if(more_than_once==0) cout << "Case #" << lzd << ": Volunteer cheated!" << endl;
        else if(more_than_once==1) cout << "Case #" << lzd << ": " << it << endl;
        else cout << "Case #" << lzd << ": Bad magician!" << endl;
        for(int i=0; i<=16; ++i) wyst[i]=0;
    }
    return 0;
}
