#include <iostream>

using namespace std;

int main()
{

    bool T[16];

    int Z,N;

    cin>>Z;

    int z,a,b;

    int temp;

    int O,Ol;

    for (z=0;z<Z;z++)
    {
        for (a=0;a<16;a++)
        {
            T[a]=0;
        }
        cin>>N;
        for (a=0;a<4;a++)
        {
            for (b=0;b<4;b++)
            {
                cin>>temp;
                if(a==(N-1))
                {
                    T[temp-1]=1;
                }
            }
        }
        cin>>N;
        for (a=0;a<4;a++)
        {
            for (b=0;b<4;b++)
            {
                cin>>temp;
                if (T[temp-1] && (a==(N-1)))
                T[temp-1]=1;
                else
                T[temp-1]=0;
            }
        }

        Ol=0;

         for (a=0;a<16;a++)
         {
             if (T[a])
             {
                 Ol++;
                 O=a;
             }
         }

         cout<<"Case #"<<z+1<<": ";
         if (Ol==0)
         cout<<"Volunteer cheated!\n";
         if (Ol==1)
         cout<<O+1<<"\n";
         if (Ol>1)
         cout<<"Bad magician!\n";
    }

    return 0;
}
