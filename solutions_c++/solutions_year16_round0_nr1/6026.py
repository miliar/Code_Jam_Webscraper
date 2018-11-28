#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t,asd[10],i,j,k,l;
	long long int inp,count,temp;
	cin>>t;
	for(l=1;l<=t;l++)
    {
        for(i=0;i<10;i++)
        {
            asd[i]=0;
        }
        cin>>inp;
        if(inp==0)
        {
            cout<<"Case #"<<l<<": INSOMNIA\n";
            continue;
        }
        count = inp;
        k=0;
        while(1)
        {
            temp = inp;
            k=0;
            while(temp)
            {
                j = temp % 10;
                asd[j] = 1;
                temp /= 10;
            }
            for(j=0;j<10;j++)
            {
                k+=asd[j];
            }
            if(k==10)
            {
                break;
            }
            inp += count;
        }
        cout<<"Case #"<<l<<": "<<inp<<endl;
    }
}
