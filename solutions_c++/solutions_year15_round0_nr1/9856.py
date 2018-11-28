#include<iostream>
using namespace std;
int main()
{

int T,s;
char st[1005];

cin>>T;
for(int i=0;i<T;i++)
{
    cin>>s;
    cin>>st;
    int count=0;
    int result=0;
    for(int j=0;j<=s;j++)
    {
        if(count>=j)
        count=count + (st[j]-'0');
        else {
        int x=j-count;
        result=result+x;
        count=count + (st[j]-'0')+x;
        }
        if(count>=9)
        break;

    }
    cout<<"Case #"<<i+1<<": "<<result<<endl;
}

}
