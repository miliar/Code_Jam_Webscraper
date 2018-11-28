#include <fstream>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

int viz[17],t,a[5],k,aux,nr,sol;

int main()
{
    int i,g,h;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>k;nr=0;
        for (g=1;g<=4;g++)
            if (g!=k)
            for (h=1;h<=4;h++)
                cin>>aux;
            else for (h=1;h<=4;h++)
            {
                cin>>a[h];
                viz[a[h]]++;
            }
        cin>>k;
        for (g=1;g<=4;g++)
            if (g!=k)
            for (h=1;h<=4;h++)
                cin>>aux;
            else for (h=1;h<=4;h++)
            {
                cin>>aux;
                if (viz[aux]==1)
                    {sol=aux;nr++;}
            }
        for (h=1;h<=4;h++)
                viz[a[h]]--;
        cout<<"Case #"<<i<<": ";
        if (nr==0)
            cout<<"Volunteer cheated!";
        else if (nr==1)
            cout<<sol;
        else cout<<"Bad magician!";
        cout<<'\n';
    }
    cin.close();cout.close();
    return 0;
}
