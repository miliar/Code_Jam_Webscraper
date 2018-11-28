#include<bits/stdc++.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
#define mod 1000000007
#define ii  pair<int,int>

using namespace std;
typedef long long ll;



using namespace std;
/*struct node
{
    ll nm,tm;
}nd[2000010];

int cmp(const void *a,const void *b)
{
    node *va=(node *)a;
    node *vb=(node *)b;
    if(va->tm==vb->tm)
    {
        if(va->nm<vb->nm)
        return -1;
        else
        return 1;
    }
    else
    {
        if(va->nm<vb->nm)
        return -1;
        else
        return 1;
    }
    if(va->tm==vb->tm)
    return va->nm-vb->nm;
    else
    return va->tm-vb->tm;
}*/

/*ll g(ll a,ll b)
{
    if(b==0)
    return a;
    else
    return g(b,a%b);
}
ll lc(int a,int b)
{
    ll lcm=(a*b)/g(a,b);
    return lcm;
}*/


int main()
{

int tst,t;
freopen("B-large.in", "r", stdin);
freopen("Bout-LARGE", "w", stdout);
scanf("%d",&t);
    for(tst=1;tst<=t;tst++)
    {

        string s;
        cin>>s;
        int count=0,i=0,len=s.length();
        bool pos = false,neg=false;
        while(i<len){
           pos=false;
           neg=false;
            while(i<len&&s[i]=='+'){

            pos=true;
            i++;
            }
            while(i<len&&s[i]=='-'){
            neg=true;
            i++;
            }
            if(pos&&neg)
            count+=2;
            else if(neg)
            count+=1;
        }

        printf("Case #%d: %d\n",tst,count);


    }






    return 0;
}
