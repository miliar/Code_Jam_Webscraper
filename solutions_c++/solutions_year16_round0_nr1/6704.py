#include<iostream>
using namespace std;
int main()
{
    long long int a,b[10],j,r,temp,sm,t[100],o[100],ip,x,flag[100];
    cin>>ip;
    for(x=0;x<ip;x++)
        cin>>t[x];
    for(x=0;x<ip;x++)
    {
        j=1;
        sm=0;
        if(t[x]==0)
        {
            flag[x]=0;
            continue;
        }
        for(int i=0;i<10;i++)
            b[i]=0;
        while(sm!=10)
        {
            o[x]=r=t[x]*j;
            while(r!=0)
            {
                temp=r%10;
                switch(temp)
                {
                    case 0: b[0]=1;
                            break;
                    case 1: b[1]=1;
                            break;
                    case 2: b[2]=1;
                            break;
                    case 3: b[3]=1;
                            break;
                    case 4: b[4]=1;
                            break;
                    case 5: b[5]=1;
                            break;
                    case 6: b[6]=1;
                            break;
                    case 7: b[7]=1;
                            break;
                    case 8: b[8]=1;
                            break;
                    case 9: b[9]=1;
                            break;
                }
                r/=10;
            }
            j++;
            sm=0;
            for(int i=0;i<10;i++)
                sm+=b[i];
        }
    }
    for(x=0;x<ip;x++)
    {
        cout<<"Case #"<<x+1<<": ";
        if(flag[x]==0)
            cout<<"INSOMNIA";
        else
            cout<<o[x];
        cout<<endl;
    }

}
