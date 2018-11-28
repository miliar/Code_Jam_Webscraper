#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdlib>
#include<map>
#include<cmath>
#include<cstring>

using namespace std;
#define loop(i,N) for(i=0;i<N;i++)
#define loop1(i,N) for(i=1;i<N;i++)
#define loop2(i,x,N) for(i=x;i<N;i++)

#define revloop(i,N) for(i=N;i>0;i--)
#define revloop2(i,x,N) for(i=x;i>N;i--)

#define s(n) scanf("%d",&n)
#define s2(n,k) scanf("%d %d",&n,&k)
#define p(n) printf("%d\n",n)
#define p2(n,k) printf("%d %d\n",n,k)

#define sl(n) scanf("%ld",&n)
#define sl2(n,k) scanf("%ld %ld" ,&n,&k)

#define pl(n) printf("%ld\n",n)
#define pl2(n,k) printf("%ld %ld\n",n,k)


#define sll(n) scanf("%lld",&n)
#define sll2(n,k) scanf("%lld %lld" ,&n,&k)

#define pll(n) printf("%lld\n",n)
#define pll2(n,k) printf("%lld %lld\n",n,k)


//#define sll(n) n=fastInput()

#define sc(n) scanf("%c",&n)

//#define ss(n) scanf("%s",n)

#define sf(n) scanf("%f",&n)

#define pb(n) push_back(n)



#define MOD 1000000007

#define MAX7 10000000
#define MAX6 1000000
#define MAX5 100000
#define MAX4 10000
#define MAX3 1000

typedef unsigned long long int ulli;
typedef signed long long int slli;
typedef unsigned long int uli;
typedef signed long int sli;

using namespace std;
struct node
{
    int value;
    int id;
} ;

bool compareByLength(const node &a, const node &b)
{
    return a.value < b.value;
}
vector <node> vec;
int N;
void main2()
{

    cin>>N;
    int i,j,k,tot=0;
    node temp;
    vec.clear();
    loop(i,N)
    {
        cin>>temp.value;
        tot+=temp.value;
        temp.id=i;
        vec.push_back(temp);
    }


    sort(vec.begin(),vec.end(),compareByLength);

    revloop(j,vec.size()-1)
    {
        if(vec[j].value)
        {
            while(vec[j].value-vec[j-1].value > 1)
                {cout<<(char)(65+vec[j].id)<<(char)(65+vec[j].id)<<" ";
                vec[j].value-=2;

            }
            if(tot&1 && j==2 && vec[j-2].value==1)
                {
                cout<<(char)(65+vec[j-2].id)<<" ";
                vec[j-2].value-=1;
                tot++;
                }
            else
            {
                cout<<(char)(65+vec[j].id)<<(char)(65+vec[j-1].id)<<" ";
                vec[j].value-=1;vec[j-1].value-=1;
            }
                      sort(vec.begin(),vec.end(),compareByLength);
            j++;
        }







    }
    cout<<endl;
    }
    int T,test;


    int main()
    {
    freopen("A-small-attempt0 (2).in","r",stdin);
    freopen("output.txt","w",stdout);

        cin>>T;

        loop1(test,T+1)
        {
            printf("Case #%d: ",test);
            main2();
        }

        return 0;
    }
