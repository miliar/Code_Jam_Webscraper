#include <iostream>
#include<fstream>

using namespace std;
int check(bool a[])
{
    int f=1;
    for (int i=0;i<10;i++)
    {
        if(a[i]==false)
        {
            f=0;
            return f;
        }
    }
    return f;
}
int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in>>t;
    int e=t;
    while(t--)
    {
        bool num[10]={false};
        long long int n ;
        in>>n;

        int r;
        if (n==0)
        {
             out<<"Case #"<<e-t<<": INSOMNIA"<<endl;
        }
        else
        {
            for(int i=1;;i++)
            {
                        long long int x ;
                int q=1;
                x=n*i;
                long long int z=x;
                while(x!=0)
                {
                    r=x%10;
                    x=x/10;
                    num[r]=true;
                    if(check(num)==1)
                        {
                            out<<"Case #"<<e-t<<": "<<z<<endl;
                        q=0;
                        break;
                        }
                }
                if(q==0)
                    break;
            }
        }


    }
    return 0;
}
