#include <iostream>
#include <stdio.h>

using namespace std;

void sortowanko(double tab[], int rozmiar) {
    double temp;
    for(int i=0;i<rozmiar;i++)
    {
        for(int j=0;j<rozmiar-1;j++)
        {
            if(tab[ j ]>tab[ j + 1 ]) {
                temp=tab[j];
                tab[j]=tab[j+1];
                tab[j+1]=temp;
            }
        }
    }
}

int main()
{
    int t,n;
    cin>>t;

    for(int i=0;i<t;i++) {
        cin>>n;
        double ken[n],naomi[n];
        for(int j=0;j<n;j++) {
            cin>>naomi[j];
        }
        for(int j=0;j<n;j++) {
            cin>>ken[j];
        }

        sortowanko(ken,n);
        sortowanko(naomi,n);

        int w=0,dw,c=n-1;
        bool a=true;
        for(int j=n-1;j>=0;j--) {
            for(int k=c;k>=0;k--) {
                if(ken[j]>naomi[k]) {
                    w++;
                    c=k-1;
                    break;
                }
                if(k==0) a=false;
            }
            if(a==false) break;
        }
        w=n-w;

        a=true;
        dw=0;
        c=n-1;
        for(int j=n-1;j>=0;j--) {
            a=true;
            for(int k=c;k>=0;k--) {
                if(naomi[j]>ken[k]) {
                    dw++;
                    c=k-1;
                    break;
                }
                if(k==0) a=false;
            }
            if(a==false) break;
        }
        /*
        for(int z=0;z<n;z++) cout << ken[z] << " ";
        cout << endl;
        for(int z=0;z<n;z++) cout << naomi[z] << " ";
        cout << endl;
        */

        printf ("Case #%d: %d %d", i+1,dw,w);
        if((i+1)<t) cout << endl;
    }
    return 0;
}
