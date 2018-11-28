#include<iostream>
#include<math.h>
#include<fstream>
#include<string>
using namespace std;

#define ull unsigned long long int
ull bin = 0;
ull coinct;



int primality_test(ull n)
{
    if(n==2) return 1;
    if(n==3) return 1;
    if(n%2==0) return 0;
    if(n%3==0) return 0;

    ull i = 5;
    ull w = 2;
    while(i*i <=n)
    {
        if(n%i==0) return 0;

        i+=w;
        w = 6-w;
    };

    return 1;
}

ull getfactor(ull n)
{
    ull i;
    for( i=2; i<sqrt(n); i++)
    {
        if(n%i==0)
        {
            break;
        }
    }

    return i;
}


ull tobin(ull n)
{

    if(n/2!=0) tobin(n/2);
    bin = bin*10 + n%2;

    return bin;
}

ull base_changer(ull n,int base)
{
    ull num = 0;
    int ll = 0;
    while(n)
    {
        num = num + (n%10)*pow(base,ll++);
        n/=10;
    }

    return num;
}

int main()
{
   // cout << base_changer(100011,2) << endl;
    ifstream file;
    ofstream out("/Users/Az/Dropbox/codejam/16_3/out");
    file.open ("/Users/Az/Dropbox/codejam/16_3/inp");
    int n;
    ull number;
    int N, J;
    int flag;
    int ct = 1;
    file >> n;
    while(n--)
    {

        file >> N >> J;
        out << "Case #" << ct <<":\n";
        coinct = 1;
        for (ull i=0; coinct<=J; i++)
        {
            flag = 0;
            tobin(i);
            number = pow(10,N-1) + bin*10 + 1;
            //cout << number << "\n";
            bin = 0;

            ull baseval[11] = {0};
            ull fac[9] = {0};
            for(int j=2; j<=10; j++)
            {
                baseval[j] = base_changer(number,j);
                if(primality_test(baseval[j]))
                {
                    //cout << baseval[j] << " => Prime \n";
                    flag = 1;
                    break;
                }
            }
            if(flag)
                continue;
            else
            {
                    coinct++;
                    int ll = 2;
                    out << number;
                    for(int i=0; i<9; i++)
                        {   fac[i] = getfactor(baseval[ll++]);
                            out <<" "<< fac[i];
                        }
                        out << "\n";
            }

            //cout << number << endl;

        }
        ct++;
//        cout << getfactor(number);
//        if(primality_test(number)) cout << "prime\n";
//        else cout << "not prime";
    };
    return 0;
}
