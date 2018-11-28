	#include <fstream>
	#include <cstring>
	
	using namespace std;
	
	ifstream in("d.in"); ofstream out("d.out");
	int T, l=1;
	
	int main()
	{
	in>>T;
	while(T--)
	{
	 int K, C, S;
	 in>>K>>C>>S;
	 out<<"Case #"<<l<<": ";
	 for(int i = 1; i<=K; i++) out<<i<<" ";
	 out<<endl; l++;
	}
}


