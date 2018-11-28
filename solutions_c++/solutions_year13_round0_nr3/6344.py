#include <iostream>
#include <sstream>
#include <string.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

int sq(int tmp)
{
    int i = 1;
    for(i=1;i*i<tmp;i++);

    return i;
}

int check(char tmp[])
{
    char ch[100];
    int i,j=strlen(tmp);

    for(i=0;i<strlen(tmp);i++)
    {
        ch[i] = tmp[j-1];
        j--;
    }

    for(i=0;i<strlen(tmp);i++)
    {
        if(ch[i] != tmp[i])
            return 0;
    }
    return 1;
}

int main()
{
    int t,a,b,n,num,sum;
    char tmp[100];
    ifstream cin("C-small-attempt0.in");
    ofstream cout("C.out");

    while(cin>>t)
    {
        n = 0;

        while(t--)
        {
            n++;
            sum = 0;
            cin >> a >> b;
            memset(tmp,0,sizeof(tmp));
            while(a<=b)
            {
                num = sq(a);
                itoa(a,tmp,10);
                if(num*num == a&&check(tmp) == 1)
                {
                    itoa(num,tmp,10);

                    if(check(tmp) == 1)
                        sum++;

                }

                a++;
            }

            cout <<"Case #"<<n<<": "<<sum<<endl;
        }
    }

}
