#include<cstdio>
#include<algorithm>
#include<bitset>
#include<vector>
#include<string>
#include<cstring>
#define LL long long
using namespace std;

struct Trie {
    int nr;
    Trie *alf[26];
    ~Trie()
    {
        for(int i= 0;i<26;i++)delete alf[i];
    }
    Trie()
    {
        for(int i = 0;i<26;i++)alf[i] = 0;
        nr = 0;
    }
};
Trie *root,*aux;

bitset<15> viz;
vector<int> V[10];
int T,N,M,SOL,cnt,i,S[10],nr,j,startPos,endPos,ok,first;
char A[10][110],Str[110],*p;

int make_trie(int X)
{
    int prec = 0,total =0,curr=0;
    int c;
    Trie *root,*aux;
    root = new Trie;
    root->nr = 1;
    for(vector<int>::iterator it=V[X].begin();it!=V[X].end();it++)
    {
        strcpy(Str,A[*it]);
        prec = 1;
        for(aux=root,p=Str;*p;p++)
        {
            prec = aux->nr;
            c = *p - 'A';
            if(! (aux->alf[c]))
            {
                aux->alf[c] = new Trie;
                aux->alf[c]->nr = ++total;
            }
            aux = aux->alf[c];
            curr = aux->nr;
        }
    }
    delete root;
    return total;
}

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        SOL = 0;
        nr = 0;
        printf("Case #%d: ",t);
        scanf("%d%d",&M,&N);
        for(i=1;i<=M;i++)scanf(" %s",A[i]);
        startPos = endPos = 0;
        for(i=1;i<=M;i++)
        {
            startPos = startPos*10 + 1;
        }
        endPos = startPos * N;
        for(i=startPos;startPos<=endPos;startPos++)
        {
            i = startPos;
            viz = 0;
            ok = 1;
            int no = 0;
            for(j=1;j<=M;j++)
            {
                S[j] = i%10;
                i/=10;
                if(S[j]>0 && S[j]<=N)
                {
                    no += (viz[S[j]] == 0);
                    viz[S[j]] = 1;
                }
                else ok = 0;
            }
            if(!ok || no != N)continue;
            for(j=1;j<=N;j++)V[j].resize(0);
            for(j=1;j<=M;j++)
                V[S[j]].push_back(j);
            cnt = 0;
            for(i=1;i<=N;i++)
                cnt+=make_trie(i);
            if(SOL<cnt){SOL = cnt;nr=0;}
            if(SOL==cnt)nr++;
        }
        printf("%d %d\n",SOL+N,nr);
    }
    return 0;
}
