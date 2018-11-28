#include <iostream>
#include <cmath>

using namespace std;
#define lli long long int

int main() {
    std::ios_base::sync_with_stdio(false);
	lli test,k;
	cin>>test;
    for(k=1;k<=test;k++)
    {
        lli n,newnum,copy;
        cout<<"Case #"<<k<<": ";
        cin>>n;
        copy=n;
        lli freq[12]={0},flag=0,digit,ans,i;
        if(n==0) cout<<"INSOMNIA"<<endl;
        else
        {
            i=1;
            newnum=n;
            while(flag!=10)
            {
                newnum=copy*i;
                n=newnum;
                while(n)
                {
                    // cout<<"hello  "<<i<<endl;
                    digit=n%10;
                    n=n/10;
                    // cout<<"newnum= "<<newnum<<" n= "<<n<<"  digit="<<digit<<"  ";
                    if(freq[digit]==0)
                    {
                        freq[digit]++;
                        flag++;
                    }
                    // cout<<"flag="<<flag<<endl;
                    if(flag==10)
                        break;
                }    
                if(flag==10)
                {
                    ans=newnum;
                    break;
                }
                i++;
                    
            }
            cout<<ans<<endl;
        }
        
        
    }
	return 0;
}
