#include <iostream>
#define smaxn 1001
using namespace std;
int main ()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin >> t;
	for (int tn = 0 ; tn < t ; tn++)
	{
		int smax;
		cin >> smax;
		int peo [smaxn];
		char peoin [smaxn];
		cin >> peoin ;
		for(int q = 0 ; q < smax+1 ; q++ )
		{
			peo[q] = peoin [q] - '0';
			
		}
		

		int fri = 0;
		int claped = 0;
		for(int q = 0 ; q < smax+1 ; q++ )
		{
			//cout << q <<":("<<claped<<") ";
			if(claped < q && peo[q]>0)
			{
				fri += (q - claped) ;
				claped = q;
				//cout << ". need :" << (q - claped) ;
			}
			//cout<<endl;
			claped += peo [q];
		}
		cout << "Case #" << (tn+1) << ": " << fri << endl;
	}
	

}