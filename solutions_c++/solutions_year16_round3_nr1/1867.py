#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <sstream>
#include <algorithm>


using namespace std;
vector<int> v;
vector<char> b(26);
int a1,a2;
int n;
 int ind1=0,ind2=0;

int szum()
{
  int sum=0;
    for(int i=0; i<n && sum<4; ++i)
    {
        sum+=v[i];
    }
    return sum;
}
bool kivesz()
{
    int sum=0;
    for(int i=0; i<n && sum<4; ++i)
    {
        sum+=v[i];
    }
    if(sum==3)
    {
        return false;
    }
    int max=0;

    for(int i=0; i<n; ++i)
    {
        if(v[i]>max)
        {
            max=v[i];ind1=i;
        }
    }
    v[ind1]--;
    max=0;
    for(int i=0; i<n; ++i)
    {
        if(v[i]>max)
        {
            max=v[i]; ind2=i;
        }
    }
    v[ind2]--;
    cout<<b[ind1]<<b[ind2]<<" ";
    if(szum()==0) return false;
    return true;

}
int main()
{
    b[0]='A';
    b[1]='B';
    b[2]='C';
    b[3]='D';
    b[4]='E';
    b[5]='F';
    b[6]='G';
    b[7]='H';
    b[8]='I';
    b[9]='J';
    b[10]='K';
    b[11]='L';
    b[12]='M';
    b[13]='N';
    b[14]='O';
    b[15]='P';
    b[16]='Q';
    b[17]='R';
    b[18]='S';
    b[19]='T';
    b[20]='U';
    b[21]='V';
    b[22]='W';
    b[23]='X';
    b[24]='Y';
    b[25]='Z';


    freopen("5.txt","r",stdin);
    freopen("ki2.txt","w",stdout);

    int tt;
    cin>>tt;
    for(int tn=1; tn<=tt; ++tn)
    {
           cout<<"Case #"<<tn<<": ";

        cin>>n;
        v.clear();
        v.resize(n);
        for(int i=0; i<n; ++i) cin>>v[i];
        while(kivesz())
        {

        }
        if (szum()==3)
        {
            vector<int> w;
            bool l=false;
            int ind=-1;
            for(int i=0; i<n; ++i)
            {

                if(v[i]==2)
                {
                    cout<<b[i]<<" ";
                    l=true;
                    ind=i;
                }
                if(v[i]==1)
                {
                    w.push_back(i);
                }
            }
            if(l)
            {
                cout<<b[w[0]]<<b[ind];
            }
            else
            {
                cout<<b[w[0]]<<" ";
                cout<<b[w[1]]<<b[w[2]];
            }
        }






        cout<<endl;
    }


    return 0;
}
