#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<bitset>


using namespace std;

int main()
{
    freopen("d:\\Coding\\input.txt","r",stdin);
    freopen("d:\\Coding\\output.txt","w",stdout);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {


        int A[4][4],a1,a2;
        vector<int>v1,v2;

        cin>>a1;

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>A[i][j];
                if(i+1==a1)
                    v1.push_back(A[i][j]);

            }

        cin>>a2;

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>A[i][j];
                if(i+1==a2)
                    v2.push_back(A[i][j]);

            }
        int check=0,ans;
        vector<int>::iterator it;
        for(int i=0;i<4;i++)
        {
            it=find(v2.begin(),v2.end(),v1[i]);
            if(it!=v2.end())
            {
                ans=*it;
                check++;
            }
        }

        if(ii!=1)
            cout<<endl;
        if(check==0)
            cout<<"Case #"<<ii<<":"<<" Volunteer cheated!";
        else if(check==1)
            cout<<"Case #"<<ii<<":"<<" "<<ans;
        else
            cout<<"Case #"<<ii<<":"<<" Bad magician!";

    }

    return 0;
}
