#include <iostream>
#include <algorithm>
#include <iomanip>
#include <climits>
#include <cstring>

using namespace std;

int main()
{
int T,z,x,r,c,fl,q;

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin >> T;
for(z=1;z<=T;z++)
{
fl=0;
cin >> x >> r >> c;
if(x==1)
fl=0;
else if(x==2){
	if(r%2==0 || c%2==0)
	fl=0;
	else
	fl=1;
}
else if(x==3){
	if((r%3==0 && c>=2 )||(c%3==0 && r>=2))
	fl=0;
	else
	fl=1;
}
else{
	if((r%4==0 && c>=3 )||(c%4==0 && r>=3))
	fl=0;
	else
	fl=1;
		
}
cout<<"Case #"<< z <<": ";
if(fl==0)
cout << "GABRIEL" << endl;
else
cout << "RICHARD" << endl;


}

return 0;
}


