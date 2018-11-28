#include <cstdio>
#include <vector>
using namespace std;
int n;
int l,x;
int t;
char ch[10005],arb[40005];
vector<int>inc,sf;
int calc(char c1,char c2)
{
    int as=0;
    if(c1<0)
    {
        c1=-c1;
        as=1;
    }
    if(c2<0)
    {
        c2=-c2;
        if(as==1) as=0;
        else as=1;
    }
    if(c1==1)
    {
        if(as==0) return c2;
        return -c2;
    }
    else if(c1=='i')
    {
        if(c2=='i')
        {
            if(as==0) return -1;
            return 1;
        }
        else if(c2=='j')
        {
            if(as==0) return 'k';
            return (-'k');
        }
        else if(c2=='k')
        {
            if(as==0) return (-'j');
            return 'j';
        }
        else if(c2==1)
        {
            if(as==0) return 'i';
            else return (-'i');
        }
    }
    else if(c1=='j')
    {
        if(c2=='i')
        {
            if(as==0) return (-'k');
            return 'k';
        }
        else if(c2=='j')
        {
            if(as==0) return -1;
            return 1;
        }
        else if(c2=='k')
        {
            if(as==0) return 'i';
            return (-'i');
        }
        else if(c2==1)
        {
            if(as==0) return 'j';
            else return (-'j');
        }
    }
    else if(c1=='k')
    {
        if(c2=='i')
        {
            if(as==0) return 'j';
            return (-'j');
        }
        else if(c2=='j')
        {
            if(as==0) return (-'i');
            return 'i';
        }
        else if(c2=='k')
        {
            if(as==0) return -1;
            return 1;
        }
        else if(c2==1)
        {
            if(as==0) return 'k';
            else return (-'k');
        }
    }
    return 0;
}
void updt(int s,int e,int nod,int pos)
{
    if(s==e) arb[nod]=ch[pos];
    else
    {
        int mij=(s+e)/2;
        if(pos<=mij) updt(s,mij,2*nod,pos);
        else updt(mij+1,e,2*nod+1,pos);
        arb[nod]=calc(arb[2*nod],arb[2*nod+1]);
    }
}
char query(int s,int e,int p1,int p2,int nod)
{
    if(s==p1&&e==p2) return arb[nod];
    else
    {
        int mij=(s+e)/2;
        if(p2<=mij) return query(s,mij,p1,p2,2*nod);
        else if(p1>mij) return query(mij+1,e,p1,p2,2*nod+1);
        return calc(query(s,mij,p1,mij,2*nod),query(mij+1,e,mij+1,p2,2*nod+1));
    }
}
int main()
{
    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);
    scanf("%d",&t);
    for(int yyy=1;yyy<=t;yyy++)
    {
        bool ast=0;
        printf("Case #%d: ",yyy);
        scanf("%d%d",&l,&x);
        n=l*x;
        for(int i=1;i<=40002;i++) arb[i]=1;
        scanf("%c",&ch[0]);
        for(int i=1;i<=l;i++)
        {
            scanf("%c",&ch[i]);
            updt(1,n,1,i);
        }
        for(int s=1;s<x;s++)
        {
            int tmp=s*l+1;
            for(int i=tmp;i<tmp+l;i++)
            {
                ch[i]=ch[i-l];
                updt(1,n,1,i);
            }
        }
        if(ch[1]=='i') inc.push_back(1);
        char val=ch[1];
        for(int i=2;i<=n-2;i++)
        {
            val=calc(val,ch[i]);
            if(val=='i') inc.push_back(i);
        }
        if(ch[n]=='k') sf.push_back(n);
        val=ch[n];
        for(int i=n-1;i>=3;i--)
        {
       ///     if(yyy==4) printf("%d %d ",ch[i],val);
            val=calc(ch[i],val);
            if(val=='k') sf.push_back(i);
        }
        int ss1=inc.size(),ss2=sf.size();
        for(int it1=0;it1<ss1;++it1)
        {
            for(int it2=0;it2<ss2;++it2)
            {
                if(inc[it1]+1>=sf[it2]) continue;
                val=query(1,n,inc[it1]+1,sf[it2]-1,1);
                if(val=='j')
                {
                    ast=1;
                    break;
                }
            }
            if(ast==1) break;
        }
        if(ast==0) printf(" NO");
        else printf(" YES");
        printf("\n");
        inc.clear();
        sf.clear();
    }
}
