#include<iostream>
using namespace std;

int main()
{
    int A[10],t,num,temp,flag=0,j;

    cin>>t;
    int k=1;
    while(t--)
    {
        cin>>num;

        if(num==0)
        {
            cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
        }

        else
        {
            for(int i=0;i<10;i++)
            {
                A[i]=0;
            }

            flag=-10;
            for(j=1;;j++)
            {
                //cout<<num<<"a"<<endl;
                temp=j*num;
                int temp1 = temp;
                //cout<<temp<<"b"<<endl;
                while(temp!=0)
                {
                    int a=temp%10;
                    //cout<<a<<endl;
                    A[a]=1;
                    temp=temp/10;
                }

                for(int k=0;k<10;k++)
                {
                    if(A[k]==0)
                    {
                        flag=-10;
                        break;
                    }

                    else
                    {
                        flag=0;
                    }
                }

                //cout<<flag<<"test"<<endl;
                if(flag==0)
                {
                    cout<<"Case #"<<k<<": "<<temp1<<endl;
                    break;
                }

                if(j>100000 &&  flag==-10)
                {
                    cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
                }
            }
        }
        k++;
    }
}
