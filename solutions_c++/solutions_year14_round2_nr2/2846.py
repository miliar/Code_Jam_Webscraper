#include <fstream>
std::ifstream fin("B-small-attempt0.in");
std::ofstream fout("output.out");
int a, b, k, c;
void citire()
{
     fin>>a>>b>>k;
}
void numarare()
{
     c = 0;
     for(int i = 0; i< a; i++)
     {
             for(int j = 0; j< b; j++)
             {
                     if((i&j) < k) c++;
             }
     }
}
void afisare(int a)
{
     fout<<"Case #"<<a+1<<": "<<c<<"\n";
}
int main()
{
    int T;
    fin>>T;
    for(int i =0; i< T; i++)
    {
           citire();
           numarare();
           afisare(i);
    }
    return 0;
}
