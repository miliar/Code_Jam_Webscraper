#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    ofstream out;
    int count=1;
    out.open("output.txt");
    ifstream ini;
    ini.open("input4.in");
    int t;
    ini>>t;

    //while(ini)
    //for(int m=1;m<=100;m++)
    while(t>0)
    {

    long long int n;
    ini>>n;
    int arr[10]={0,1,2,3,4,5,6,7,8,9};

     int num=0;
     long long int i=1;
    while(1)
    {
        if(n==0)
        {
            //cout<<endl<<"INSOMNIA";
            cout<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
            out<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
            count++;
            break;

        }
       long long  int n1=i*n;
        while(n1>0)
        {
            int d=n1%10;
            n1=n1/10;
            for(int j=0;j<10;j++)
            {
                if(arr[j]==d)
                {
                    arr[j]=21;
                    num=num+1;
                }
            }

        }
        if(num==10)
        {
            cout<<"Case #"<<count<<": "<<i*n<<endl;
            out<<"Case #"<<count<<": "<<i*n<<endl;
            count++;
            break;
        }
        else{
            i=i+1;
        }


    }
    t--;

    }

    return 0;
}
