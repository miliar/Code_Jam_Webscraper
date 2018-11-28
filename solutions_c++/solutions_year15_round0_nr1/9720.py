#include<iostream>
#include<fstream>
using namespace std;
ifstream in("aa.in");
int main()
{

    ofstream out("output.txt");
    int func(int);
    int i,t;
    in>>t;
    int ans[102];
    for(i=0; i<t; i++)
        ans[i]=func(i);
    for(i=0; i<t; i++)
    {
        out<<"Case #"<<i+1<<": "<<ans[i]<<'\n';
        cout<<"Case #"<<i+1<<": "<<ans[i]<<'\n';
    }
    return 0;

}

int func(int i)
{
    int max_s,temp,count=0,no_of_s=0,no_of_p_add=0;
    char str[80];
    in>>max_s;
    in>>str;
    while(count<=max_s)
    {
        temp=(int)(str[count]-'0');
        if(temp!=0)
    {
        if(no_of_s>=count&&temp)
                no_of_s+=temp;
            else
            {
                no_of_p_add+=count-no_of_s;
                no_of_s+=no_of_p_add;
                continue;
            }
        }
        count++;
    }
    return no_of_p_add;
}
