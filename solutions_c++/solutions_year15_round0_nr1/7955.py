//case#1
/*< SHRI GANESHAY NAMAH >*/
/* <rakesh kumar pal >*/
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <string.h>
#include <bitset> 
#include <vector>
#include <iomanip>
#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
int main()
{
	//ofstream output;
	//output.open("output.out");
	//ifstream inp;
	//inp.open("A-small-attempt0.in");
	int test=0;
	cin>>test;
	//inp>>test;
	int t=1;
	while(t<= test)
	{
		int smax=0;
		cin>>smax;
		//inp>>smax;
		string st;
		cin>>st;
		//inp>>st;
		int len = st.length();
		int total = 0,k=0;
		int invite = 0;
		int inv = 0;
		for(k=0;k<len;++k)
		{
			/*
			cout<<" invite :"<<invite<<endl;
			cout<<" total :"<<total<<endl;
			cout<<" k :"<<k<<endl;
			cout<<" val :"<<st[k]-48<<endl;
			 */
			invite = 0;
			if(k>0 && total<k && (st[k]-48 )> 0)
			{
				invite = k-total;
				inv = inv + invite;
				total = total + invite;
			}
			
			total+=st[k]-48;
			
		}
		cout<<"Case #"<<t<<": "<<inv<<endl;
		//output<<"Case #"<<t<<": "<<invite<<endl;
		++t;
	}
	//inp.close();
	//output.close();
	return 0;
}