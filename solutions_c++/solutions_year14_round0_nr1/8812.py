#include<fstream>
using namespace std;

int main()
{
    int k;
    ifstream a ("q1.txt");
    ofstream b ("a1.txt");
    a>>k;
    for (int i=0; i<k; i++)
    {
        int ans;
        int r1[4];
        int r2[4];
        char x[15];
        a>>ans;
        a.getline(x,15);
        for (int j=1; j<=4; j++)
        {
            if (j!=ans)
            {
                a.getline(x,15);
            }
            if(j==ans)
            {
                a>>r1[0];
                a>>r1[1];
                a>>r1[2];
                a>>r1[3];
                a.getline(x,15);
            }
        }
        a>>ans;
        a.getline(x,15);
        for (int j=1; j<=4; j++)
        {
            if (j!=ans)
            {
                a.getline(x,15);
            }
            if(j==ans)
            {
                a>>r2[0];
                a>>r2[1];
                a>>r2[2];
                a>>r2[3];
                a.getline(x,15);
            }
        }
        int flag=0;
        for (int p=0;p<4;p++)
        {
            for (int q=0;q<4;q++)
            {
                if (r1[p]==r2[q])
                {
                    flag++;
                    ans=r1[p];
                }

            }

        }
        if(flag==0)

            b<<"Case #"<<i+1<<": "<<"Volunteer Cheated!"<<endl;
        else if(flag==1)
            b<<"Case #"<<i+1<<": "<<ans<<endl;
        else
            b<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    }
}
