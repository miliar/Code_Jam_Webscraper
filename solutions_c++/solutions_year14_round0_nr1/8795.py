#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    ifstream f("A-small-attempt0.in");
    ofstream fki("out.txt");
    int t;
    f>>t;
    for (int k=1; k<=t; k++)
    {
        int s;
        int sor;
        f>>sor;
       // cout<<sor<<endl;
        for (int i=1; i<sor; i++)
        {
            for (int j=0; j<4; j++)
            {
                f>>s;//elotte felesleges
            }
        }
        int Sor[4];
        for (int j=0; j<4; j++)
        {
            f>>Sor[j];
        }
        for (int i=sor+1; i<=4; i++)
        {
            for (int j=0; j<4; j++)
            {
                f>>s;//utana felesleges
            }
        }


         f>>sor;
        // cout<<sor<<endl;
        for (int i=1; i<sor; i++)
        {
            for (int j=0; j<4; j++)
            {
                f>>s;//elotte felesleges
            }
        }
        int Sor2[4];
        for (int j=0; j<4; j++)
        {
            f>>Sor2[j];
        }
        for (int i=sor+1; i<=4; i++)
        {
            for (int j=0; j<4; j++)
            {
                f>>s;//utana felesleges
            }
        }
        for (int i=0; i<4; i++)
        {
           // cout<<Sor[i]<<" ";
        }
       // cout<<endl;
        for (int i=0; i<4; i++)
        {
           // cout<<Sor2[i]<<" ";
        }
      //  cout<<endl;
       int mi=0;
       int ossz=0;
       for (int i=0; i<4; i++)
       {
           for (int j=0; j<4; j++)
           {if (Sor[i]==Sor2[j]){ossz++;mi=Sor[i];}}
       }
     fki<<"Case #"<<k<<": ";
     if (ossz==1){fki<<mi<<endl;}
     if (ossz==0){fki<<"Volunteer cheated!"<<endl;}
     if (ossz>1){fki<<"Bad magician!"<<endl;}

    }
    return 0;
}
