#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN=10005;
int a,b,t,i,j,len,currint,ind1,ind2,index1[MAXN],index2[MAXN];
bool ans;
char currchar;
string aa,bb,cc,c;
pair<int,char> hold,ii=make_pair(0,'i'),jj=make_pair(0,'j'),kk=make_pair(0,'k'),times[256][256],prod[MAXN][MAXN];
int main()
{
    freopen("k.in","r",stdin);
    freopen("C:/Users/Penguin/Desktop/OUT.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    times['1']['1']=make_pair(0,'1');
    times['1']['i']=make_pair(0,'i');
    times['1']['j']=make_pair(0,'j');
    times['1']['k']=make_pair(0,'k');
    times['i']['1']=make_pair(0,'i');
    times['i']['i']=make_pair(1,'1');
    times['i']['j']=make_pair(0,'k');
    times['i']['k']=make_pair(1,'j');
    times['j']['1']=make_pair(0,'j');
    times['j']['i']=make_pair(1,'k');
    times['j']['j']=make_pair(1,'1');
    times['j']['k']=make_pair(0,'i');
    times['k']['1']=make_pair(0,'k');
    times['k']['i']=make_pair(0,'j');
    times['k']['j']=make_pair(1,'i');
    times['k']['k']=make_pair(1,'1');
    cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        cout<<"Case #"<<tt<<": ";
        cin>>a>>b>>cc;
        len=a*b;
        ind1=0;
        ind2=0;
        if (len<3)
        {
            cout<<"NO\n";
            continue;
        }
        ans=false;
        c="";
        while (b--)c+=cc;
        for (i=0;i<len;i++)
        {
            prod[i][i]=make_pair(0,c[i]);
            currint=0;
            currchar=c[i];
            for (j=i+1;j<len;j++)
            {
                hold=times[currchar][c[j]];
                currint^=hold.first;
                currchar=hold.second;
                prod[i][j]=make_pair(currint,currchar);
            }
            if (prod[0][i]==ii)
            {
                index1[ind1++]=i;
            }
        }
        for (i=len-1;i>=2;i--)
        {
            if (prod[i][len-1]==kk)
            {
                index2[ind2++]=i;
            }
        }
        for (i=0;i<ind1;i++)
        {
            for (j=0;j<ind2;j++)
            {
                if (index2[j]-index1[i]>1 && prod[index1[i]+1][index2[j]-1]==jj)
                {
                    ans=true;
                    goto here;
                }
            }
        }
        here:
        if (ans)cout<<"YES\n";
        else cout<<"NO\n";
    }
    return 0;
}
