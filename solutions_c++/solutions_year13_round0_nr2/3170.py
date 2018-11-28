#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>

using namespace std;
const int max_n = 105;
int a[max_n][max_n];
int maxr[max_n],maxc[max_n];
int T,N,M;

void calmaxr()
{
    for(int i=0;i<N;i++)    
    {
        maxr[i] = a[i][0];
        for(int j=1;j<M;j++)
            maxr[i] = max(maxr[i],a[i][j]);    
    }
}

void calmaxc()
{
    for(int j=0;j<M;j++)    
    {
        maxc[j] = a[0][j];
        for(int i=1;i<N;i++)
            maxc[j] = max(maxc[j],a[i][j]);    
    }
}

bool poss()
{
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(maxr[i] > a[i][j] && maxc[j] > a[i][j])
                    return false;    
            }    
        }
        return true;
}

int main()
{
    cin >> T;
    for(int t=0;t<T;t++)
    {
        cin >> N >> M;
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++)
                scanf("%d",&a[i][j]);
        calmaxr();
        calmaxc();
        cout << "Case #"<<t+1<<": ";
        if(poss())
            cout << "YES" <<endl;
        else
            cout << "NO" <<endl; 
    }
    return 0;    
}
