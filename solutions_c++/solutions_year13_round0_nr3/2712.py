#include<iostream>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<math.h>
#include <sstream>

using namespace std;

bool palindromo(string a)
{
    string aux = a;
    reverse(a.begin(), a.end());
   if(aux == a)return true;
   return false;
}


bool cuadrado(long long int a)
{
    double aux = sqrt(a);
    long long int y = (int)aux;
    if(y - aux == 0)return true;
    return false;
}




int main()
{
    stringstream ss;
    int casos;
    cin>>casos;
    list<string> lista;
    string pal;
    int caso = 0;
    //cin.ignore();
    for(int i = 0; i< casos; i ++)
    {
                 long long int a,b;
                 cin>>a>>b;

                int conta = 0;
                 for(int i = a; i <= b; i ++)
                 {
                     stringstream ss;
                     ss << i;
                    string aux = ss.str();

                    stringstream gg;
                     gg << (int)sqrt(i);
                    string aux2 = gg.str();
                     //cout<<"aux "<<aux<<endl;;
                     if(cuadrado(i) == true && palindromo(aux) && palindromo(aux2))
                     {
                        conta ++;
                      //  cout<<i<<endl;
                     }
                 }
                 caso ++;
                  cout<<"Case #"<<caso<<": ";
                 cout<<conta<<endl;
    }




    return 0;
}


