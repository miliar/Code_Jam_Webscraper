#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int cases,length=0,num=0;
    cin>>cases;
    for(int i=1;i<=cases;i++)
    {
        char stack[100]={NULL};
        cin>>stack;
        length=strlen(stack);
        for(int j=0;j<length-1;j++)
        {
            if(stack[j]!=stack[j+1])
                num++;
        }
        if(stack[length-1]!='+')
            cout<<"Case #"<<i<<": "<<num+1<<endl;
        else
            cout<<"Case #"<<i<<": "<<num<<endl;
        num=0;
        length=0;
    }
    return 0;
}
