#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int x,y;
    for(int i=0; i<n;i++)
    {
        cin >>y>>x;
        int tab[x][y];
        for(int ii=0;ii<y;ii++)
            for(int kk=0;kk<x;kk++)
            {
                 cin >> tab[kk][ii];
            }

        int no = 0;
        int no1 = 0;
        int no2 = 0;
        int yy;
        int zmian = 0;
        for(int zz=0; zz<x&&no==0; zz++)
        for(int ii=0;ii<y&&no==0;ii++)
        {
               int min = tab[zz][ii];
               for(int kk=0; kk<x; kk++)
                    if(tab[kk][ii]>min)
                    {
                        no1 = 1;
                    }
                for(int kk=0; kk<y; kk++)
                    if(tab[zz][kk]>min)
                    {
                        no2 = 1;
                    }
                if(no1&&no2)
                {
                  no = 1;
                  //cout << zz << ":" << ii <<endl;
                }
                no1 = 0;
                no2 = 0;

        }
        cout << "Case #" << i+1 << ": ";
        if(no) cout << "NO";
        else cout << "YES";
        cout << endl;
    }

    return 0;
}
