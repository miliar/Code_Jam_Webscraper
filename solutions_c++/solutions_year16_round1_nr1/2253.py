//AUTOR:MURRUGARRA JEFFRI ERWIN
//UNIVERSIDAD: UNIVERSIDAD NACIONAL DE TRUJILLO
#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i 1<<30-1
struct Nodo
{
    char dato;
    Nodo *sgt;
};
typedef Nodo* Tlista;
Tlista CrearNodo(char V)
{
    Tlista nuevo=new Nodo();
    nuevo->dato=V;
    nuevo->sgt=NULL;
    return nuevo;

}
Tlista InsertarInicio(Tlista &p,char data)
{
    Tlista nuevo=CrearNodo(data);
    if(p!=NULL)
    {
        nuevo->sgt=p;
    }
    p=nuevo;
    return p;
}
Tlista InsertarFinal(Tlista &p,char data)
{
   Tlista nuevo=CrearNodo(data);
    Tlista t,q=p;
    while(q!=NULL)
    {
        t=q;
        q=q->sgt;
    }
    if(p==NULL)
    {
        p=nuevo;
    }
    else
    {
        t->sgt=nuevo;
    }
        return p;
}

void Mostrar(Tlista p)
{
    Tlista q=p;
    while(q!=NULL)
    {
        printf("%c",q->dato);
        q=q->sgt;
    }
}
int main(){
/*
   freopen("A-large (1).in", "r", stdin);
   freopen("A-large (1).txt", "w", stdout);
*/
int casos;
scanf("%d",&casos);
char cad[1005],cad2[1005];
REP(i,casos)
{
    Tlista p=NULL;
    scanf("%s",&cad);
    int t=strlen(cad);
    int val=cad[0];
    REP(i,t)
    {
        if(i==0)
        {
            InsertarInicio(p,cad[i]);
        }
        else
        {
            if(val>(int) cad[i])
            {
                InsertarFinal(p,cad[i]);//insertar final;
            }
            else
            {
                InsertarInicio(p,cad[i]);//insertar inicio;
                val=cad[i];
            }


        }
    }
    printf("Case #%d: ",i+1);
    Mostrar(p);
    printf("\n");
}

/*

    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


