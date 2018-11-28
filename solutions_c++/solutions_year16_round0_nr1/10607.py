#include<iostream>

using namespace std;

int main()
{
    int t;
    unsigned long long int n,r,m,i,k,p,q;

    cin>>t;

    int j=1;

    while(t--)
    {
        int cnt=0;

        p=1;
        int flag=0;
        cin>>n;
        m=n;
        if(n==0)
            {
               cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
                j++;
            }
            else
            {
                int h[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
                while(flag==0)
                {

                    while(m>0)
                    {
                        r=m%10;
                        h[r]=r;
                        m=m/10;

                    }

                    //for(k=0;k<10;k++)
                        //cout<<h[k]<<" ";

                    //cout<<endl;

                    cnt=0;
                    for(i=0;i<10;i++)
                    {
                        if(h[i]>=0)
                        {
                            cnt++;
                        }
                    }

                    //cout<<cnt<<endl;

                    if(cnt<10)
                        {
                            p++;
                            m=n*p;
                            q=m;

                        }
                    else
                       if(cnt==10)
                        {
                            flag=1;
                        }


            }

            cout<<"Case #"<<j<<": "<<q<<endl;
            j++;
        }


    }

    return 0;

}
