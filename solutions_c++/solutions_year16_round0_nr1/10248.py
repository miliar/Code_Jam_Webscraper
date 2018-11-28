/* 15-03-2016*/

/*

         Do not go gentle into that good night,
         Old age should burn and rave at close of day;
         Rage, rage against the dying of the light.
         Though wise men at their end know dark is right,
         Because their words had forked no lightning they
         Do not go gentle into that good night.


*/
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define MAXX 100000009


int main()
{

	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int t;
	in>>t;
	int TT=t;
	while(t--)
	{
		int n;
		in>>n;
		out<< "Case #" << TT-t << ": ";
		if(n==0){
			out<<"Insomnia\n";
		}
		else {
			map<long long int,int>m;
			for(int i=1;;i++){
				long long int N=i*n;
				while(N){
					m[N%10]++;
					N/=10;
				}
				int f=0;
				for(int i=0;i<=9;i++){
					f+=(m[i]>0);
				}
				if(f==10){
					out<<i*n<<"\n";
					break;
				}
			}
		}
	}
	in.close();
	out.close();
	return 0;
}




