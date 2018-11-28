#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int t,n,m,ar[200][200],maxr[200],maxc[200],flag,i,j,p=0;
ifstream fin("B-large.in");
ofstream fout("output.txt");
fin>>t;
while(t--)
{
    flag=0;
    fin>>n>>m;

    for(i=0;i<n;i++)
    maxr[i]=0;
    for(j=0;j<m;j++)
    maxc[j]=0;
    for(i=0;i<n;i++)
    for(j=0;j<m;j++)
    {
       fin>>ar[i][j];
       if(maxr[i]<ar[i][j])
       maxr[i]=ar[i][j];
       if(maxc[j]<ar[i][j])
       maxc[j]=ar[i][j];
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(((ar[i][j])<maxr[i])&&(ar[i][j]<maxc[j]))
            flag=1;
        }

}
p++;
if(flag==1)
fout<<"Case #"<<p<<": "<<"NO"<<endl;
else
fout<<"Case #"<<p<<": "<<"YES"<<endl;
}
return 0;
}
