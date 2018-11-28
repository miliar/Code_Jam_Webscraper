#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T=0;
    cin>>T;
    vector<double> me(1000,1.0);
    vector<double> him(1000,1.0);
    for(int icaseInd=1; icaseInd<=T; ++icaseInd)
    {
        int num;
        cin>>num;
        for(int i=0; i<num; ++i)
        {
            cin>>me[i];
        }
        for(int i=0; i<num; ++i)
        {
            cin>>him[i];
        }
        sort(me.begin(),me.begin()+num);
        sort(him.begin(),him.begin()+num);
        int numCheat=0;
        int numNoCheat=0;
        int j=num-1;
        for(int i=num-1;i>=0;--i)
        {
            if(me[i]>him[j])
            {
                ++numNoCheat;
            }else if(me[i]==him[j])
                {
                   ++numNoCheat;
                   --j;
                   --i;
            }else
            {
                --j;
            }
        }
        j=num-1;
        for(int i=num-1; i>=0; --i)
        {
            while(j>=0&&me[i]<=him[j])
            {
                --j;
            }
            if(j>=0&&me[i]>him[j])
                ++numCheat;
            --j;
        }
        cout<<"Case #"<<icaseInd<<": "<<numCheat<<" "<<numNoCheat<<"\n";
    }
    return 0;
}
