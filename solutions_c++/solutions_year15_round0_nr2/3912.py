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


int T,D,val,answer=-1;
vector<int> cakes;


void possibilities(vector<int> vec,int cnt)
{
    vector<int> keep;
    int half;


    sort(ALL(vec),greater<int>());


    keep = vec;
    answer = (answer==-1 ? cnt+vec[0] : min(answer, cnt+vec[0]));


    if(vec[0]==0 || vec[0]==1 || (answer!=-1 && cnt>answer))
        return;



//    for(int i=0; i<keep.size(); ++i)
//        --keep[i];
//    possibilities(keep,cnt+1);


    vec.push_back(0);
    half = vec[0]/2;
    FOR(i,1,half)
    {
        --vec[0];
        ++vec[vec.size()-1];
        possibilities(vec, cnt+1);
    }

}


int main()
{
    open_read1;
    open_write1;

    scanf("%d",&T);


    FOR(i,1,T)
    {
        scanf("%d",&D);

        FOR(j,1,D)
        {
            scanf("%d",&val);
            cakes.push_back(val);
        }


        possibilities(cakes,0);


        printf("Case #%d: %d\n",i,answer);
        answer=-1;
        cakes.clear();
    }


    return 0;
}
