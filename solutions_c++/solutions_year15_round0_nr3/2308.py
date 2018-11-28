#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
string X;
int len;
int sec[10001];
inline int f2(int a, int b, bool c=0)
{
    int sign=1;
    int t;
    if(a*b<0){a<0 ? a=-a : b=-b; sign*=-1;}
    if(a!=1&&c!=0) sign*=-1;
    if(a==1){t=b;}
    else if(a==2)
    {
        if(b==1){t=2;}
        else if(b==2){t=-1;}
        else if(b==3){t=4;}
        else if(b==4){t=-3;}
    }
    else if(a==3)
    {
        if(b==1){t=3;}
        else if(b==2){t=-4;}
        else if(b==3){t=-1;}
        else if(b==4){t=2;}
    }
    else if(a==4)
    {
        if(b==1){t=4;}
        else if(b==2){t=3;}
        else if(b==3){t=-2;}
        else if(b==4){t=-1;}
    }
    return sign*t;
}
inline int f3(char x)
{
    if(x=='i') return 2;
    if(x=='j') return 3;
    if(x=='k') return 4;
}
inline bool f(int a, int b)
{
    //i:1~a, j:a+1~b, k:b+1~len
    int num;

    num=sec[a];
    if(num!=2) return false;

    num=f2(sec[a],sec[b],1);
    if(num!=3) return false;

    num=f2(sec[b],sec[len],1);
    if(num!=4) return false;
    return true;
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    bool flg;
    int T,l,re;
    string str;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        sec[0]=1;
        for(int i=1;i<1001;i++) sec[i]=0;

        cin>>l>>re;
        cin>>str;
        X="";
        flg=0;
        for(int i=0;i<re;i++) X+=str;
        len=l*re;
        //cout<<"len="<<len<<endl;
        for(int i=1;i<=len;i++) sec[i]=f2(sec[i-1],f3(X[i-1]));
        //cout<<"Cal..."<<endl;
        for(int i=1;i<len-1;i++)
        {
            for(int j=i+1;j<len;j++)
            {
                if(f(i,j)==true) flg=1;
            }
        }
        cout<<"Case #"<<k+1<<": ";
        cout<<(flg ? "YES\n" : "NO\n");
    }
    return 0;
}
