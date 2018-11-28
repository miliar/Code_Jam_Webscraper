#include <iostream>
#include <fstream>
using namespace std;

bool allTrue (bool values[]) {
    for (int j=0;j<10;j++) {
        if (!values[j])
		{
            return false;
		}
	}
    return true;
}

int main()
{
    FILE *fin = freopen("A-small-attempt2.in", "r", stdin);
	FILE *fout = freopen("A-small.txt", "w", stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else
        {
            bool a[10]={false};
            int q=1;
            while(true)
            {

                int x=n*(q++);
                while(x>0)
                {
                    a[x%10]=true;

                    x=x/10;
                }
                if(allTrue(a))
                {
                    cout<<"Case #"<<i<<": "<<n*(q-1)<<endl;
                    break;
                }
            }
		}
	}
	return 0;
}
