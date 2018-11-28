#include <iostream>
#include <cstring>
#include <math.h>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;



int main()
{
    int cuantos[1005];
    memset(cuantos, 0, sizeof(cuantos));
    //set<int> puedenser;
    map<int, int> puedenser;
    for(int i = 1; i <= sqrt(1000); i++)
    {
        puedenser[i*i] = i;
    }

    int cont = 0;
    int voy;
    for(int i = 1; i <= 1000; i++)
    {
        if(puedenser.find(i) != puedenser.end())
        {
            //cout << "puede ser "<<i<<"raiz " << puedenser[i]<<endl;
            stringstream convert;
            convert << i;
            string s = convert.str();
            //cout << s <<endl;
            string s2 = s;
            reverse(s.begin(), s.end());
            if(s2 == s)
            {
                //cout << "cuadrado palindrome"<<endl;
                stringstream convert2;
                convert2 << puedenser[i];
                s = convert2.str();
                s2 = s;
                reverse(s.begin(), s.end());
                if(s2 == s)
                {
                    int j = i;
                    //cout << "Raiz palindrome"<<endl;
                    while(cuantos[j] == 0)
                    {
                        cuantos[j] = cont;
                        j--;
                    }
                    //cout<< "raiz " << s2 <<" de "<<i<<endl;
                    //cout<< "raiz " << puedenser[i] <<" de "<<i<<endl;
                    //cout <<"cont "<<cont<<endl;
                    cuantos[i] = ++cont;
                    voy = i;
                }
            }
        }
    }
    while(voy <= 1000)
    {
        cuantos[voy] = cont;
        voy++;
    }

    int k;
    cin>>k;
    for(int c = 0; c < k; c++)
    {
        int n, m;
        cin>>n>>m;
        cout << "Case #"<<c+1<<": "<<cuantos[m]-cuantos[n-1]<<endl;
    }
    return 0;
}
