#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	int t=1,T;
	cin>>T;
	while(t<=T)
	{
		int n,i,w=0,dw=0;
		double a_a[1000],b_a[1000];
		map<double,int> a,b;
		cin>>n;
		for(i=0;i<n;i++)
        {
            cin>>a_a[i];
            a.insert(pair<double,int>(a_a[i],1));
        }
		for(i=0;i<n;i++)
        {
            cin>>b_a[i];
            b.insert(pair<double,int>(b_a[i],1));
        }
		map<double,int>::iterator it,it2,it3;
		it=a.begin();
		while(it!=a.end())
        {
            it2=b.upper_bound(it->first);
            if(it2==b.end())
            {
                it2=b.begin();
            }
            if(it->first > it2->first)
                w++;
            it3=it;
            it++;
            a.erase(it3);
            b.erase(it2);

        }

        for(i=0;i<n;i++)
        {
            a.insert(pair<double,int>(a_a[i],1));
            b.insert(pair<double,int>(b_a[i],1));
        }
        while(a.size()!=0 && b.size()!=0)
        {
            it=a.end();
            it2=b.end();
            it--;
            it2--;
          //  cout<<"at end "<<it->first<<" "<<it2->first<<endl;
            if(it->first > it2->first)
            {
                dw++;
                a.erase(it);
                b.erase(it2);
            }
            else
            {
                a.erase(a.begin());
                b.erase(it2);
            }
        }

		cout<<"Case #"<<t<<": "<<dw<<" "<<w<<endl;
		t++;
	}
	return 0;
}
