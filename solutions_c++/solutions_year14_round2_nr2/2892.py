#include <fstream>
using namespace std;

ifstream f("newlottery.in");
ofstream g("newlottery.out");

long long a,b,k;
int m[90],n[90],sol[90],p,q,r,t;

void baza2 (long long x, int m[90],int &p){
    int i=1;
    while(x>0){
        m[i]=x%2;
        x=x/2;
        i++;
    }
    p=i-1;
}

void andi(int m[90], int p, int n[90], int &q){
    int i;
    if(p<q){
        for(i=1;i<=p;i++)
            if(m[i]==1 && n[i]==1)
                n[i]=1;
            else
                n[i]=0;
        q=p;
    }
    else{
        for(i=1;i<=q;i++)
            if(m[i]==1 && n[i]==1)
                n[i]=1;
            else
                n[i]=0;
    }
}

void nr10(long long &x, int m[90], int p){
    x=0;
    int i;
    long long pu=1;
    for(i=1;i<=p;i++){
        if(m[i]==1)
            x=x+pu*m[i];
        pu=pu*2;
    }
}

void creste(int sol[90], int &r){
    int t=1,i=1;
    do{
        sol[i]=sol[i]+t;
        t=sol[i]/10;
        sol[i]=sol[i]%10;
        i++;
    }while(t!=0 && i<=r);
    if(t!=0){
        r++;
        sol[r]=t;
    }
}

void vidare(int m[90], int &p){
    for(int i=1;i<=p;i++)
        m[i]=0;
    p=0;
}

int main()
{
    int i;
    long long x,y,j,l;
    f>>t;
    for(i=1;i<=t;i++){
        f>>a>>b>>k;
        r=1;
        for(j=0;j<a;j++)
            for(l=0;l<b;l++){
                vidare(m,p);
                vidare(n,q);
                baza2(j,m,p);
                baza2(l,n,q);
                andi(m,p,n,q);
                nr10(x,n,q);
                if(x<k){
                    creste(sol,r);
                }
            }
        g<<"Case #"<<i<<": ";
        for(j=r;j>=1;j--)
            g<<sol[j];
        g<<"\n";
        vidare(sol,r);
    }
    return 0;
}
