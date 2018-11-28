#include<iostream>
#include<string.h>
using namespace std;

int main()
{
    int test,k=1;

    cin>>test;

    while(test--)
    {
        int a=0,s=0,count1=0;
        char A[100];

        cin>>A;

        for(int i=0;i<strlen(A);i++)
        {
            if(A[i]=='-')
                s++;
            else
                a++;
        }

        if(a==strlen(A))
        {
            count1=0;
            cout<<"Case #"<<k<<": "<<count1<<endl;
            //cout<<"test1"<<endl;
        }

        else if(s==strlen(A))
        {
            count1=1;
            cout<<"Case #"<<k<<": "<<count1<<endl;
            //cout<<"test2"<<endl;
        }

        else
        {
            //cout<<"test3"<<endl;
            char current,previous;
            int cur=0,pre=0,add=0,sub=0;

            for(int i=1;i<strlen(A);i++)
            {
                current=A[i];
                cur=i;
                pre=i-1;
                previous=A[i-1];

                if(current!=previous)
                {
                    //cout<<"test4"<<endl;
                    for(int j=0;j<=pre;j++)
                    {
                        A[j]=current;
                    }
                    count1++;
                }

                //cout<<A<<"test"<<endl;
                add=0;
                sub=0;
                for(int w=0;w<strlen(A);w++)
                {
                    //cout<<"test5"<<endl;
                    if(A[w]=='-')
                        sub++;
                    else
                        add++;
                }

                //cout<<"test6"<<endl;
                //cout<<add<<endl;
                //cout<<sub<<endl;
                if(add==strlen(A))
                {
                    cout<<"Case #"<<k<<": "<<count1<<endl;
                    break;
                }

                else if(sub==strlen(A))
                {
                    cout<<"Case #"<<k<<": "<<count1+1<<endl;
                    break;
                }
            }
        }
        k++;
    }
}
