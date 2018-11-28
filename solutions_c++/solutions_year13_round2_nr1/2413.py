#include<iostream>
#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<algorithm>
using namespace std;
using std::ifstream;
using std::ofstream;
#define size 10000

int answer(int A, int top)
{
	for(int i=0;i<top;i++)
	{
		A=2*A-1;
	}
	return A;
}

int main()
{
	ofstream out;
	out.open("output.txt");

	int T, A,N,top, target, ans, br, tar;
	int a[size], b[size], c[size];
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>A>>N;
		for(int j=0;j<N;j++)
			cin>>a[j];

		sort(a,a+N);
		ans=0;
		br=N;
		top=N-1;
		target=0;

		if(A!=1)
		{
			while(target<=top){
				if((N-target+ans)<br)
					br=N-target+ans;
				if(A>a[target])
				{
					A+=a[target];
					target++;
				}else{
					tar=target;
					while((tar<=top) && A<=a[target])
					{
						A=2*A-1;
						ans++;
					}
					A+=a[target];
					target++;
				}
			}
			if(br<ans)
				ans=br;
		}
		else ans=N;

		//ans
		cout<<"Case #"<<i<<": "<<ans<<endl;
		out<<"Case #"<<i<<": "<<ans<<endl;
	}

	out.close();

	return(0);
}