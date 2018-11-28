#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main()
{
    std::ifstream myfile("D-large.in");
    std::ofstream myfile2("output.txt");
    int t;
    myfile>> t;
    for(int i=0;i<t;i++)
    {
        int n;
        myfile>> n;
        double a[n],b[n];
        for(int j=0;j<n;j++)
        {
            myfile>> a[j];
        }
        for(int j=0;j<n;j++)
        {
            myfile>> b[j];
        }

        std::sort(a,a+n);
        std::sort(b,b+n);
        int count1=0,count2=n;
        int j=0,k=0;
        while(j<n)
        {
            if(a[j]<b[k])
            {
                j++;
            }
            else
            {
                count1+=1;
                j++;
                k++;
            }
        }
        j=0;k=0;
        while(j<n)
        {
            if(a[k]<b[j])
            {
                k++;
                j++;
                count2-=1;
            }
            else
            {
                j++;
            }
        }
        myfile2<<"Case #"<<(i+1)<<": "<<count1<<" "<<count2<<"\n";
    }
    myfile.close();
    myfile2.close();
    return 0;
}
