#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
int main()
{
	
	//freopen("C:\\Users\\Balasubramanian\\Downloads\\B-large.in", "r", stdin);
    //freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\output22.out", "w", stdout);
    long double c,f,x;int t;
    cin>>t;int count=0;
    while(t--){
    count++;
    cin>>c>>f>>x;
    long double tim=0.0;
    long double speed=2.0;
	int t=1;
	while(t)
	{
		if(x<=c){
			tim+=(x/speed);
			t=0;break;
		}
		else{
		
		if(((c/speed)+(x/(speed+f)))<=(x/speed))
		{
			tim+=((c/speed));
			speed+=f;
		}
		else{
			tim+=(x/speed);
			t=0;break;
		}
	}
	}
	cout<<"Case #"<<count<<": "<<fixed<<showpoint<<setprecision(7)<<tim<<endl;
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
