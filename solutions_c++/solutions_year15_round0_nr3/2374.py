#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

char inp[10005];
char str[300005];
char preprod[300005];
char posprod[300005];
char mult[200][200];
int sign[200][200];
void precomp()
{
      char types[4] = {1,'i','j','k'};
      mult[1][1] =  mult['i']['i'] = mult['j']['j'] = mult['k']['k'] = 1;
      mult['i']['j'] = mult['j']['i'] = mult[1]['k'] = mult['k'][1] = 'k';
      mult['j']['k'] = mult['k']['j'] = mult[1]['i'] = mult['i'][1] = 'i';
      mult['i']['k'] = mult['k']['i'] = mult[1]['j'] = mult['j'][1] = 'j';
      
      REP(i,4)
      {
            sign[1][types[i]] = sign[types[i]][1] = 1;
            if(i!=0)sign[types[i]][types[i]] = -1;
      }
      sign['i']['j'] = 1, sign['j']['i'] = -1;
      sign['i']['k'] = -1, sign['k']['i'] = 1;
      sign['k']['j'] = -1, sign['j']['k'] = 1;
}
int main()
{
      int t;
      precomp();
      s(t);
      REP(tt,t)
      {
            printf("Case #%d: ",tt+1);
            LL x;
            LL times;
            LL l;
            sl(l);
            sl(x);
            ss(inp);
            times = min(x%4+20,x);
            strcpy(str,inp);
            REP(i,times-1)
                  strcat(str,inp);
            strcpy(inp,str);
            //printf("%s\n",inp);
            l = l*times;
            int sgn=1,firsti = -1, lastk=-1;
            preprod[0]=inp[0];
            if(preprod[0]=='i' && sgn==1 && firsti==-1)
                  firsti=0;
            INC(i,1,l-1)
            {
                  preprod[i] = mult[preprod[i-1]][inp[i]];
                  sgn = sgn*sign[preprod[i-1]][inp[i]];
                  //printf("At index %d, preprod = %c, sign = %d\n",i,preprod[i],sgn);
                  if(preprod[i]=='i' && sgn==1 && firsti==-1)
                        firsti = i;
            }
            //printf("l = %lld, firsti = %d\n",l,firsti);
            if(preprod[l-1]!=1 || sgn!=-1 || firsti==-1)
            {
                  printf("NO\n");
                  continue;
            }
            sgn=1;
            posprod[l-1] = inp[l-1];
            if(posprod[l-1]=='k')
            {
                  if(l-1-firsti>1)
                        printf("YES\n");
                  else
                        printf("NO\n");
                  continue;
            }
            DEC(i,l-2,0)
            {
                  posprod[i] = mult[inp[i]][posprod[i+1]];
                  sgn = sgn*sign[inp[i]][posprod[i+1]];
                  if(preprod[i]=='k' && sgn==1)
                  {
                        if(i-firsti>1)
                              printf("YES\n");
                        else
                              printf("NO\n");
                        lastk=i;
                        break;
                  }
            }
            if(lastk==-1)printf("NO\n");
      }
      return 0;
}
