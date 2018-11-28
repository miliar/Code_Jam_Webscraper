#include <iostream>
#include <string>
#include <bitset>
using namespace std;

string cc;
int tryNO(100);
int tt;
int cur, ans,xx;
bool inso;//INSOMNIA;

int main() {
	freopen("al.in","r",stdin);
	freopen("al.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii)
	{
	ans = 0;
	inso = true;
    cin >> cur; 
    std::bitset<16> myFlag(0x03FF); 

	
	for (int jj = 1; jj<tryNO && myFlag != 0; ++jj)
	{
		xx = jj * cur;
		cc = to_string(xx);
			for(int mm = 0; mm < cc.length(); ++mm)
				{myFlag.reset(cc[mm]-'0');}
									
						if (!static_cast<unsigned short>( myFlag.to_ulong() ) ) 
							{
								ans = xx;
								inso = false;
								break;
							}					

	}


	if (inso)
	printf("Case #%d: INSOMNIA\n",ii);
	
	else
	printf("Case #%d: %d\n",ii,ans);	
		
		
	}
	return 0;
}
