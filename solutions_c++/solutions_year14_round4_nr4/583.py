#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
ifstream cin ("D-small-attempt1.in");
ofstream cout ("temp.out");
string save[1000];
int w[1000];
int maxl,way;
int m,n;
void work (int node)
{
    if (node==m)
    {
        int total=0;
        bool empty=false;
        for (int i=0;i<n;i++)
        {
            string temp[1000];
            int p=0;
            for (int j=0;j<m;j++)
                if (w[j]==i) {temp[p]=save[j];p++;}
            int many=1;
            int q=1;
            if (p==0) {empty=true;break;}
            while (1)
            {
                bool can=false;
                for (int j=0;j<p;j++)
                {
                    if (q<=temp[j].size())
                    {
                        can=true;
                        bool all=true;
                        for (int x=0;x<j;x++)
                        {
                            if (q<=temp[x].size())
                            {
                                bool same=true;
                                for (int y=0;y<q;y++)
                                    if (temp[j][y]!=temp[x][y]) {same=false;break;}
                                if (same) {all=false;break;}
                            }
                        }
                        if (all) many++;
                    }
                }
                if (can==false) break;
                q++;
            }
            //cout<<"!!"<<many<<endl;
            total+=many;
        }
        //cout<<total<<endl;
        if (!empty)
        {
            if (total>maxl) {maxl=total;way=1;}
            else if (total==maxl) way++;
        }
        return;
    }
    for (int i=0;i<n;i++)
    {
        w[node]=i;
        work (node+1);
    }
}
int main ()
{
    int t;
    cin>>t;
    int i;
    for (i=1;i<=t;i++)
    {
        cin>>m>>n;
        for (int j=0;j<m;j++)
            cin>>save[j];
        maxl=0;way=1;
        work (0);
        cout<<"Case #"<<i<<": "<<maxl<<" "<<way<<endl;
    }
}
