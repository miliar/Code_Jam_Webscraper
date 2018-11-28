# include <cstdio>
# include <vector>
# include <algorithm>
# include <cstring>
# include <stack>

using namespace std;

struct two
{
  int pos,type,cnt;
  
  two(int p,int t,int c)
  {
    pos=p;
    type=t;
    cnt=c;
  }

  bool operator<(const two& t)const
  {
    if(pos!=t.pos)return pos<t.pos;
    return type<t.type;
  }
};

vector<two> intervals;
stack <two> takestack;

const long long MOD=1000002013ll;

long long gettot(long long D,long long N)
{
  if(D<0)D=-D;
  long long ret=((N*(N+1))/2 - ((N-D)*(N-D+1))/2)%MOD;
  //printf("%Ld\n",ret);
  return ret;
}

int main()
{
  int T;
  scanf("%d",&T);

  for(int t=1;t<=T;t++)
  {
    intervals.clear();

    int N,P;
    scanf("%d%d",&N,&P);

    long long goodtot=0ll;
    for(int i=0;i<P;i++)
    {
      int a,b,c;
      scanf("%d%d%d",&a,&b,&c);
      a--,b--;
      intervals.push_back(two(a,1,c));
      intervals.push_back(two(b,2,c));
      goodtot=(goodtot+gettot(b-a,N)*c)%MOD;
    }

    sort(intervals.begin(),intervals.end());

    long long badtot=0ll;
    for(int i=0,start=0,cnt=0;i<intervals.size();i++)
    {
      if(intervals[i].type==1)
      {
        takestack.push(intervals[i]);
      }
      else
      {
        while(1)
        {
          two t=takestack.top();
          takestack.pop();
          int reduce=min(t.cnt,intervals[i].cnt);
          badtot=(badtot+reduce*gettot(intervals[i].pos-t.pos,N))%MOD;
          t.cnt-=reduce;
          intervals[i].cnt-=reduce;
          if(intervals[i].cnt==0)
          {
            if(t.cnt!=0)takestack.push(t);
            break;
          }
        }
      }
    }

    long long improvement=(goodtot+MOD-badtot)%MOD;
    printf("Case #%d: %Ld\n",t,improvement);
  }
  return 0;
}
