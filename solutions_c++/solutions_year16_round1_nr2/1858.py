
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;


int tt;
int cur,ans,nn;

int main()
{
	freopen("bl.in","r",stdin);
	freopen("bl.out","w",stdout);

	cin >> tt;

	for (int ii=1;ii<=tt;++ii)
	{



        int hh[2505];
        for (int i = 0; i < 2504; ++i) {  hh[i] = 0;}

	    cin>>nn;


	    nn= nn*(2 * nn - 1);
	    for (int jj= 0; jj < nn;  ++jj)

	        {

	            cin >> cur;

	            if (hh[cur] )
	           { hh[cur]= 0;}
	            else
	           { hh[cur] = 1;}

	        }

        cout<<"Case #" <<ii<<": ";

        for (int mm = 0; mm< 2504; ++ mm)
          if(hh[mm])  cout<<" "<<mm;
        	cout <<endl;
	}



	return 0;
}
