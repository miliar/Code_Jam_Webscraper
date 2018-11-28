#include <iostream>
#include <fstream>
using namespace std;

int main()
{
     ofstream write;
    write.open ("file.out");

    ifstream read("B-small-attempt0.in");
    int t;
    read>> t;
    for(int k=1;k<=t;k++)
    {
        int n,m;
        read >>n;
        read >>m;
        int arr[n][m];
        int arr2[n][m];
        for(int i=0;i<n;i++)
        {
            int max=0;
            for(int j=0;j<m;j++)
            {
                read>>arr[i][j];
                if(arr[i][j]>max)
                {
                    max=arr[i][j];
                }
            }
            for(int j=0;j<m;j++)
            {
                arr2[i][j]=max;
            }
        }
        bool correct=true;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]!=arr2[i][j])
                {
                    for(int k=0;k<n;k++)
                    {
                        arr2[k][j]=arr[i][j];
                    }
                }
            }
        }
        for(int i=0;i<n&&correct==true;i++)
        {
            for(int j=0;j<m&&correct==true;j++)
            {
                if(arr[i][j]!=arr2[i][j])
                {
                    correct=false;
                }
            }
        }
        if(correct==true)
        {
            write<<"Case #"<<k<<": YES"<<endl;
        }
        else
        {
            write<<"Case #"<<k<<": NO"<<endl;
        }
    }
    write.close();
    return 0;
}
