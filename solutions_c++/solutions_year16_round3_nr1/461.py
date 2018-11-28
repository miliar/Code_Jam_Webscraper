#include<cstdio>
#include<algorithm>
#include<queue>
using namespace std;

priority_queue < pair < int,char> > H;

pair < int , char > P;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for ( int te = 1 ; te<=T ; te++ )
    {
        int n,to=0;
        scanf("%d",&n);
        for ( int c=1 ; c<=n ; c++ )
        {
            scanf("%d",&P.first);
            P.second = 'A' + c-1;
            to += P.first;
            H.push(P);
        }
        printf("Case #%d: ",te);
        if ( to % 2 == 1 )
        {
            P = H.top();
            H.pop();
            printf("%c ",P.second);
            P.first -= 1;
            if ( P.first != 0 )
                H.push(P);
        }
        while (!H.empty())
        {
            P = H.top();
            H.pop();
            printf("%c",P.second);
            P.first -= 1;
            if ( P.first != 0 ) H.push(P);
            P = H.top();
            H.pop();
            printf("%c ",P.second);
            P.first -= 1;
            if ( P.first != 0 ) H.push(P);
        }
        printf("\n");
    }
}
