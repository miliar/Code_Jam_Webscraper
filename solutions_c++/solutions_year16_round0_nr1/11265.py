#include <iostream>
using namespace std;
struct hola
{
    int p;
    bool aux;
};
int main ()
{
    int a;
    cin>>a;
    for(int i=0; i<a; i++)
    {
        hola q[10];
        for(int j=0; j<10; j++)
        {
            q[j].p=j;
            q[j].aux=false;
        }
        long long  b;
        cin>>b;
        if(b==0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
        else
        {
            int y=1;
            int auxi=b;
            bool respuesta = false;
            do{

                while( b > 0 )
                {
                    int w = b%10;
                    b /= 10;
                    q[w].aux=true;
                }
                if(q[8].aux==true&&q[1].aux==true&&q[2].aux==true&&q[3].aux==true&&q[4].aux==true&&q[5].aux==true&&q[6].aux==true&&q[7].aux==true&&q[9].aux==true&&q[0].aux==true)
            {
            cout<<"Case #"<<i+1<<": "<<auxi*y<<endl;
              respuesta= true ;
            }
             y++;
                b = auxi*y;

             }while(respuesta==false);
        }

    }
}
