#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void sortit(vector <int> &ff,int l,int r){
	
	int ll = l;int rr = r;int mid = ff[(l+r)/2];
	while (ll<=rr)
	{
		while (ff[ll]<mid) ll++;
		while (ff[rr]>mid) rr--;
		if (ll<=rr) {swap(ff[ll],ff[rr]);ll++;rr--;}
	}
	if (ll<r) sortit(ff,ll,r);
	if (l<rr) sortit(ff,l,rr);

}

int main()
{
	int n,i,m,t,temps,taild,cnt1,taild1 ,ans;
	int m1;
	vector<int> totd;
	ifstream ist1("input1.in");
	ofstream ost1("output1.out");
	int a[1000],b[1000];
	ist1 >> n;

	for (int i = 1;i<=n;i++)
	{
		totd.clear();
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		cnt1 = 0;
		ist1 >> m >> t; 
		ans = t;
		//cout<<m<<" "<<t<<endl;
		for (int i1 = 0;i1<=t-1;i1++)
		{ist1 >> temps;totd.push_back(temps);b[i1] = t - i1 - 1;//cout<<temps<<" ";
		}
		//cout<<endl;
		if (m == 1) ost1<<"Case #"<<i<<": "<<t<<endl;else {
		sortit(totd,0,totd.size()-1);
		//ost1 <<totd[0]<<totd[1]<<endl;
		taild = totd.size()-1;
		for (int i1 = 0;i1<=taild;i1++)
		{
			if (m > totd[i1]) m += totd[i1];
			else {
						m1 = m;
						while (m1 <= totd[i1])
						{
							m1 = m1 * 2 -1;
							cnt1++;
						}
						m1 += totd[i1];
						m  = m1;
				}
			a[i1] = cnt1;
		}
		
		for (int i1 = 0;i1<=taild;i1++)
		{
			//cout<<a[i1]<<" "<<b[i1]<<endl;
			if (ans > a[i1] + b[i1]) ans = a[i1] + b[i1];
		}
		ost1<<"Case #"<<i<<": "<<ans<<endl;
		}
		//system("pause");
	}
	ost1.close();
	system("pause");
}