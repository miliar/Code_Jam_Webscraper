#include <iostream>
bool a[10];
bool check()
{
    int i;
    for(i=0;i<10;i++)
    {
        if(a[i]==false)
            return false;
    }
    return true;
}
int main()
{
    int n;

    std::cin>>n;

    if(1<=n && n<=100)
    {
        for(int inst=0;inst<n;inst++)
        {
            int i;
            long num,temp,temp2;

            std::cin>>num;
            std::cout << "Case #" << (inst+1) << ": ";
            for(i=0;i<10;i++)
                a[i]=false;

            if(num == 0)
                std::cout<<"INSOMNIA"<<std::endl;
            else
            {
                int tn=1;
                while(!check())
                {
                    temp = tn*num;
                    temp2=temp;
                    while(temp2>0)
                    {
                        a[temp2%10]=true;
                        temp2/=10;
                    }
                    tn++;

                }
                std::cout<<temp<<std::endl;
            }
        }
    }
}
