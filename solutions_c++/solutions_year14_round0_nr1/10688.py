#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t,a,b,aux,ini,cont;
    vector <int> grid1;
    vector <int> grid2;
    cin>>t;
    for(int c=0;c<t;c++)
    {
        grid1.clear();
        grid2.clear();
        //read input
        cin>>a;
        ini=4*(a-1);
        for(int d=0;d<16;d++)
        {
            cin>>aux;
            if (d>=ini  && d<ini+4) grid1.push_back(aux);
        }
        cin>>b;
        ini=4*(b-1);
        for(int d=0;d<16;d++)
        {
            cin>>aux;
            if (d>=ini  && d<ini+4) grid2.push_back(aux);
        }
        //analysis
        cont=0;
        for(int d=0;d<4;d++)
        {
            for(int e=0;e<4;e++)
            {
                if (grid2[e]==grid1[d]) {cont++;a=grid1[d];}
            }
        }
        cout<<"Case #"<<c+1<<": ";
        if (cont==1) cout<<a;
        if (cont>1) cout<<"Bad magician!";
        if (cont<1) cout<<"Volunteer cheated!";
        cout<<endl;

    }
    return 0;

}
