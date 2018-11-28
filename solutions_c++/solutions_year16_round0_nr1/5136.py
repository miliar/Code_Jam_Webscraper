#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

bool number[10];

bool isSleep()
{
    for (int i = 0; i < 10; i++)
    {
        if (number[i]==false)
            return false;
    }
    return true;
}

void cntNumber(int n)
{
    while(n > 0)
    {
        int x = n%10;
        n/=10;
        number[x] = true;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int i = 1; i <=T;i++)
    {
        memset(number,0,sizeof number);
        int n;
        cin>>n;
        if (n == 0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        int temp = n;
        cntNumber(temp);
        while(!isSleep())
        {
            temp+=n;
            cntNumber(temp);
        }
        cout<<"Case #"<<i<<": "<<temp<<endl;
    }



    fclose(stdin);
    fclose(stdout);
}
