#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

pair<double,int> D[2010];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T,N;
    double A[1005],B[1005];
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        for(int i=0;i<N;i++)
        {
            cin>>A[i];
            D[i].first=A[i];
            D[i].second=1;
        }
        for(int i=0;i<N;i++)
        {
            cin>>B[i];
            D[i+N].first=B[i];
            D[i+N].second=2;
        }
        sort(A,A+N);
        sort(B,B+N);
        sort(D,D+2*N);
        int aa=0,bb=0;
        int cnt=0;
        for(int i=0;i<2*N;i++)
        {
            if(D[i].second==1) cnt++;
            else
            {
                if(cnt>0)
                {
                    bb++;
                    cnt--;
                }
            }
        }
        bb=N-bb;
        int pb=0;
        for(int i=0;i<N;i++)
        {
            if(A[i]>B[pb])
            {
                aa++;
                pb++;
            }
        }
        printf("Case #%d: %d %d\n",ca,aa,bb);
    }
    return 0;
}




