#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cout << #x << " : " << x << endl ;
int main()
{
	int t , k ;

	ifstream ip("in.txt");
	ofstream op("out.txt");

	ip>>t;
	//p.get(ch);

	double c , f , x , time , recovery_time , rate , cookie ;
	for(k=1;k<=t;k++)
	{
		ip >> c >> f >> x ;
		//cout << c << " " << f << " " << x << endl ;
		time = 0 ; rate = 2.0 ;
		cookie = c ; recovery_time = (c/f) ;

		while( 1 ) {
			time += (c/rate) ;
			//dbg(cookie) ; dbg(time) ;
			if( ( recovery_time*rate + cookie ) >= x ) { time += ( (x-cookie)/rate ) ; break ; }
			 rate += f ;
		}

		//p.getline(str,300);
		op << "Case #" << k <<": " ;

		op << fixed << setprecision(7) << time << endl ;
		//printf("%.7lf\n" , time ) ;


	}
	ip.close();
	op.close();
	return 0;
}
