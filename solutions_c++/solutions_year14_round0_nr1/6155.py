#include<iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    int a[16], b[16];
    int x, y, i, j, k;
    j=1;
    int m;
    int n;
    while(T--)
    {
        m = -1;
        n = 0;
        cin>>x;
        for(i=0;i<16;++i)
            cin>>a[i];
        cin>>y;
        for(i=0;i<16;++i)
            cin>>b[i];
        
        x = x*4 - 4;
        y = y*4 - 4;
        for(i=0;i<4;++i)
        {
            for(k=0;k<4;++k)
            {
                if(a[x+i]==b[y+k])
                {
//                    cout<<"Match i = "<<i<<" k = "<<k<<endl;
                    m=a[x+i];
                    if(n==1)
                    {
                        n=2;
                        break;
                    }
                    if(n==0)
                        n = 1;
                    
                }
            }   
        }


        if(m==-1)
            cout<<"Case #"<<j<<": Volunteer cheated!"<<endl;
        else if (m!=-1 && n<2)
            cout<<"Case #"<<j<<": "<<m<<endl;
        else
            cout<<"Case #"<<j<<": Bad magician!"<<endl;
        j++;
    }
    return 0;
}

    
