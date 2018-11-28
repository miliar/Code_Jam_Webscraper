#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include<cstring>
#include<fstream>
#include<climits>
using namespace std;
int main()
{
    int test;
    cin>>test;
    ofstream myfile;
      myfile.open ("output.txt");
    for(int a=1; a<=test; a++)
    {
        int ar[4][4];
        int br[4][4];
        int i[4],j[4];
        int w,x,y,z;
        int count=0;
        int first;
        cin>>first;

        for(int p=0; p<4; p++)
        {
            for(int q=0; q<4; q++)
            {
                cin>>ar[p][q];
                if(first==p+1)
                {
                    i[q]=ar[p][q];
                }
            }

        }
        int second;
        cin>>second;
        for(int p=0; p<4; p++)
        {
            for(int q=0; q<4; q++)
            {
                cin>>br[p][q];
                if(second==p+1)
                {
                    j[q]=br[p][q];
                }
            }

        }
        int ans;
        for(int v=0;v<4;v++)
        {
            for(int n=0;n<4;n++)
            {
                if(i[v]==j[n])
                {
                    //cout<<i[v]<<endl;
                    count++;
                    ans=i[v];
                }
            }
        }
        cout<<"Case #"<<a<<": ";
        myfile <<"Case #"<<a<<": ";
        if(!count)
            {cout<<"Volunteer cheated!\n"; myfile<<"Volunteer cheated!\n";}
        else if(count==1)
            {cout<<ans<<endl;myfile<<ans<<endl;}
        else if(count>1)
            {cout<<"Bad magician!\n"; myfile<<"Bad magician!\n";}


    }
     myfile.close();
     return 0;
}
