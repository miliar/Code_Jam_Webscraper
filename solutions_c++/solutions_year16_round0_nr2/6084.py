#include<iostream>
using namespace std;
int main()
{
	string inp;
	int i,j,k,l,t,n;
	cin>>t;
	for(l=1;l<=t;l++)
    {
        cin>>inp;
        n=0;
        k=inp.length();
        for(i=0;i<k-1;i++)
        {
            if(inp[i]!=inp[i+1])
            {
                n++;
            }
        }
        if(inp[k-1]=='-')
            n++;
        cout<<"Case #"<<l<<": "<<n<<endl;
    }
}
