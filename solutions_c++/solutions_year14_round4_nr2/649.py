#include<fstream>
#include<algorithm>
using namespace std;
ifstream cin ("B-large.in");
ofstream cout ("temp.out");
int main ()
{
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        int save[1010];
        bool use[1010];
        for (int j=0;j<n;j++)
        {
           cin>>save[j];
           use[j]=false;
        }
        int ans=0;
        int begin=0,end=n-1;
        for (int j=0;j<n-1;j++)
        {
            int minl=-1;
            for (int x=begin;x<=end;x++)
                if (!use[x])
                    if (minl==-1||save[minl]>save[x]) minl=x;
            if (minl-begin>end-minl)
            {
                ans+=end-minl;
                for (int x=minl;x<end;x++) save[x]=save[x+1];
                end--;
            }
            else
            {
                ans+=minl-begin;
                for (int x=minl;x>begin;x--) save[x]=save[x-1];
                begin++;
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
}
