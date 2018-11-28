#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int zc;
    cin>>zc;
    for(int tc=1;tc<=zc;tc++)
    {
        int first, second, tmp, row1[4], row2[4],flag=-2;
        cin>>first;
        string str;
        for(int i=0;i<(first-1)*4;i++)
            cin>>tmp;
        for(int i=0;i<4;i++)
        {
            cin>>row1[i];
        }
        for(int i=first*4;i<4*4;i++)
            cin>>tmp;
        cin>>second;
        for(int i=0;i<(second-1)*4;i++)
            cin>>tmp;
        for(int i=0;i<4;i++)
        {
            cin>>row2[i];
            for(int j=0;j<4;j++)
                if(row2[i]==row1[j])
                    if(flag>=0)
                        flag=-1;
                    else if(flag==-2)
                        flag=i;
        }
        for(int i=second*4;i<4*4;i++)
            cin>>tmp;
        if(flag>=0)
            cout<<"Case #"<<tc<<": "<<row2[flag]<<endl;
        else if(flag==-1)
            cout<<"Case #"<<tc<<": "<<"Bad magician!"<<endl;
        else
            cout<<"Case #"<<tc<<": "<<"Volunteer cheated!"<<endl;
    }
}
