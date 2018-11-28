#include <iostream>

using namespace std;
int t;
int tab[6][6];
int tab2[6][6];
void wczytaj()
{
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int x,y;
        cin>>x;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>tab[j][k];
            }
        }
        cin>>y;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>tab2[j][k];
            }
        }
        int wynik=0;
        int z=0;
        for(int j=0;j<4;j++)
        {
            int tmp=tab[x-1][j];
            for(int k=0;k<4;k++)
            {
                if(tab2[y-1][k]==tmp) {z=tmp; wynik++; break;}
            }
            //cout<<tmp<<endl;
        }
        //cout<<wynik<<endl;
        cout<<"Case #"<<i+1<<": ";
        if(wynik==1) cout<<z;
        if(wynik>1) cout<<"Bad magician!";
        if(wynik==0) cout<<"Volunteer cheated!";
        cout<<endl;
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    wczytaj();
}
