#include<fstream>
#include<string>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int main()
{
	string st;
	int t,n,curr,ans,q,i;
	cin >> t;
	for(q=1;q<=t;q++)
	{
		cin >> n;
		st.clear();
		ans=0;
		curr=0;
		cin >> st;
		for(i=0;i<=n;i++)
		{
			
           if (st[i]!='0')
           {
            	if (curr<i)
        	        {
        		      ans+=i-curr;
        		      curr=i;
        	        }
        	curr+=int(st[i])-48;
           }
        }
            cout << "Case #" << q << ":" << " " << ans << "\n";
   }
	return 0;
}
