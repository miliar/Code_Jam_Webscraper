#include <iostream>
#include <string>
#include <bitset>
using namespace std;


int tt;
int cur, ans;
bool inso;//INSOMNIA;

string ss;

int main() 
{
	freopen("bl.in","r",stdin);
	freopen("bl.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii)
	{
    	ans = 0;
        cin >> ss; 
        ss = ss + "+";
        
        for (int jj = 0; jj<ss.length()-1;++jj) 
            {
                if(ss[jj] != ss[jj+1]) ++ans;
            }
            
    
    	printf("Case #%d: %d\n",ii,ans);	
	}
	return 0;
}
