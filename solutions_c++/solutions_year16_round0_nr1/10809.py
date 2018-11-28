#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,i,j,n;

    ofstream myfile;
    myfile.open("1.txt");

    cin>>t;

    for(int k=1;k<=t;k++)
    {
        cin>>n;

        int arr[15]={0};

        if(n==0)
        {
            myfile<<"Case #"<<k<<": INSOMNIA"<<endl;
            continue;
        }

        for(int i=1;;i++)
        {
            n=n*i;
            int temp=n;

            while(temp!=0)
            {
                int r=temp%10;

                arr[r]=1;

                temp=temp/10;
            }

            int flag=0;
            for(int j=0;j<10;j++)
            {
                if(arr[j]==1)
                flag++;
            }

            if(flag==10)
            {
                myfile<<"Case #"<<k<<": "<<n<<endl;
                break;
            }

            n=n/i;
        }
    }
    myfile.close();
    return 0;
}
