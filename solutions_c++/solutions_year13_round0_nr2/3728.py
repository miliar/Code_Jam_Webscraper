#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k = 0; k<t; ++k)
    {
        int n, m;
        cin>>n>>m;
        vector< vector<int> > lawnDesire;
        vector< vector<bool> > lawnCut;
        vector<int> hMax(n,0), vMax(m,0);
        for(int i = 0; i<n; ++i)
        {
            vector<int> vec;
            for(int j = 0; j<m; ++j)
            {
                int nn;
                cin>>nn;
                vec.push_back(nn);

                if(hMax[i] < nn)
                {
                    hMax[i] = nn;
                }
                if(vMax[j] < nn)
                {
                    vMax[j] = nn;
                }
            }
            lawnDesire.push_back(vec);
            lawnCut.push_back(vector<bool>(m, false));
        }
        int cont = 0;
        for(int i = 0; i<n; ++i)
        {
            for(int j = 0; j<m; ++j)
            {
                if(!lawnCut[i][j] && lawnDesire[i][j] == hMax[i])
                {
                    lawnCut[i][j] = true;
                    cont++;
                }
            }
        }

        for(int j = 0; j<m; ++j)
        {
            for(int i = 0; i<n; ++i)
            {
                if(!lawnCut[i][j] && lawnDesire[i][j] == vMax[j])
                {
                    lawnCut[i][j] = true;
                    cont++;
                }
            }
        }
        cout<<"Case #"<<k+1<<": ";
        if(cont == n*m)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
