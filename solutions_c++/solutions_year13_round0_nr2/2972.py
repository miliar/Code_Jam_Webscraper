
#include<iostream>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<math.h>
#include <sstream>

using namespace std;

bool revisar(int ii ,int jj, int n,int m,int matriz[][500], int num)
{
        bool paila1 = true;
        for(int i = 0; i < m; i ++)
        {
            if(matriz[ii][i] > num)paila1 = false;
        }
        bool paila2 = true;
        for(int i = 0; i < n; i ++)
        {
            if(matriz[i][jj] > num)paila2 = false;
        }
      //  cout<<paila1<<paila2<<endl;
        if(paila1 || paila2)return true;


}




int main()
{
    int caso = 1;

    int casos;
    cin>>casos;


    for(int i = 0; i< casos; i ++)
    {
        int n,m;
        cin>>n>>m;
        int matriz[500][500];
        for(int i = 0; i < n; i ++)
        {
            for(int j = 0; j < m; j ++)
            {
                cin>>matriz[i][j];
            }
        }
        bool bandera = true;
        for(int i = 0; i < n; i ++)
        {
            for(int j = 0; j < m; j ++)
            {
               int num = matriz[i][j];

                   bool a =  revisar(i,j,n,m,matriz,num);
                   if(!a)
                   {
                       bandera = false;
                       break;
                   }

            }
        } cout<<"Case #"<<caso++<<": ";
        if(bandera)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;




        //cout<<conta<<endl;
    }




    return 0;
}
