#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        int n; IF >> n;
        int arr[3000]={0},x;
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                IF >> x; arr[x]++;
            }
        }
        OF << "Case #" << tt << ": ";
        for(int i=0;i<3000;i++)
        {
            if(arr[i]&1)
                OF << i << " ";
        }
        OF << endl;
    }
    OF.close(); IF.close();
}


