#include <iostream>

using namespace std;

int main()
{
    int T, tt;
    cin>>T;
    tt=0;
    int a[T][7];
    while(tt<T)
    {
        char x[8];
        cin>>a[tt][0];
        int i=1;
            cin>>x;
            while(i<=(a[tt][0]+1))
            {
                a[tt][i]=x[i-1]-'0';
                i++;
            }
        tt++;

    }
    for(int i=0;i<T;i++)
    {
        int c=0;
        int s=0;
        s=s+a[i][1];
        for(int j=2;j<=(a[i][0]+1);j++)
        {

            if(s<j-1)
               {
                c=c+(j-1)-s;
                s-=a[i][j-1];
                a[i][j-1]+=(j-1)-s;
                s+=a[i][j-1];
               }
            s=s+a[i][j];
        }
        cout<<"Case #"<<i+1<<": "<<c<<endl;
    }

return 0;
}
