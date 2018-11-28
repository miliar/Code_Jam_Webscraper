#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<sstream>
using namespace std;
int main()
{
    ifstream ifile;
    ofstream ofile;
    int tc,i,j,smax;
    ifile.open("A-large.in");
    ofile.open("XYZ.txt");
    ifile>>tc;
    for(i=0;i<tc;i++)
    {
        string str;
        int sum=0,cot=0,arr[10000];
        int temp;
        stringstream ss;
        ifile>>smax;
        ifile>>str;

        for(j=0;j<=smax;j++)
        {
            ss<<str.at(j);
            ss>>temp;
            arr[j]=temp;
            ss.str(string());
            ss.clear();

        }

        for(j=0;j<smax;j++)
        {
            sum+=arr[j];
            if(sum<j+1 && arr[j+1]!=0)
            {
                cot=cot + (j+1-sum);
                sum=sum + (j+1-sum);
            }
        }

        ofile<<"Case #"<<(i+1)<<": "<<cot<<endl;
    }
    ifile.close();
    ofile.close();

    return 0;
}
