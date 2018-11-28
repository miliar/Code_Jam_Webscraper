/*#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
	ifstream infile("A-small-attempt4.in");
	ofstream outfile("outfile.out");
	int T;
	infile>>T;
	for(int i=1;i<=T;i++)
	{
		
		vector<int> V;
		int A,N;
		infile>>A>>N;
		if(A==1) {outfile<<"Case #"<<i<<": "<<N<<endl;continue;}
		for(int j=1;j<=N;j++)
		{
			int m;
			infile>>m;
            V.push_back(m);
		}
		for(int j=0;j<N;j++){
			for(int k=0;k<N-1;k++)
			{
				if(V.at(k)>V.at(k+1))
				{
					int mm=V.at(k);
					V.at(k)=V.at(k+1);
					V.at(k+1)=mm;
				}
			}
		}
		
		int min=0;
		int r=1;
		while(r<=N)
		{
			
			while(r<=N)
			{
				if(V.at(r-1)<A)
				{
				  A+=V.at(r-1);
				  r++;
				}
				else break;
			}
			if(r>N) {break;}
			if(r==N) {min++;break;}

			int same=1,u=A,rr=r;
			 
			while(V.at(N-same)==V.at(N-same-1))  { 
				same++;u=u+u-1;
				while(rr<=N)
				{
					if(V.at(rr-1)<u)
					{
						u+=V.at(rr-1);
						rr++;
					}
					else break;
				}
			}
			if(same){
                 if(u-1>V.at(N-1-same)-V.at(N-1-same-1)) A=u;
				 else N-=same;
			}
			else {
				if(A-1>V.at(N-1)-V.at(N-2)) A+=A-1;
				else N--;
			}
			
			
			min++;
		}
		
		outfile<<"Case #"<<i<<": "<<min<<endl;
	}

}*/

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("mote.out");

	int times = 0;
	in >> times;
	for (int num = 0;num < times;num++)
	{
		int me = 0;
		in >> me;
		int all = 0;
		in >> all;
		vector<int> vec1;
		for (int i = 0;i < all;i++) { int temp = 0; in >> temp; vec1.push_back(temp); }
		sort(vec1.begin(),vec1.end());
		int minP = all;

		if (me == 1)
		{
			out << "Case #" << num + 1 << ": " << all << '\n';
			continue;
		}

		for (int i = 0;i <= all;i++)
		{
			int t = 0;
			int current = me;
			for (int j = 0;j < i;j++)
			{
				if (current > vec1[j]) { current += vec1[j]; }
				else
				{
					int p = 0;
					int m = 0;
					m = (vec1[j] + 1 - current) / (current - 1);
					if ((vec1[j] + 1 - current) % (current - 1)) { m++; }
					m += 1;
					int flag = 0;
					while (m != 1) { if (m % 2) flag = 1; m /= 2; p++; }
					if (flag) p++;

					int mult = 1;
					for (int k = 0;k < p;k++) { mult *= 2; }
					mult--;
					current += mult * (current - 1);
					current += vec1[j];
					t += p;
				}
			}
			t += all - i;
			if (t < minP) minP = t;
		}

		out << "Case #" << num + 1 << ": " << minP << '\n';
	}
	return 0;
}
