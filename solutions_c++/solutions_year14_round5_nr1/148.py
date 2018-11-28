#include <iostream>
using namespace std;

long long trans[1000010];
long long psum[1000010];

int main()
{
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	
	int T; cin >> T;
	for(int tc=0; tc<T; tc++)
	{
		long long p, q, r, s;
		int N;
		cin >> N >> p >> q >> r >> s;
		//cout << p << " " << q << " " << r << " " << s << endl;
		for(int i=0; i<N; i++)
		{
			trans[i]=(i*p+q)%r+s;
			//cout << trans[i] << " ";
		}
		//cout << endl;
		psum[0]=0;
		for(int i=1; i<=N; i++) psum[i]=psum[i-1]+trans[i-1];
		
		
		
		long long tot=psum[N]; int b=0;
		long long ans=tot;
		for(int a=0; a<N; a++)
		{
			long long rem=tot-psum[a];
			
			b=max(a+1,b);
			
			while(2*(psum[b]-psum[a])<rem)
			{
				b++;
			}
			ans=min(ans, max(psum[a], max(psum[b]-psum[a], tot-psum[b])));
			if(b>a+1) 
			ans=min(ans, max(psum[a], max(psum[b-1]-psum[a], tot-psum[b-1])));
			/*cout << a << " " << b << endl;
			cout << ans << endl;
			cout << psum[a] << " " << psum[b]-psum[a] << " " << tot-psum[b-1] << endl;*/
		}
		
		double prob=tot-ans;
		prob/=tot;
		//cout << tot << " " << ans;
		
		cout << "Case #" << tc+1 << ": ";
		printf("%.10f\n", prob);
	}
}
