#include <iostream>

using namespace std;

int main()
{
    bool uciekac;
    int ileTestow, wierszy, kolumn;
    int *maxWiersza = new int[1];
    int *maxKolumny = new int[1];
    int *pole = new int[1];

    cin>>ileTestow;

    for(int i=0; i<ileTestow; ++i)
    {
        uciekac = false;
        delete [] maxWiersza;
        delete [] maxKolumny;
        delete [] pole;

        cin>>wierszy>>kolumn;

        maxWiersza = new (nothrow) int[wierszy];
        for(int a=0; a<wierszy; ++a) maxWiersza[a]=0;

        maxKolumny = new (nothrow) int[kolumn];
        for(int a=0; a<kolumn; ++a) maxKolumny[a]=0;

        //for(int a=0; a<kolumn; ++a) {cout<<maxKolumny[a]<<"     "<<maxWiersza[a]<<endl;}

        pole = new (nothrow) int[wierszy*kolumn];

        for(int a=0; a<wierszy; ++a)
        {
            for(int b=0; b<kolumn; ++b)
            {
                cin>>pole[(a*kolumn) + b];
                if(pole[(a*kolumn) + b]>maxWiersza[a]) maxWiersza[a]=pole[(a*kolumn) + b];
                if(pole[(a*kolumn) + b]>maxKolumny[b]) maxKolumny[b]=pole[(a*kolumn) + b];
            }
        }

        /*for(int a=0; a<kolumn; ++a) {cout<<maxKolumny[a]<<"     "<<maxWiersza[a]<<endl;}
        for(int a=0; a<kolumn*wierszy; ++a) {cout<<pole[a]<<"     ";}*/

        for(int a=0; a<wierszy; ++a)
        {
            for(int b=0; b<kolumn; ++b)
            {
                if((pole[(a*kolumn) + b]<maxWiersza[a])&&(pole[(a*kolumn) + b]<maxKolumny[b])) {cout<<"Case #"<<i+1<<": NO\n"; uciekac = true; break;}
            }
            if(uciekac) break;
        }
        if(uciekac) continue;

        cout<<"Case #"<<i+1<<": YES\n";
    }

    return 0;
}
