#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream gin("input.txt");
    ofstream gout("output.txt");
    int t;
    gin>>t;
    int cas=0;
    while(t--)
    {
        cas++;
        int data1[5];
        int data2[5];
        int n,x;
        gin>>n;
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                if(n==i)gin>>data1[j];
                    else gin>>x;
            }
        }
        gin>>n;
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                if(n==i)gin>>data2[j];
                    else gin>>x;
            }
        }
        int f=0;
        int ans=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;++j)
            {
                if(data1[i]==data2[j]){++f,ans=data1[i];break;}
            }
        }
        if(f==0)gout<<"Case #"<<cas<<": Volunteer cheated!"<<endl;
        else if(f==1)gout<<"Case #"<<cas<<": "<<ans<<endl;
        else if(f>=2)gout<<"Case #"<<cas<<": Bad magician!"<<endl;
    }
}
