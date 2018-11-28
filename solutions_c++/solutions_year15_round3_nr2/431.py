//Author : Jatin Goyal
//codecracker4

#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007  //NA
#define N 1000000+5
#define ll long long int
#define dt int
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)
#define tr(container, it) for(vector<dt> ::iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> >::iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)
#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;
#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second
string str,targ;
vector<char>ans;
int s,f[N];
double bas=0,maxe,num;

int kmp()
{
    int m=targ.size(),n=ans.size();
    if(m>n){ return 0;} //if pattern is more than text

    int i=0,ct=0,j=0;

    while(i<n)
    {
        int check=-1;
        while(i<n)
        {
            if(j==m) j=f[j];  //if input is in stl ..then pattern [m] gives sigsegv
            if(ans[i]==targ[j]) {j++; i++; if(j==m) {check=i; break;}}
            else if(j>0) j=f[j];
            else i++;
        }
        if(check!=-1) ct++; //check-m gives the matching index  // for(i=check-m;i<check;i++) cout<<text[i];
        else break;

        //j=0; //so that for i/p,jjjjj -jj ,o/p is 2 ,otherwise it is 4
    }
    return ct;
}

int rec(int ct)
{
    if(ct==s)
    {
        int dum=kmp();
        maxe=max(maxe,(double)dum);
        num+=dum;
        bas++;
        return 0;
    }
    for(int i=0;i<str.size();i++)
    {
        ans.pb(str[i]);
        rec(ct+1);
        ans.pop_back();
    }
}

int failure()  //longest matching prefix and suffix //used when current string to be matched fails with text
{
    int i,j;
    f[0]=0;  //for zero length 0
    f[1]=0;  //for length 1 -also zero

    for(i=2;i<=targ.size();i++)
    {
        j=f[i-1];
        while(3)
        {
            if(targ[j]==targ[i-1])
            {
                f[i]=j+1;
                break;
            }
            if(j==0) {f[i]=0; break;}
            j=f[j];
        }
    }
    return 0;
}
int main()
{
    int t,l,k;
	freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
	cin>>t;
	rep(tes,1,t)
	{
        bas=0;
        maxe=0;
        num=0;
	    cout<<"Case #"<<tes<<": ";
	    cin>>k>>l>>s;
	    cin>>str>>targ;
	    failure();
	    //rep(i,0,targ.size()) cout<<f[i]<<' '<<endl;
	    for(int i=0;i<str.size();i++)
        {
            ans.pb(str[i]);
            rec(1);
            ans.pop_back();
        }
        //rep(i,0,3) ans.pb('A');
        //cc1(kmp());
        //cc3(maxe,num,bas);
        printf("%0.12lf\n",maxe-num/bas);
    }
}


