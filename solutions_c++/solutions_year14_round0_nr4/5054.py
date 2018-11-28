
#include <fstream>
using namespace std;

ifstream f("war.in");
ofstream g("war.out");

int t,n;
double a[1001], k[1001], b[1001];

int pozdiv(double a[1001], int li, int lf){
    int i,j;
    double aux,piv;
    i=li-1;
    j=lf+1;
    piv=a[li];
    do{
        do{i++;}while(a[i]<piv);
        do{j--;}while(a[j]>piv);
        if(i<j){
            aux=a[i];
            a[i]=a[j];
            a[j]=aux;
        }
    }while(i<j);
    return j;
}

void quicksort(double a[1001], int li, int lf){
    int m;
    if(li==lf)
    return;
    m=pozdiv(a,li,lf);
    quicksort(a,li,m);
    quicksort(a,m+1,lf);
}

int main(){
    f>>t;
    int z,i,j,nr,nrd,cod,u;
    for(z=1;z<=t;z++){
        f>>n;
        for(i=1;i<=n;i++)
            f>>a[i];
        for(i=1;i<=n;i++)
            f>>k[i];
        quicksort(a,1,n);
        quicksort(k,1,n);
        for(i=1;i<=n;i++)
            b[i]=a[i];
        nrd=0;
        for(i=n;i>=1;i--){  //umblu in vector ken
            cod=0;
            for(j=1;j<=n && cod==0;j++)
                if(b[j]>k[i]){
                    cod=1;
                    u=j;
                }
            if(cod==1){
                b[u]=0;
                nrd++;
            }
        }
        for(i=1;i<=n;i++)
            b[i]=k[i];
        nr=0;
        for(i=n;i>=1;i--){
            cod=0;
            for(j=n;j>=1 && cod==0;j--)
                if(a[i]<b[j]){
                    u=j;
                    cod=1;
                }
            if(cod==0){
                nr++;
                j=1;
                while(b[j]==0 && j<=n)
                    j++;
                b[j-1]=0;
            }
            else
                b[u]=0;
        }
        g<<"Case #"<<z<<": "<<nrd<<" "<<nr<<"\n";
    }
    return 0;
}