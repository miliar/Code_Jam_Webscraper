#include <bits/stdc++.h>
using namespace std;

ifstream f("wow.in");
ofstream g("wow.out");

#define LE 1066

#define char short int

char bff[LE];
char ind[LE];

char mdl(char val,char md)
{
    if (val<0) val+=md;
    if (val>=md) val-=md;
    return val;

}

int main()
{
    int nrt;
    f>>nrt;

    for (int tt=1;tt<=nrt;++tt)
    {
        char n,i;
        f>>n;

        for(i=1;i<=n;++i)
        {
            f>>bff[i];
            ind[i-1]=i;
        }


        char result=0;

        do{


            for(char right=0;right<n;++right) {

bool okz=false;

                for (char i = 0; i <= right; ++i) {

                    char p1 = mdl(i - 1, right + 1);
                    char p2 = mdl(i + 1, right + 1);



                    okz|=(ind[p2] != bff[ind[i]]&&ind[p1] != bff[ind[i]]);
                    if (okz==true) break;

                    }

                if (okz == true) continue;


                result = max((char)result, (char)(right+1));
                }





        }while (next_permutation(ind,ind+n));

        cout<<"Case #"<<tt<<": "<<result<<'\n';


        g<<"Case #"<<tt<<": "<<result<<'\n';
    }

    return 0;
}