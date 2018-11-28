#include<bits/stdc++.h>

using namespace std;
int t;

void solve (int a)
{
    int aux=a;
    int cont=0;
    int qtosja=0;
    vector<bool> usados(10,false);

    while(qtosja<10 and cont<1000)
    {
        aux=a*(cont+1);
        while(aux>0)
        {
            int temp=aux%10;
            if(!usados[temp])
            {
                usados[temp]=true;
                qtosja++;
            }
            aux/=10;
        }
        cont++;
    }
    cout<<"Case #"<<t<<": ";
    if(cont==1000)
    {
        cout<<"INSOMNIA"<<endl;
    }
    else
    {
        long long int temp = a;
        temp=temp*cont;
        cout<<temp<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    int te;
    cin>>te;
    for(t=1;t<=te;t++)
    {
        int a;
        cin>>a;
        solve(a);
    }

    return 0;
}
