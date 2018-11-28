#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue> 

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b)                 for(int i=a;i<b;i++)
#define rep(i,n)                    forr(i,0,n) 
#define all(v)                      v.begin(),v.end()    
#define uniq(v)                     sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a)                      memset(a,0,sizeof a)
    
#define debug                       if(1)
#define debugoff                    if(0)    

#define print(x)                 cerr << x << " ";    
#define pn()                     cerr << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

#define MAX 100010
#define MOD 1000000007
/*
void brute()
{
    int Nr,Dr,g,A=1,B=1,C=0,D=1;    
    set< pii > s,ss;
    s.insert(make_pair(A,B));
    s.insert(make_pair(C,D));
    set< pii >::iterator i;
    set< pii >::iterator j;
  int cnt = 4;
  while(cnt--)
  {
    for(i=s.begin();i!=s.end();i++)
    {
        for(j=s.begin();j!=s.end();j++)
        {
            A = (*i).first;B = (*i).second;
            C = (*j).first;D = (*j).second;

            Nr = A*D + B*C;
            Dr = 2*B*D;
            g = __gcd(Nr,Dr);
            Nr /= g;
            Dr /= g;
            ss.insert(make_pair(Nr,Dr));
        }
    }

    s.clear();
    for(i=ss.begin();i!=ss.end();i++)    
    {
        cout<<(*i).first<<" "<<(*i).second<<"|";
        s.insert((*i));
    }
    cout<<endl;
  }
}
*/
int main()
{
    int t,gen,cases=0;
    LL P,Q;
    bool f;
    scanf("%d",&t);
    while(t--)
    {
        cases++;
        gen = 0;
        f = true;
        scanf("%lld/%lld",&P,&Q);      
        while(P<Q)
        {
            gen++;
            if(Q%2==0)
                Q/=2;
            else 
            {
                f = false;
                break;
            }    
        }
        if(f && P==Q)
            printf("Case #%d: %d\n",cases,gen);
        else if(f && P>Q && (Q&(Q-1))==0)
            printf("Case #%d: %d\n",cases,gen);
        else
            printf("Case #%d: impossible\n",cases);
    }
    return 0; 
}
