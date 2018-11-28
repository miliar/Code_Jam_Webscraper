#include <iostream>

using namespace std;


int main()
{
    int t, n, flag, A[10], x, num, rem, h;
    for(int z=0; z<10; z++)
        A[z]=0;
    cin>>t;
    for(int x=1; x<=t; x++)
    {
        flag=10;
        cin>>n; h=1;
        if(n==0) { cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl; flag=0;}
        while(flag>0)
            {
                num=h*n;  h=h+1;
                while(num>0 && flag!=0)
                {
                    rem=num%10;
                    for(int f=0; f<10; f++)
                    {
                        if(rem==f)
                        {
                            if(A[f]==0)
                            {
                                A[f]=1; flag=flag-1;
                            }

                        }
                    }
                    num=num/10;
                }
            }
            if(n!=0){ for(int y=0; y<10; y++)A[y]=0; cout<<"Case #"<<x<<": "<<(h-1)*n<<endl;}



    }
    return 0;
}
