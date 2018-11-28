#include <vector>
#include <algorithm> 
#include <fstream>

using namespace std;
typedef vector<double> vd;

ifstream in("D-large.in"); ofstream out("d.out");
int T,m=1;
double tmp;

int main()
{
	in>>T;
	while(T--)
	{
		int N; vd naomi, ken;
		in>>N;
		for(int i=0;i<N;i++) {in>>tmp;naomi.push_back(tmp);}
		for(int i=0;i<N;i++) {in>>tmp;ken.push_back(tmp);}
		int war=N,dwar=0;
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		
		int k=0,l=0;
		while(k<N&&l<N)
		{
			if(naomi[k]<ken[l]){war--;k++;l++;} else l++;
		}
		
		k=0;l=0;
		while(k<N&&l<N)
		{
			if(naomi[k]>ken[l]){dwar++;k++;l++;} else k++;
		}
		
		
		out<<"Case #"<<m<<": "<<dwar<<" "<<war<<endl;
		m++;
		
		}
}

