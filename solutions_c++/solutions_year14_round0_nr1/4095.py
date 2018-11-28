#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout("output.txt");
    int test;
    cin>>test;
    int kase=0;


    while(test--)
    {




        kase++;
        int aray_1[5];
        int data_2[5];


        int n,x;
        cin>>n;
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                if(n==i)cin>>aray_1[j];
                    else cin>>x;
            }
        }
        cin>>n;



        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                if(n==i)cin>>data_2[j];
                    else cin>>x;
            }
        }



        int fre=0;


        int nswer=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;++j)
            {
                if(aray_1[i]==data_2[j]){++fre,nswer=aray_1[i];break;}
            }
        }
        if(fre==0)fout<<"Case #"<<kase<<": Volunteer cheated!"<<endl;
        else if(fre==1)fout<<"Case #"<<kase<<": "<<nswer<<endl;
        else if(fre>=2)fout<<"Case #"<<kase<<": Bad magician!"<<endl;
    }
}
