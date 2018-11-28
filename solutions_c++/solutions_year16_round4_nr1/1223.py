//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

char aa[100009],ss[100009];
string dd,ANS,L,R;

pair<int,pair<int,int> > check(int curr,int take,int n)
{
    if(take==n)
    {
        if(curr==0) return make_pair(1,make_pair(0,0));
        if(curr==1) return make_pair(0,make_pair(1,0));
        if(curr==2) return make_pair(0,make_pair(0,1));
    }
    pair<int,pair<int,int> > aa,ss;

    if(curr==0)
    {
        aa=check(0,take+1,n);
        ss=check(2,take+1,n);
        return make_pair(aa.first+ss.first,make_pair(aa.second.first+ss.second.first,aa.second.second+ss.second.second));
    }

    if(curr==1)
    {
        aa=check(1,take+1,n);
        ss=check(0,take+1,n);
        return make_pair(aa.first+ss.first,make_pair(aa.second.first+ss.second.first,aa.second.second+ss.second.second));
    }

    if(curr==2)
    {
        aa=check(1,take+1,n);
        ss=check(2,take+1,n);
        return make_pair(aa.first+ss.first,make_pair(aa.second.first+ss.second.first,aa.second.second+ss.second.second));
    }

}

string prnt(int curr,int take,int n)
{
    if(take==n)
    {
        if(curr==0) return "R";
        if(curr==1) return "P";
        if(curr==2) return "S";
    }

    string aa,ss;

    if(curr==0)
    {
        aa=prnt(0,take+1,n);
        ss=prnt(2,take+1,n);
        if(aa>ss) swap(aa,ss);
        return aa+ss;
    }

    if(curr==1)
    {
        aa=prnt(1,take+1,n);
        ss=prnt(0,take+1,n);
        if(aa>ss) swap(aa,ss);
        return aa+ss;
    }

    if(curr==2)
    {
        aa=prnt(1,take+1,n);
        ss=prnt(2,take+1,n);
        if(aa>ss) swap(aa,ss);
        return aa+ss;
    }

}

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    int i,j,k,l,n,cas,test,flag,temp,now,ans=0,p,r,s;
    pair<int,pair<int,int> >rock,paper,scissors,giv,tata;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>r>>p>>s;

        giv=make_pair(r,make_pair(p,s));

        rock=check(0,0,n);
        paper=check(1,0,n);
        scissors=check(2,0,n);

//        tata=giv;
//        cout<<tata.first<<" "<<tata.second.first<<" "<<tata.second.second<<endl;
//        tata=rock;
//        cout<<tata.first<<" "<<tata.second.first<<" "<<tata.second.second<<endl;
//        tata=paper;
//        cout<<tata.first<<" "<<tata.second.first<<" "<<tata.second.second<<endl;
//        tata=scissors;
//        cout<<tata.first<<" "<<tata.second.first<<" "<<tata.second.second<<endl;


        printf("Case #%d: ",cas);

        if(giv==rock)
        {
            cout<<prnt(0,0,n);
            cout<<endl;
        }
        else if(giv==paper)
        {
            cout<<prnt(1,0,n);
            cout<<endl;
        }
        else if(giv==scissors)
        {
            cout<<prnt(2,0,n);
            cout<<endl;
        }
        else cout<<"IMPOSSIBLE\n";

    }



}
