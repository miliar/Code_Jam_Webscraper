#include <iostream>
#include <deque>
#include <sstream>
#include <stdio.h>
#include <cstdlib>

using namespace std;
bool insom = true;
int main()
{
    int cases; deque <int> test; int temp;
    cin>>cases;
    for(int i =0; i<cases; i++)
    {
        cin>>temp;
        test.push_back(temp);
    }
    int a;
    for(int i =0; i<test.size(); i++)
    {
        int n=test[i]; int sum; int sum2;
        int arr[10]={0,0,0,0,0,0,0,0,0,0};
        for(int count=1;count<200;count++)
        {

            sum=count*n;
            sum2=sum;
            while(sum)
            {
                a=sum%10;
                //cout<<"index:"<<a<<endl;
                arr[a]=1;
                sum/=10;
            }
            //cout<<"sum:"<<sum<<endl;
            //for(int index=0;index<10;index++)
           // {
              //  cout<<arr[index];
            //}
            //cout<<endl;
            bool reached = true;
            for(int index=0;index<10;index++)
            {
                if(arr[index]!=1)
                {
                    reached = false;
                    break;
                }
            }
            if(reached)
                {printf("Case #%d: %d",i+1,sum2);
                    insom = false;
                    break;}
        }

            if(insom)
                printf("Case #%d: INSOMNIA",i+1);
            cout<<endl;
    }
   // cout << "Hello world!" << endl;
    return 0;
}

