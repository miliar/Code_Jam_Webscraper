#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int n[t];
    double nm[t][10],kn[t][10];
    for(int i=0;i<t;i++)
    {
        cin>>n[i];
        for(int j=0;j<n[i];j++)
        {
            cin>>nm[i][j];
        }
        sort(nm[i], nm[i] + n[i]);
        for(int j=0;j<n[i];j++)
        {
            cin>>kn[i][j];
        }
        sort(kn[i], kn[i] + n[i]);
    }
    for(int i=0;i<t;i++)
    {
        int dw=0;
        int j1=0,j2=0;
        for(int j=0;j<n[i];j++)
        {

            if(nm[i][j1]>kn[i][j2])
            {
                dw++;
                j2++;
            }
            j1++;
        }
        reverse(nm[i], nm[i] + n[i]);
        reverse(kn[i], kn[i] + n[i]);
        int w=0;
        j1=0;
        j2=0;
        for(int j=0;j<n[i];j++)
        {

            if(nm[i][j1]>kn[i][j2])
            {
                w++;
            }
            else
            {
                j2++;
            }
            j1++;
        }
        cout<<"Case "<<"#"<<i+1<<": "<<dw<<" "<<w<<endl;
    }
    return 0;
}

