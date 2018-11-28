#include<fstream>
#include<algorithm>

using namespace std;

int main()
{
    ifstream fr;
    ofstream fw;
    fr.open("D-large.in");
    fw.open("C-small.out");
    int t;
    fr>>t;
    double na[1001],ken[1001];
    int y,z,n,p,q,r;
    for(int i=1;i<=t;i++)
    {
        y=z=0;
        fr>>n;
        for(int j=0;j<n;j++)
            fr>>na[j];
        sort(na,na+n);
        for(int j=0;j<n;j++)
            fr>>ken[j];
        sort(ken,ken+n);

        p=n-1;q=0;r=n-1;
        for(;p>=0;p--)
        {
            if(na[p]>=ken[r])
            {
                z++;
                q++;
            }
            else
                r--;
        }

        p=n-1;q=0;r=n-1;
        for(;p>=0;p--)
        {
            if(ken[p]>=na[r])
                q++;
            else
            {
                y++;
                r--;
            }
        }
        fw<<"Case #"<<i<<": "<<y<<" "<<z<<endl;

    }

    return 0;
}
