#include <iostream>
#include <cmath>
using namespace std;

void check();
int nextPal(int num);
bool isPal(int num);
int main()
{
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++)
    {
        cout<<"Case #"<<i<<": ";
        check();
    }
}

void check()
{
    int n,m;
    cin>>n>>m;
    int count=0;
    int x=0;
    x=sqrt(n);
    if(x*x<n)
        x++;
    if(!isPal(x))
        x=nextPal(x);
    while(x*x<=m)
    {
        if(isPal(x*x))
        {
         count++;
        }
        x=nextPal(x);
    }
    cout<<count<<'\n';
}

int nextPal(int num)
{
    do{
        num++;
    }while(!isPal(num));
    return num;
}

bool isPal(int num)
{
    if(num<10)
        return true;
    int x=num, count=1;
    while(x>=10)
        {
            x/=10;
            count++;
        }
    int array[count];
        x=num;
        for(int i=0;i<count;i++)
        {
            array[i]=x%10;
            x/=10;
        }
            for(int i=0;i<count/2;i++)
        {
            if(array[i]!=array[(count-1)-i])
                return false;
        }
    return true;
}
