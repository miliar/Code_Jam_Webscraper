#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1005;

int main()
{
    freopen("E:\\acm\\input.txt","r",stdin);
    freopen("E:\\acm\\output.txt","w",stdout);
    int T; cin>>T;
    for(int cas=1; cas<=T; cas++)
    {
        printf("Case #%d: ",cas);
        int N; cin>>N;
        int a[MAXN],b[MAXN];
        for(int i=0; i<N; i++)
        {
            char tmp;
            while(cin>>tmp && tmp!='.'){}
            cin>>a[i];
        }
        for(int i=0; i<N; i++)
        {
            char tmp;
            while(cin>>tmp && tmp!='.'){}
            cin>>b[i];
        }
        sort(a,a+N);
        sort(b,b+N);
        int x = 0,y = 0;

        int j = N-1;
        for(int i=N-1; i>=0; i--)
        {
            if(a[i] > b[j]) y++;
            else j--;
        }
        int low = 0;
        j = N-1;
        for(int i=N-1; i>=low; )
        {
            if(a[i] > b[j]) x++, i--, j--;
            else low++, j--;
        }
        cout<<x<<" "<<y<<endl;
    }
}
