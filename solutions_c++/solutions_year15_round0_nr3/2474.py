/********************************/
/***  Coded By Ankush Sharma  ***/
/********************************/

#include<bits/stdc++.h>
using namespace std;
string str="", temp;
map<char, int> m;
int ref[5][5];


int main()
{
    //std::ios::sync_with_stdio(false);
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int t, c; cin>>t;
    c=t;
    m['i']=2, m['j']=3, m['k']=4;
    memset(ref, 0, sizeof(ref));
    ref[1][1]=1 , ref[1][2]=2 , ref[1][3]=3 , ref[1][4]=4 ,
    ref[2][1]=2 , ref[2][2]=-1 , ref[2][3]=4 , ref[2][4]=-3 ,
    ref[3][1]=3 , ref[3][2]=-4 , ref[3][3]=-1 , ref[3][4]=2 ,
    ref[4][1]=4 , ref[4][2]=3 , ref[4][3]=-2 , ref[4][4]=-1 ;
    while(t--)
    {
        long long l, x; cin>>l>>x;
        str="", temp; cin>>temp;
        for(int i=0; i<x; i++)
            str+=temp;
        set<int> s[3];
        int arr[10001]={0}, jjj[10001];
        int cur=m[str[0]]; jjj[0]=cur;
        if(cur==2) s[0].insert(0) ;
        for(int i=1; i<str.length(); i++)
        {
            cur=ref[abs(cur)][m[str[i]]]*(cur/abs(cur));
            jjj[i]=cur;
            if(cur==2) s[0].insert(i) ;
        }

        cur=m[str[str.length()-1]];
        if(cur==4) s[2].insert(str.length()-1),  arr[str.length()-1]=1 ;
        for(int i=str.length()-2; i>=0; i--)
        {
            cur=ref[m[str[i]]][abs(cur)]*(cur/abs(cur));
            if(cur==4) s[2].insert(i), arr[i]=1 ;
        }

        cout<<"Case #"<<c-t<<": ";
        set<int>::iterator p=s[0].begin();
        int flag=0, cur1=*p;
        for( ; p!=s[0].end(); p++)
        {
            cur1=*p;
            set<int>::iterator q=s[2].upper_bound(cur1);
            for( q; q!=s[2].end(); q++)
            {
                int req=jjj[*q-1];
                req=ref[req][jjj[*p]];
                if(req==3)
                {
                   cout<<"YES\n"; flag=1; break;
                }
            }
            if(flag==1) break;
        }
        if(flag==0)
        {
            cout<<"NO\n";
        }
    }
    return 0;
}

