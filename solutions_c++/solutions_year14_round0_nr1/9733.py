#include <string>
#include <vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<sstream>
#include<stack>
#include<queue>
#include<set>
#include <fstream>
using namespace std;

int main()
{
    int T;
    int k=1;
    cin>>T;
    while(T--)
    {
        int c1,c2;
        cin>>c1;
        int a[5][5];
        int b[5][5];
        for(int i=1;i<5;i++)
            for(int j=1;j<5;j++)
                cin>>a[i][j];
        cin>>c2;
        for(int i=1;i<5;i++)
            for(int j=1;j<5;j++)
                cin>>b[i][j];
        int candidates = 0;
        int s=0;
        for(int i=1;i<5;i++)
        {
            for(int j=1;j<5;j++)
            {
                if(a[c1][i]==b[c2][j]){
                    candidates++;
                    s=i;
                    }
            }
        }
        cout<<"Case #"<<k++<<": ";
        if(candidates>1)   
            cout<<"Bad magician!";
        else if(candidates==1)
            cout<<a[c1][s];
        else
            cout<<"Volunteer cheated!";
        cout<<endl; 
    }
    return 0;
}