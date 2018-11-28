#include<iostream>
#include<fstream>

using namespace std;
int main()
{

int arr[6]={1,4,9,121,484};
    ifstream input("input.txt");

    ofstream myfile;
    myfile.open ("outputttt.txt");
    int t;
    int pop=0;
    input>>t;
    while(t--)
    {
        int a,b,m=0,n=0;
        input>>a>>b;
        for(int i=0;i<5;i++)
        {
        if(arr[i]>=a)
        {
        m=i;
        break;
        }
        }

        //cout<<m;
        for(int j=4;j>=0;j--)
        {
            if(arr[j]<=b)
            {
                n=j;
                break;
            }
        }
       // cout<<" "<<n<<" ";
       if(a>484)
       myfile<<"Case #"<<(++pop)<<": "<<0<<endl;
        else
        myfile<<"Case #"<<(++pop)<<": "<<(n-m+1)<<endl;
        }

    }

