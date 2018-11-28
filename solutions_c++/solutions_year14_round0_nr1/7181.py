#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define MOD 1000000009


template <typename X> X gcd(X a, X b){if(!b)return a; else return gcd(b, a%b);}

int main()
{
    int t;
    freopen("C:/Users/UMANG JALAN/Desktop/CODE/inp.txt","r",stdin);
    freopen("C:/Users/UMANG JALAN/Desktop/CODE/out.txt","w",stdout);
    scanf("%d",&t);
    int x,y;
    int temp=1;
    while(t--)
    {
        bitset<17> bs; bs.set();
        scanf("%d",&x);
        for(int i=1;i<=4;i++)
        {
        for(int j=1;j<=4;j++)
        {
            scanf("%d",&y);
            if(i==x) bs[y]=0;
        }
        }
        int cnt=0,ans;
        scanf("%d",&x);
        for(int i=1;i<=4;i++)
        {
        for(int j=1;j<=4;j++)
        {
            scanf("%d",&y);
            if(i==x && bs[y]==0) {cnt++; ans=y;}
        }
        }
        if(cnt==1)
        {
            printf("Case #%d: %d\n",temp,ans);
        }
        else if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",temp);
        }
        else{
            printf("Case #%d: Bad magician!\n",temp);
        }
        temp++;
    }
}
