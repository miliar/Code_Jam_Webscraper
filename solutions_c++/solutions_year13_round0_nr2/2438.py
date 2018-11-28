#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>
#include <locale>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main(void)
{
    ofstream cout ("B-large.out");
    ifstream cin ("B-large.in");
    int T;
    int N,M;
    int a[100][100];
    int rowmax[100];
    int colmax[100];
    int i,j,k;
    string ans;
    bool stat;
    cin>>T;
    for(k=1;k<=T;k++)
    {
        stat=true;
        ans="";
        cin>>N>>M;
        for(i=0;i<N;i++)    rowmax[i]=0;
        for(i=0;i<M;i++)    colmax[i]=0;
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                cin>>a[i][j];
                rowmax[i]=max(a[i][j],rowmax[i]);
            }
        }
        for(i=0;i<M;i++)
        {
            for(j=0;j<N;j++)
            {
                colmax[i]=max(a[j][i],colmax[i]);
            }
        }
        //for(i=0;i<M;i++)    cout<<colmax[i]<<" ";
        //cout<<"\n";
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                if((a[i][j]<rowmax[i])&&(a[i][j]<colmax[j]))
                {
                    stat=false;
                    break;
                }
            }
            if(!stat)   break;
        }
        if(stat)    ans="YES";
        else        ans="NO";
        cout<<"Case #"<<k<<": "<<ans<<"\n";
    }
    return 0;
}
