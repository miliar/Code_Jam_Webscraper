/*
 * File:   main.cpp
 * Author: Jon la Cour
 *
 * Created on April 26, 2013, 8:22 PM
 */

#include<fstream>
#include<sstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>

using namespace std;

int main()
{
    int t,temp1,e,r,n;
    int ans[11][5],v[10];

    cin>>t;

    ans[0][0]=0;
    ans[0][1]=0;
    ans[0][2]=0;
    ans[0][3]=0;
    ans[0][4]=0;

    for (int i = 0; i < t; i++)
    {
        cin>>e>>r>>n;
        for(int j=1; j<=n; j++)
        {
            cin>>v[j-1];
            for(int k=0; k<=e-r; k++)
            {
                ans[j][k]=0;
                int l=0;
                if(k>r)
                    l=k-r;
                for(; l<=e-r; l++)
                {
                    if(ans[j-1][l]+v[j-1]*(l+r-k)>ans[j][k])
                        ans[j][k]=ans[j-1][l]+v[j-1]*(l+r-k);
                }
            }
        }

        fstream filestr;
        filestr.open ("output.txt", fstream::in | fstream::out | fstream::app);

        std::ostringstream s;
        s << "Case #" << i+1 << ": " << ans[n][0];
        std::string result = s.str();

        filestr<<result<<endl;
        filestr.close();
    }
    return 0;
}
