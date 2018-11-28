#include <math.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main()
{

    ifstream fin("D-large (2).in");
    ofstream fout("LargeAlyyyyyyy.txt");
    int T;
    float *arr1,*arr2;
    fin>>T;
    for(int t=1; t<=T; t++)
    {
        int war=0,dwar=0;
        int n;

        fin>>n;
        arr1=new float[n];
        arr2=new float[n];
        for(int i=0; i<n; i++)
            fin>>arr1[i];

        for(int i=0; i<n; i++)
            fin>>arr2[i];

        sort(arr1,arr1+n);
        sort(arr2,arr2+n);



        int j=0;
        for(int i=0; i<n; i++)
        {
            if(arr1[i]>arr2[j]){
                dwar++;
                j++;
            }


        }

        j=0;
        for(int i=n-1; i>=0; i--)
        {
            if(arr1[i]>arr2[n-j-1])
                war++;
            else
                j++;
        }
        fout<<"Case #"<<t<<": "<<dwar<<" "<<war<<endl;

    }
    return 0;
}
