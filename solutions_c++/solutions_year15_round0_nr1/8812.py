#include<iostream>



using namespace std;

long atoi(char x)
{
	long z = (long)x - 48;
	return z;
}


long func(long s,char a[])
{
    long c = atoi(a[0]);
    long d = 0;

    for (long i=1;i<=s;i++)
    {
        if (c < i)
        {
            c++;
            d++;
            i--;
            continue;
        }

        else
        {
            c += atoi(a[i]);
        }

    }

    return d;
}

int main()
{
    long t;
    cin>>t;
    long output[100];

    for (long i=0;i<t;i++)
    {
        long s = 0;
        char a[1010];
        cin>>s;
        cin>>a;
        output[i] = func(s,a);
    }

    for (long i=0;i<t;i++)
        cout<<"case #"<<i+1<<": "<<output[i]<<endl;
}
