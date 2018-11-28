#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)


int vet[20];
unsigned long long m[20][20] =
{
    {}, {},
    {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536 },
    {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721 },
    {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824, 4294967296 },
    {1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125, 152587890625 },
    {1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336, 13060694016, 78364164096, 470184984576, 2821109907456 },
    {1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201, 96889010407, 678223072849, 4747561509943, 33232930569601 },
    {1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592, 68719476736, 549755813888, 4398046511104, 35184372088832, 281474976710656 },
    {1, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 205891132094649, 1853020188851841 },
    {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000, 10000000000000000 }
};


int main()
{
    int T, n, j;
    vector<unsigned long long> provas;

    cin>>T;

    int encontrados = 0, bits, aux;
    bool ehJam;

    /*cout<<"{\n";
    f(i, 2, 10)
    {
        unsigned long long x = 1;
        cout<<"{"<<1<<", ";
        f(j, 1, 16)
        {
            x=x*i;
            cout<<x<<", ";
        }
        cout<<"}"<<endl;
    }
    cout<<"}\n";*/


    f(t, 1, T)
    {
        cin>>n>>j;

        bits=0;


        for(; encontrados<j ; bits++)
        {
            ehJam = true;

            aux = bits;
            vet[0]=vet[n-1]=1;
            f(i, 1, n-2)
            {
                vet[i]=aux%2;
                aux/=2;
            }


            f(base, 2, 10)
            {

                unsigned long long valor = 0;
                unsigned long long * pot = m[base];
                f(i, 0, n-1)
                {
                    valor += vet[i]*pot[i];
                }

                //cout<<"base "<<base<<" valor "<<valor<<endl;
                //getch();

                unsigned long long limite = (unsigned long long) sqrt(valor)+1;
                //cout<<"limite para base "<<base<<" eh "<<limite<<endl;
                //getch();
                unsigned long long p;
                bool primo = true;  // N>=2 -> no mínimo string = 11 -> nunca vai ser 1
                for(p=2; p<=limite;)
                {
                    //cout<<"p "<<p<<endl;
                    if(valor%p==0)
                    {
                        primo = false;
                        break;
                    }
                    p++;
                }



                if(primo)
                {
                    ehJam=false;
                    break;
                }
                else
                    provas.push_back(p);

            }


            if(ehJam)
            {
                encontrados++;
                f(i, 0, n-1)
                {
                    cout<<vet[n-1-i];
                }
                cout<<" ";
                for(vector<unsigned long long>::iterator it = provas.begin(); it!=provas.end() ; it++ )
                {
                    cout<<*it<<" ";
                }
                cout<<endl;
            }

            provas.clear();
        }
    }



    return 0;
}
