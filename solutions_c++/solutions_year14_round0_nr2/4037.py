#include <iostream>

using namespace std;
int t;
void wczytaj()
{
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long double c,f,x;
        cin>>c>>f>>x;
        long double wynik=0;
        long double s=2;
        while((long double)x/s>(long double)(c/s)+(x/(s+f)))
        {
            wynik+=c/s;
            s+=f;
        }
        wynik+=x/s;
        cout.precision(15);
        cout<<"Case #"<<i<<": "<<wynik<<endl;
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    wczytaj();
}
