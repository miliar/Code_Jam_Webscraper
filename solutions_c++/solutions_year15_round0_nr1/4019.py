#include<bits/stdc++.h>

#define FOR(i,a,b) for(auto i=a; i!=b+1-2*(a>b); i+=1-2*(a>b))
#define REP(i,a,b) for(auto i=a-(a>b); i!=b-(a>b); i+=1-2*(a>b))
#define ALL(v) v.begin(),v.end()
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 155010
#define MAXN 1000000007
#define PI 3.141592653589793
#define open_read1 freopen("C:\\Users\\Hepic\\Desktop\\a.txt","r",stdin)
#define open_write1 freopen("C:\\Users\\Hepic\\Desktop\\b.txt","w",stdout)
#define open_read freopen("ariprog.in","r",stdin)
#define open_write freopen("ariprog.out","w",stdout)

using namespace std;


typedef long long LL;
typedef pair<int,int> PII;


int T,S,add_people,curr;
string people;


int main()
{
    open_read1;
    open_write1;

    scanf("%d",&T);

    FOR(i,1,T)
    {
        scanf("%d",&S);
        cin>>people;


        add_people = 0;
        curr = 0;

        REP(i,0,people.size())
        {
            if(curr < i)
            {
                ++add_people;
                ++curr;
            }

            curr += people[i]-'0';
        }


        printf("Case #%d: %d\n",i,add_people);
    }


    return 0;
}
