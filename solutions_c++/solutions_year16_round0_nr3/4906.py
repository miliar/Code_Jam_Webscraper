#include <iostream>

using namespace std;
int t,n,j;

int main()
{
    int temp;
    unsigned long flag=1;
    cin>>t>>n>>j;

    for(int i=1;i<=t;i++)
    {
        temp=0;

        cout<< "Case #"<<i<<":"<<endl;







           for(int k=0;k<j;k++,temp++)
           {
               cout<<"11";
                for(int k=0;k<(n-4)/2;k++)
                {
                    if((flag<<k)&temp)
                        cout<<"11";
                    else
                        cout<<"00";
                }
                cout<<"11"<<" 3 4 5 6 7 8 9 10 11"<<endl;
           }


    }

}
