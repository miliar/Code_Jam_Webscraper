#include<iostream>
#include<cstdio>
#include<vector>
#include<set>

using namespace std;
#define For(a,b,c) for(a = b;a < c; a++)
#define rep(a,b) for(int a=0;a<b;a++)


int main()
{
    freopen ("data.out","w",stdout);
    freopen ("data.in","r",stdin);
    int t;
    cin>>t;
    int fila,aux,soluciones;
    vector<int> v;
    rep(T,t)
    {
        v.assign(19,0);
        cout<<"Case #"<<T+1<<": ";
        cin>>fila;
        rep(i,4) rep(j,4)
        {
            cin>>aux;
            if(i == fila - 1) v[aux]++;
        }
        cin>>fila;
        rep(i,4) rep(j,4)
        {
            cin>>aux;
            if(i == fila - 1) v[aux]++;
        }
        soluciones = 0;
        rep(i,18) if(v[i] == 2)
        {
            soluciones++;
            aux = i;
        }
        if(soluciones == 1) cout<<aux;
        else if(!soluciones) cout<<"Volunteer cheated!";
        else cout<<"Bad magician!";
        cout<<endl;
    }
    return 0;
}
