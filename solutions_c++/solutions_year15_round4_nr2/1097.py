#include<iostream>
#include <utility>
#include <vector>
#include <cmath>


using namespace std;

void takeInputAndProcess()
{
	int N;
	double R,X;
	cin >> N >> R >> X;
	double p[N],q[N];
	for(int i=0;i<N;i++)
		cin >> p[i] >> q[i];
	
	if(N == 1 && q[0] != X)
	{
		cout << "IMPOSSIBLE";
		return;
	}
	cout.precision(15);
	if(N == 1 && q[0] == X)
	{
		double r =1.0*R;
		r = r/p[0];
		cout << r;
		return;
	}
	if(N == 2)
	{
		double pt,qt;
		pt = X*R*1.0;
		pt = pt-(q[0]*R*1.0);
		if(q[1] != q[0])
		{pt = pt/((q[1]-q[0])*1.0);
		
	       qt = X*R*1.0;
	       qt = qt-(q[1]*R*1.0);
	       qt = qt/((q[0]-q[1])*1.0);
	      
		if(pt < 0 || qt <0)
		{
		   cout << "IMPOSSIBLE";
		   return;
		}		
	       pt = pt/p[1];
		qt = qt/p[0];
	      if(pt > qt)
		cout << pt;
		else
		cout << qt;
	      }
	      else if(q[1] == X)
	      {
		double ptr = 1.0*R;
		ptr = ptr/(p[1]+p[0]);
		cout << ptr;
	      }
	      else
	      {
		cout << "IMPOSSIBLE";
                return;
	      }
	}

}

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
	   cout << "Case #" << i << ": " ;
            takeInputAndProcess();
            cout << endl;
	}
	return 0;
}
