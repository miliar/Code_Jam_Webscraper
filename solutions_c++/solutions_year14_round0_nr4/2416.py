#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<algorithm>
using namespace std;
double arr1[1000],arr2[1000];
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("D-large.in");
    f2.open("output.out");
    int it=1,t,n,count_war,count_dewar;
    f1>>t;
    while(it<=t)
    {
                count_war = count_dewar = 0;
                f1>>n;
                for(int i=0;i<n;i++)f1>>arr1[i];
                for(int i=0;i<n;i++)f1>>arr2[i];
                sort(arr1,arr1+n);
                sort(arr2,arr2+n);
                for(int i=0,j=0;i<n && j<n;)
                {
                        if(arr1[i]<arr2[j])
                        {
                                           count_war++;i++;j++;
                                           }
                        else j++;
                        }
                count_war = n-count_war;
                for(int i=n-1,j=n-1;i>=0 && j>=0;)
                {
                        if(arr1[i]>arr2[j])
                        {
                                           count_dewar++;i--;j--;
                                           }
                        else j--;
                        }
                f2<<"Case #"<<it++<<": "<<count_dewar<<" "<<count_war<<endl;
                }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
