#include<iostream>
using namespace std;
int main()
{
    long int number,tempnum,ans;
    int testcases,temp,count=0,i,k=0;
    int check[10];
    cin>>testcases;
    while(testcases--)
    {
        cin>>number;
        k++;
        if(number==0)
        {
              cout<<"Case #"<<k<<": INSOMNIA"<<endl;
              continue;
        }

        for(int j=0;j<10;j++) check[j] = 0;

        i=0,count=0;

        while(count!=10)
        {
            i++;

            tempnum = number*i;
            ans = tempnum;
            while(tempnum>0)
            {
                temp = tempnum%10;
                tempnum = tempnum/10;
                if(check[temp]!=1)
                {
                    check[temp] = 1;
                    count++;
                    if(count==10) break;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
return 0;
}
