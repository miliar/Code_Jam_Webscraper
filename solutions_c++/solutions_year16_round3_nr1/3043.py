#include<bits/stdc++.h>
using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)
typedef pair<int, int> ii;

int total, n;
vector <ii> v;
bool achado;
int t;

void valido(int k, int quant, string s)
{
    //cout<<"k "<<k<<" "<<"quant "<<quant<<endl;
    //cout<<"total "<<total;
    int maximo =0;

    if(achado)
        return;
    if(k>total)
        return;


    int mapa[5]= {0};

    f(j, k, total-1)
    {
        mapa[v[j].second]++;
    }

    f(i, 0, n-1)
    {
        if(mapa[i]>maximo)
            maximo =mapa[i];
    }


    //cout<<"maximo "<<maximo<<endl;
    if(maximo>quant/2.0)
        return;

     if(k==total)
        {

            cout<<"Case #"<<t<<": "<<s<<endl;
            achado =true;
            return;
        }

    valido(k+1, quant-1, s+ ((char)(65+v[k].second))+" " );

    if(k+1<=total-1)
        valido(k+2, quant-2, s+((char)(65+v[k].second))+((char)(65+v[k+1].second))+" ");

}

int main()
{
    int T;
    string resp;
    cin>>T;

    for(t=1;t<=T; t++)
    {
        v.clear();

        int cont=0;
        cin>>n;
        total=0;
        f(c, 0, n-1)
        {
            int a;
            cin>>a;
            f(k, 1, a)
            {
                v.push_back(ii(cont, c));
                cont++;
            }
            total+=a;
        }
        vector<ii> original=v;


        for( ;  ;)
        {
            next_permutation(v.begin(), v.end());
            ///f(i, 0, total-1)
              ///  cout<<(char) (65+v[i].second);
            ///cout<<endl;
            achado = false;
            string inicial = "";
            valido(0, total, inicial);
            if(achado || v==original)
                break;

        }


    }


    return 0;
}
