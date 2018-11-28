#include <iostream>
#include <fstream>
using namespace std;

int main(int argc,char ** argv)
{

    int tcase;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin >> tcase;
    int a[100][100];
    for (int t=0; t<tcase; t++)
    {
        int m,n;
        cin >> m;
        cin >> n;
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
                cin >> a[i][j];
        }
        cout << "Case #" << t+1 << ": "; 

        bool col[100];
        bool row[100];
        
        for (int i=0; i<m; i++)
        {
            row[i]=true;
        }
        for (int j=0; j<n; j++)
        {
            col[j]=true;
        }

        
        int count=0;
        int mm=m; int nn=n;


        while (mm>0 && nn>0)
        {

        int min=100;
        int mini=0;
        int minj=0;

        bool flag1=true, flag2=true;


        for (int i=0; i<m; i++)
        {
            if (row[i])
            {
                for (int j=0; j<n; j++)
                {
                    if(col[j] && a[i][j] < min)
                    {
                        min=a[i][j];
                        mini=i;
                        minj=j;
                    }
                }
            }
        }
        for (int i=0; i<m; i++)
        {
            if (row[i] && col[minj] && a[mini][minj]!=a[i][minj])
            {
                flag1=false;
                break;
            }
        }
        if (flag1)
        {
            col[minj]=false;
            nn--;
        }
        for (int j=0; j<n; j++)
            {
                if (row[mini] && col[j] && a[mini][minj]!=a[mini][j])
                {
                    flag2 = false;
                    break;
                }
            }
        if (flag2)
        {
            row[mini]=false;
            mm--;
        }
        if (!flag1 && !flag2)
        {
            cout << "NO" << endl;
            break;
        }
        }
        if (mm==0 || nn==0)
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}
