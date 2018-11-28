#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int arr[4][4],arr1[4][4];
    int t,x,n,m;
    ifstream in("A-small-attempt0.in");
    ofstream out("out1.txt");
    in>>t;
    x=t;
    while(t-->0)
    {
        in>>n;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            in>>arr[i][j];
        }
        in>>m;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            in>>arr1[i][j];
        }
        int cnt=0,num=-1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(arr[n-1][i]==arr1[m-1][j])
                {
                    cnt++;
                    num=arr[n-1][i];
                }

            }
        }
        if(cnt==1)
        out<<"Case #"<<x-t<<": "<<num<<endl;
        else if(cnt>1)
        out<<"Case #"<<x-t<<": Bad magician!"<<endl;
        else
        out<<"Case #"<<x-t<<": Volunteer cheated!"<<endl;
    }
}
