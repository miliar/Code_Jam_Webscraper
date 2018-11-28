//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;

struct Memory
{
    int x,y,z;
};

Memory a[50];
int b[10000],c[10000];
char Ans[10000];

void rec(int n,int A,int B,int C,int l,int r)
{
    if(n==1)
    {
        if(A==1 && B==1){Ans[l]='P'; Ans[r]='R';}
        if(A==1 && C==1){Ans[l]='P'; Ans[r]='S';}
        if(B==1 && C==1){Ans[l]='R'; Ans[r]='S';}
        return;
    }

    int A1, B1, C1, A2, B2, C2,R,R1,R2;
    R=a[n-1].x; R1=a[n-1].y; R2=a[n-1].z;

    for(int i=1;i<=3;i++)
    {
        if(R+R1==A && R1+R2==B && R2+R==C){A1=R; A2=R1; B1=R1; B2=R2; C1=R2; C2=R;break;}
        if(R+R2==A && R1+R==B && R2+R1==C){A1=R; A2=R2; B1=R1; B2=R; C1=R2; C2=R1;break;}

        swap(R,R2);
        swap(R,R1);
    }


   // cout<<A1<<" "<<B1<<" "<<C1<<"\n"<<A2<<" "<<B2<<" "<<C2<<"!!!\n";
    rec(n-1,A1,B1,C1,l,(l+r)/2);
    rec(n-1,A2,B2,C2,(l+r)/2+1,r);

    bool lamp=0;
    for(int i=l;i<=(l+r)/2;i++)
    {
        if(Ans[i]==Ans[i+(l+r)/2-l+1])continue;
        if(Ans[i]<Ans[i+(l+r)/2-l+1])break;
        lamp=1; break;
    }
    if(lamp==1)
    {
        for(int i=l;i<=(l+r)/2;i++)
        {
            //cout<<i<<" "<<i+(l+r)/2-l+1<<"\n";
            swap(Ans[i],Ans[i+(l+r)/2-l+1]);
        }
    }

}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("A.in");
    ofstream cout("A.txt");


    a[0].x=1; a[0].y=0; a[0].z=0;

    for(int i=1;i<=12;i++)
    {
        a[i].x=a[i-1].x+a[i-1].z;
        a[i].y=a[i-1].y+a[i-1].x;
        a[i].z=a[i-1].z+a[i-1].y;
    }

    int T,n,A,B,C;
    cin>>T;

    for(int test=1;test<=T;test++)
    {
        cout<<"Case #"<<test<<": ";
        cin>>n>>A>>B>>C;
        swap(A,B);

        memset(b,0,sizeof(b));
        memset(c,0,sizeof(c));
        b[a[n].x]=0; b[a[n].y]=0; b[a[n].z]=0;
        b[a[n].x]++; b[a[n].y]++; b[a[n].z]++;

        c[A]=0;c[B]=0;c[C]=0;
        c[A]++;c[B]++;c[C]++;
        if(c[A]!=b[A] || c[B]!=b[B] || c[C]!=b[C]){cout<<"IMPOSSIBLE\n";continue;}

        memset(Ans,0,sizeof(Ans));
        rec(n,A,B,C,1,(1LL<<n));

        for(int i=1;i<=(1<<n);i++){if(Ans[i]==0)continue;cout<<Ans[i];}
        cout<<"\n";


    }





    return 0;
}


