#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    //ifstream in ("A-small-attempt0.in");
    //ofstream out("A-small-attempt0.out");
    int t,c=1;
    cin>>t;
    while(t--)
    {
        int n,m,r=0,i=2,x=0,b;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<c<<": "<<"Insomnia"<<endl;
        }
        else
        {
            b=n;
            int arr[10]={10,10,10,10,10,10,10,10,10,10};
            int arr1[10]={0,1,2,3,4,5,6,7,8,9};
            while(x!=10)
            {
                if(arr[0]!=arr1[0] || arr[1]!=arr1[1] || arr[2]!=arr1[2] || arr[3]!=arr1[3] || arr[4]!=arr1[4] || arr[5]!=arr1[5] || arr[6]!=arr1[6] || arr[7]!=arr1[7] || arr[8]!=arr1[8] || arr[9]!=arr1[9])
                {
                    m=b;
                    while(m!=0)
                    {
                        r=m%10;
                        arr[r]=r;
                        m=m/10;
                    }
                    b=i*n;
                    i++;
                }
                else
                {
                    x=10;
                }
            }
            cout<<"Case #"<<c<<": "<<b-n<<endl;
        }
        c++;
    }
    return 0;
}
