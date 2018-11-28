#include <iostream>
#include <list>
#include <algorithm>
#include <stdio.h>
using namespace std;
long long t,n,j,imp,tam,c;
list <long long > l;
long long a[20],b[20];
int main()
{
    ios::sync_with_stdio(0);
    freopen("outbig.txt","w+",stdout);
    cout << "Case #1:"<<endl;
    n=32;
    c=500;
    imp=0;
    tam=n/2-1;
    for (int i=0;i<tam&&imp<c;i++)
    {
        do
        {
            do
            {
                cout << "1";
                for (int k=0;k<tam;k++)
                    cout << a[k]<<b[k];
                cout <<"1 ";
                for (int i=2;i<10;i++)
                    cout << i+1<< " ";
                cout << "11"<< endl;
                imp++;
            }while (next_permutation(b,b+tam)&&imp<c);
            sort(b,b+tam);
        }while (next_permutation(a,a+tam)&&imp<c);
        a[i]=1;
        b[i]=1;
        sort(a,a+tam);
        sort(b,b+tam);
    }
    fclose(stdout);
    return 0;
}
