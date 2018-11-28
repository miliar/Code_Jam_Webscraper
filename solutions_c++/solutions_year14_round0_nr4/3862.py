#include <iostream>
#include <algorithm>

using namespace std;
int t;
long double n[1<<10];
long double k[1<<10];
int y;
int maxx()
{
    int wynik=0;
    int s=0;
    for(int i=0;i<y;i++)
    {
        if(n[i]>k[s])
        {
            wynik++;
            s++;
        }
    }
    return wynik;
}
int maxx2()
{
    int wynik=0;
    int s=0;
    for(int i=0;s<y;)
    {
        if(n[i]>k[s])
        {
            wynik++;
            s++;
        }
        else
        {
            i++;
            s++;
        }
    }
    return wynik;
}
void wypisz()
{
    for(int i=0;i<y;i++) cout<<n[i]<<" ";
    cout<<endl;
    for(int i=0;i<y;i++) cout<<k[i]<<" ";
    cout<<endl;
}
void wczytaj()
{
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>y;
        for(int j=0;j<y;j++) cin>>n[j];
        for(int j=0;j<y;j++) cin>>k[j];
        sort(n,n+y);
        sort(k,k+y);
        //wypisz();
        cout<<"Case #"<<i<<": "<<maxx()<<" "<<maxx2()<<endl;

    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    wczytaj();
}
