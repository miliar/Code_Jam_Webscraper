#include<bits/stdc++.h>
using namespace std;
int K,L,S;
int cnt[30];
string key,target;
vector<int>pos;
map<string,double>DP;

int Max;

int score(string P)
{
    //cout<<P<<endl;
    int i,j,l=P.size();
    int ret=0;
    for(i=0; i<l; i++)
    {
        bool f=1;
        for(j=0; j<L; j++)
        {
           if(i+j>=l){
               f=0;
               break;
           }
           if(P[i+j]!=target[j]){
              f=0;
              break;
           }
        }
        if(f)  ret++;
    }
   // printf("ret:%d\n",ret);
    Max=max(Max,ret);
    return ret;
}

double F(string now)
{
    if(now.size()==S)
    {
        return score(now);
    }
    if(DP.find(now)!=DP.end())  return DP[now];

    double ret=0;
    for(int i=0; i<26; i++)
    {
        if(cnt[i]==0)  continue;
        double p=(double)cnt[i]/(double)K;
        double tmp=F(now+(char)('A'+i));
        ret+=p*tmp;
    }

    return DP[now]=ret;
}

int main()
{
    int t,it,i,j,T;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(it=1; it<=T; it++)
    {
        scanf("%d%d%d",&K,&L,&S);
        memset(cnt,0,sizeof(cnt));
        cin>>key>>target;
        sort(key.begin(),key.end());
        for(i=0; i<key.size(); i++)  cnt[key[i]-'A']+=1;

        bool f=true;
        for(i=0; i<target.size(); i++)
        {
            if(!(cnt[target[i]-'A'])){
                f=false;
                break;
            }
        }

        if(!f)
        {
            printf("Case #%d: %.8lf\n",it,0.00);
            continue;
        }

        string make="";
        make+=target;

        pos.clear();
        for(i=0; i<L; i++)
        {
            bool f=true;
            for(j=0; i+j<L; j++)
            {
                if(target[i]!=target[i+j]){
                    f=false;
                    break;
                }
            }
            if(f){
                    //printf("i:%d\n",i);
                    pos.push_back(i);
            }
        }

        Max=0;

        DP.clear();
        double v=F("");
        //printf("Max:%d\n",Max);
        printf("Case #%d: %.8lf\n",it,Max-v);
    }
    return 0;
}
