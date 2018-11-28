#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int cases, input;
    int i,j,k;
    int count=0;
    int clone;
    int number;
    j=0;
    int l;
    std::string str;

    cin>>cases;
    number=cases;
    int output[cases];
    for(i=0;i<cases;i++)
    {
        output[i]=0;
    }
        while(cases--)
        {
        cin>>input>>str;
        count=0;
        for(k=0;k<=input;k++)
        {
            if(count>=k)
            {
                count+=(str[k]-'0');
            }
            else
                {
                clone=k-count;
                output[j]+=clone;
                count+=clone;
                count+=(str[k]-'0');
                }
        }
        j++;
        }
        for(l=0;l<number;l++)
        cout<<"Case #"<<l+1<<": "<<output[l]<<"\n";
    return 0;
}

