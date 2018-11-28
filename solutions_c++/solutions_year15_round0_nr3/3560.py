#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<map>
#include<list>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<set>




#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define all(s) s.begin(),s.end()
#define pb push_back
#define mp make_pair
#define sd(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define pd(x) printf("%d",x)
#define ll long long
const int mod = ((1E9)+7);
const int intmax = ((1E9)+7);




#ifndef ONLINE_JUDGE
#define TRACE
#endif
#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cout<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cout<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
#endif

using namespace std;


#define n_ 100005

int mul[5][5]={    {0,0,0,0,0},
                   {0,1,2,3,4},
                   {0,2,-1,4,-3},
                   {0,3,-4,-1,2},
                   {0,4,3,-2,-1}
                };




int lres[n_];
int rres[n_];




//term
#define mid  ((start+end)/2)
#define left (2*node)
#define right (2*node+1)

//treenode defination

struct treenode
{
    int ans;
};


treenode tree[400005];

string s;

int count1,count2;


//merge
treenode merge_(treenode a,treenode b)
{
    int res1=a.ans;
    int res2=b.ans;
    int fact1=1;
    int fact2=1;
    treenode newnode;

    if(res1<1)  { fact1 =-1 ; res1=-res1;}
    if(res2<1)  { fact2 =-1 ; res2=-res2;}

    int res= mul[res1][res2];
    newnode.ans=res*fact1*fact2;
    return newnode;
}


//build
void build(int node,int start,int end)
{

    if(start==end)
    {
         //initialization
        tree[node].ans=s[start]-'0';
        return;
    }

    build(left,start,mid);
    build(right,mid+1,end);
    tree[node]=merge_(tree[left],tree[right]);


}





treenode query(int node,int start,int end,int l,int r)
{


    if(start>r||end<l)
    {
         treenode res;
         res.ans=-7;
         return res;
    }

    if(start>=l&&end<=r) {return tree[node];}

    treenode a=query(left,start,mid,l,r);
    treenode b=query(right,mid+1,end,l,r);
    if(a.ans==-7) return b;
    if(b.ans==-7) return a;
    return merge_(a,b);


}


int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int test,a,b,c,l,x;


    sd(test);
    string t;
    int fact;

    int case_=1;
    while(test--)
    {

        count2=0;
        count1=0;

        sd(l);
        sd(x);
        c=x-1;
        cin>>t;

        for(int i=0;i<t.size();i++)
        {
            if(t[i]=='i') t[i]='2';
            if(t[i]=='j') t[i]='3';
            if(t[i]=='k') t[i]='4';

        }


        s=t;



        while(c--)
            s+=t;

        build(1,0,s.size()-1);







        int res=1;
        for(int i=0;i<s.size();i++)
        {

            fact=1;
            if(res<0)
            {
                fact=-1;
                res=-res;
            }
            res=mul[res][(s[i]-'0')];
            res=res*fact;


            if(res==2) lres[count1++]=i;

        }




        res=1;
        for(int j=s.size()-1;j>=0;j--)
        {

            fact=1;
            if(res<0)
            {
                fact=-1;
                res=-res;
            }
            res=mul[(s[j]-'0')][res];
            res=res*fact;

            if(res==4) rres[count2++]=j;

        }



        int flag=0;
        for(int i=0;i<count1;i++)
        {
            if(flag) break;
            for(int j=0;j<count2;j++)
            {
                if(rres[j]-1<lres[i]+1) break;

                    int f=query(1,0,s.size()-1,lres[i]+1,rres[j]-1).ans;
                    if(f==3)
                    {

                        flag=1;
                        break;
                    }

            }

        }

       // cout<<l<<" "<<x<<endl;


        if(flag) printf("Case #%d: YES\n",case_);
        else  printf("Case #%d: NO\n",case_);
        case_++;
    }



    return 0;


}
